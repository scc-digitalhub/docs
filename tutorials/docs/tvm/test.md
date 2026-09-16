# Test the model

There are three ways to test the model:

| Where the model runs | How you reach it | Protocols |
| --- | --- | --- |
| On the platform | [CLI port-forward](#test-the-service-on-the-platform) from your computer | REST |
| On your computer | [Docker](#run-the-model-on-your-computer), with the same serve image | REST and gRPC |
| On a Raspberry Pi | [Docker](#run-the-model-on-a-raspberry-pi) on the device | REST and gRPC |

In all cases the API is the same, so the [Python client](#send-a-picture) works everywhere: only the address changes.

## Test the service on the platform

The service is reachable only from inside the platform. The CLI opens an authenticated **port-forward**: a local port that forwards each request to the service, through the platform proxy. It carries HTTP requests, so it can be used for the REST API only.

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
curl http://localhost:18080/v2/health/ready
```

```json
{"ready":true}
```

```sh
curl http://localhost:18080/v2/models/yolo-function
```

```json
{
  "name": "yolo-function",
  "versions": ["1"],
  "platform": "tvm",
  "inputs": [{ "name": "images", "datatype": "FP32", "shape": [1, 3, 640, 640] }],
  "outputs": [{ "name": "output0", "datatype": "FP32", "shape": [1, 84, 8400] }]
}
```

The model expects one `FP32` picture of 640×640 pixels in NCHW order, and returns 8400 candidate boxes, each with 4 coordinates and 80 class scores.

## Send a picture

Download a test picture:

```sh
curl -L -o bus.jpg https://ultralytics.com/images/bus.jpg
```

Save this script as `client.py`. It reads the model signature, prepares the picture, calls the inference endpoint and prints the objects found. Set `URL` to the address of the service.

```python
import json
import urllib.request

import numpy as np
from PIL import Image

URL = "http://localhost:18080"   # port-forward, or http://localhost:8080 with Docker
MODEL = "yolo-function"          # the served name

# 1. Read the model signature
meta = json.load(urllib.request.urlopen(f"{URL}/v2/models/{MODEL}"))
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
    return (b[..., 2] - b[..., 0]) * (b[..., 3] - b[..., 1])

kept = []
for i in np.argsort(-scores):
    if scores[i] < 0.25:
        break
    top_left = np.maximum(boxes[i, :2], boxes[kept, :2])
    bottom_right = np.minimum(boxes[i, 2:], boxes[kept, 2:])
    overlap = np.prod(np.clip(bottom_right - top_left, 0, None), axis=1)
    if np.all(overlap / (area(boxes[i]) + area(boxes[kept]) - overlap) < 0.45):
        kept.append(i)

for i in kept:
    x1, y1, x2, y2 = boxes[i]
    print(f"class {classes[i]:2d}  score {scores[i]:.2f}  box ({x1:.0f}, {y1:.0f}) - ({x2:.0f}, {y2:.0f})")
```

```sh
python3 client.py
```

The output looks like this:

```
class  0  score 0.89  box (529, 230) - (640, 520)
class  0  score 0.89  box (40, 236) - (189, 537)
class  5  score 0.88  box (4, 135) - (636, 443)
class  0  score 0.87  box (176, 239) - (272, 509)
class  0  score 0.61  box (-0, 326) - (61, 516)
```

Class `0` is *person* and class `5` is *bus* in the COCO dataset: the model found four people and the bus. The boxes are in the coordinates of the 640×640 input. Through the port-forward a request takes a few seconds, because the picture travels as about 12 MB of JSON.

## Use the test scripts

The [test_infer](https://github.com/scc-digitalhub/digitalhub-core/tree/runtime-tvm/runtimes/runtime-tvm/test_infer) scripts of the runtime do the same and draw the results on the picture: `yolo.py` for detection models, `xinet.py` for pose models (people with 17 keypoints).

```sh
git clone --branch runtime-tvm --depth 1 https://github.com/scc-digitalhub/digitalhub-core.git
cd digitalhub-core/runtimes/runtime-tvm/test_infer

python3 yolo.py --url http://localhost:18080 --function yolo-function
```

```
serve:     http://localhost:18080  model 'yolo-function'
input:     images FP32 [1, 3, 640, 640]
output:    output0 FP32 [1, 84, 8400]
picture:   810x1080 -> 640x640 letterbox, NCHW, [0,1]
inference: REST in 5501 ms -> output0 FP32 [1, 84, 8400]

detections with conf > 0.25, after NMS: 5
  person         conf 0.90  box (671,385)-(810,880)
  person         conf 0.88  box (222,407)-(344,856)
  person         conf 0.87  box (50,398)-(244,905)
  bus            conf 0.84  box (31,231)-(801,778)
  person         conf 0.43  box (0,549)-(59,868)
summary:   {'person': 4, 'bus': 1}
picture:   .../test_infer/output/yolo-function.jpg
```

| Option | Description |
| --- | --- |
| `--url` | Address of the service: the port-forward, or the Docker container. |
| `--function`{: style="white-space: nowrap" } | Function name, also used as model name. |
| `--model` | Model name, when the run sets a `served_name` different from the function name. |
| `--mode grpc` and `--grpc-url` | Use gRPC, e.g. `--mode grpc --grpc-url localhost:9000` with Docker. |
| `--image` | Local path or URL of the picture (default: `bus.jpg`). |
| `--conf` | Minimum confidence of the results. |

The [README](https://github.com/scc-digitalhub/digitalhub-core/blob/runtime-tvm/runtimes/runtime-tvm/test_infer/README.md) lists all the options.

## Run the model on your computer

The compiled Model can run outside the platform with the same serve image. This works on an x86 computer with the `yolo-function-x86` build.

**1. Download the compiled Model:**

```sh
dhcli download model -p tvm-test -n yolo-function-x86 -d ./yolo-model
ls yolo-model        # metadata.json  model.so
```

**2. Start the serve image** with the model folder mounted in `/shared/model`:

```sh
docker run --rm -p 8080:8080 -p 9000:9000 \
  -v "$PWD/yolo-model:/shared/model" \
  -e TVM_MODEL_NAME=yolo-function \
  ghcr.io/scc-digitalhub/tvm-runtime-go:0.25
```

To use the Rust server instead, replace the image with `ghcr.io/scc-digitalhub/tvm-runtime-rust:0.25`.

**3. Test it** in another terminal: set `URL = "http://localhost:8080"` in `client.py`, or use the test scripts, also over gRPC:

```sh
curl http://localhost:8080/v2/models/yolo-function
python3 client.py
python3 yolo.py --url http://localhost:8080 --function yolo-function
python3 yolo.py --url http://localhost:8080 --grpc-url localhost:9000 --mode grpc --function yolo-function
```

## Run the model on a Raspberry Pi

The serve images are also published for `linux/arm64` and `linux/arm/v7`. On the device, with Docker installed:

**1. Download the build for the device** (see [Compile for ARM devices](deploy.md#6-compile-for-arm-devices-optional)):

```sh
dhcli download model -p tvm-test -n yolo-function-arm64 -d ./yolo-model     # 64-bit OS
dhcli download model -p tvm-test -n yolo-function-armv7l -d ./yolo-model    # 32-bit OS
```

If the CLI is not installed on the device, download the Model on your computer and copy the folder, for example with `scp -r yolo-model pi@<device>:`.

**2. Start the serve image**: Docker picks the ARM variant by itself.

```sh
docker run --rm -p 8080:8080 -p 9000:9000 \
  -v "$PWD/yolo-model:/shared/model" \
  -e TVM_MODEL_NAME=yolo-function \
  ghcr.io/scc-digitalhub/tvm-runtime-go:0.25
```

**3. Test it** from any computer of the same network, with `URL = "http://<device>:8080"` in `client.py`.

## Clean up

- Press **Ctrl+C** to close the port-forward and to stop the Docker containers.
- Stop the service on the platform when you no longer need it:

    ```sh
    dhcli stop <run-id> -p tvm-test
    ```

The Models stay in the project: a new `serve` run can deploy a compiled model again at any time, without building or compiling it.
