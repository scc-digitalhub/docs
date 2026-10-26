# Test the model

There are three ways to test the model:

| Where the model runs | How you reach it | Protocols |
| --- | --- | --- |
| On the platform | [CLI port-forward](#test-the-service-on-the-platform) from your computer | REST |
| On your computer | [Docker](#run-the-model-on-your-computer), with the same serve image | REST and gRPC |
| On a Raspberry Pi | [Docker](#run-the-model-on-a-raspberry-pi) on the device | REST and gRPC |

In all cases the API is the same, so the [Python client](#send-a-picture) works everywhere: only the address changes.

## Test the service on the platform

The default ClusterIP service is reachable inside the cluster. The CLI opens an authenticated **port-forward**: a local port that forwards each request to the service, through the platform proxy. It carries HTTP requests, so it can be used for the REST API only.

**1. Log in and check the service** (log in again when the CLI answers `401`):

```sh
dhcli login
dhcli services -p tvm-test
```

**2. Open the port-forward** in a first terminal, and keep it open:

```sh
dhcli port-forward -p tvm-test -f yolo-function -l 18080
```

```
✔ Port-forward listening on localhost:18080
```

`-f` selects the most recent running service of the function; pass a run ID instead to choose a specific one. `-l` is the local port: any free port works.

**3. Check the service** in a second terminal:

```sh
curl http://localhost:18080/v2/models/yolo-function
```

```json
{
  "name": "yolo-function",
  "versions": ["1"],
  "inputs": [{ "name": "images", "datatype": "FP32", "shape": [1, 3, 640, 640] }],
  "outputs": [{ "name": "output0", "datatype": "FP32", "shape": [1, 84, 8400] }]
}
```

The optional `platform` field differs between Go and Rust; the tensor signature is
what the client uses. Health endpoints indicate success with HTTP `200`, and may
have an empty body.

The model expects one `FP32` picture of 640×640 pixels in NCHW order, and returns 8400 candidate boxes, each with 4 coordinates and 80 class scores.

## Send a picture

Download a test picture:

```sh
curl -fL -o bus.jpg https://ultralytics.com/images/bus.jpg
```

Save this script as `client.py`. It reads the model signature, prepares the picture, calls the inference endpoint prints detected objects and saves `detections.jpg`. Set `URL` to the address of the service.

```python
import json
import urllib.request

import numpy as np
from PIL import Image, ImageDraw

URL = "http://localhost:18080"   # port-forward, or http://localhost:8080 with Docker
MODEL = "yolo-function"          # the served name

# 1. Read the model signature
meta = json.load(urllib.request.urlopen(f"{URL}/v2/models/{MODEL}", timeout=30))
spec = meta["inputs"][0]
_, _, height, width = spec["shape"]          # [1, 3, 640, 640]

# 2. Prepare the picture: resize, scale to [0, 1], HWC -> NCHW
image = Image.open("bus.jpg").convert("RGB").resize((width, height))
tensor = (np.asarray(image, dtype=np.float32) / 255.0).transpose(2, 0, 1)[None]

# 3. Call the Open Inference v2 endpoint
body = {"inputs": [{"name": spec["name"], "datatype": "FP32",
                    "shape": list(tensor.shape), "data": tensor.ravel().tolist()}]}
request = urllib.request.Request(f"{URL}/v2/models/{MODEL}/infer", data=json.dumps(body).encode(),
                                 headers={"Content-Type": "application/json"})
result = json.load(urllib.request.urlopen(request, timeout=300))

# 4. Read the output [1, 84, 8400]: 4 box values (cx, cy, w, h) + 80 class scores per candidate
output = result["outputs"][0]
pred = np.asarray(output["data"], dtype=np.float32).reshape(output["shape"])[0]
scores, classes = pred[4:].max(axis=0), pred[4:].argmax(axis=0)
boxes = np.stack([pred[0] - pred[2] / 2, pred[1] - pred[3] / 2,
                  pred[0] + pred[2] / 2, pred[1] + pred[3] / 2], axis=1)

# 5. Keep the best boxes and drop the overlapping duplicates (non-maximum suppression)
def area(b):
    return np.prod(np.maximum(b[..., 2:] - b[..., :2], 0), axis=-1)

kept = []
for i in np.argsort(-scores):
    if scores[i] < 0.25:
        break
    same_class = [j for j in kept if classes[j] == classes[i]]
    top_left = np.maximum(boxes[i, :2], boxes[same_class, :2])
    bottom_right = np.minimum(boxes[i, 2:], boxes[same_class, 2:])
    overlap = np.prod(np.clip(bottom_right - top_left, 0, None), axis=1)
    union = area(boxes[i]) + area(boxes[same_class]) - overlap
    if np.all(overlap / np.maximum(union, 1e-9) < 0.45):
        kept.append(i)

draw = ImageDraw.Draw(image)
for i in kept:
    x1, y1, x2, y2 = boxes[i]
    print(f"class {classes[i]:2d}  score {scores[i]:.2f}  box ({x1:.0f}, {y1:.0f}) - ({x2:.0f}, {y2:.0f})")
    draw.rectangle((x1, y1, x2, y2), outline="red", width=2)
image.save("detections.jpg")
```

```sh
python3 client.py
```

Class `0` means *person* and class `5` means *bus* for this COCO-trained model.
Coordinates refer to the resized input image. Counts and scores depend on the
export, image and preprocessing; they are not a fixed expected result.

This small client resizes directly to show the full request/response flow. For an
accuracy evaluation, use the model's reference preprocessing (including letterbox
padding where required) and compare against the original model. Total HTTP latency
includes JSON encoding, transfer and decoding; it is not pure inference time.

## Run the model on your computer

The compiled Model can run outside the platform with the same serve image. This works on a compatible Intel/AMD 64-bit computer with the `yolo-function-amd64` build.

**1. Download the compiled Model:**

```sh
dhcli download model -p tvm-test -n yolo-function-amd64 -d ./yolo-model
ls yolo-model        # metadata.json  model.so
```

**2. Start the serve image** with the model folder mounted in `/shared/model`:

```sh
docker run --rm -p 8080:8080 -p 9000:9000 \
  -v "$PWD/yolo-model:/shared/model" \
  -e TVM_MODEL_NAME=yolo-function \
  ghcr.io/scc-digitalhub/tvm-runtime-go:0.26.0
```

To use the Rust server instead, replace the image with `ghcr.io/scc-digitalhub/tvm-runtime-rust:0.26.0`.

**3. Test it** in another terminal: set `URL = "http://localhost:8080"` in `client.py`:

```sh
curl http://localhost:8080/v2/models/yolo-function
python3 client.py
```

For gRPC, use port `9000` with an Open Inference v2 client. CORE's HTTP port-forward
does not carry gRPC. The [runtime guide](../../../runtimes/tvm/#endpoints) lists the RPC methods.

## Run the model on a Raspberry Pi

Use a Raspberry Pi with Docker and either a 64-bit OS (`linux/arm64`) or an
ARMv7-compatible 32-bit OS (`linux/arm/v7`, hard-float ABI and NEON). Both Go and Rust
runtime image builds include these platforms. Use a model matching the OS and CPU.

**1. Download the build for the device** (see [Compile for ARM devices](deploy.md#6-compile-for-arm-devices-optional)):

```sh
dhcli download model -p tvm-test -n yolo-function-arm64 -d ./yolo-model     # 64-bit OS
```

For an ARMv7-compatible 32-bit OS, use this command instead:

```sh
dhcli download model -p tvm-test -n yolo-function-arm32 -d ./yolo-model
```

If the CLI is not installed on the device, download the Model on your computer and copy the folder, for example with `scp -r yolo-model pi@<device>:`.

**2. Start the serve image**: Docker picks the ARM variant by itself.

```sh
docker run --rm -p 8080:8080 -p 9000:9000 \
  -v "$PWD/yolo-model:/shared/model" \
  -e TVM_MODEL_NAME=yolo-function \
  ghcr.io/scc-digitalhub/tvm-runtime-go:0.26.0
```

**3. Test it** from any computer of the same network, with `URL = "http://<device>:8080"` in `client.py`.

!!! tip "A Raspberry Pi in the cluster"

    When the Raspberry Pi is a node of the cluster, there is no need to start Docker manually: run `serve` with `model_path` set to the ARM Model. Both the runtime and init images must support the node architecture. CORE's default init image covers only AMD64 and ARM64, so an ARM32 node requires an ARMv7-compatible init image to download the model. Test the service with the port-forward, as in [the first section](#test-the-service-on-the-platform).

## Clean up

- Press **Ctrl+C** to close the port-forward and to stop the Docker containers.
- Stop the service on the platform when you no longer need it:

    ```sh
    dhcli stop <run-id> -p tvm-test
    ```

The Models stay in the project: a new `serve` run can deploy a compiled model again at any time, without building or compiling it.
