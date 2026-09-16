# Test the model

The service is reachable only from inside the platform. To test it from your computer, the CLI opens an authenticated **port-forward**: a local port that forwards every request to the service, through the platform proxy.

```
 your computer                                          platform
 curl / Python ──► localhost:18080 ──► dhcli port-forward ──► proxy ──► yolo-function service :8080
```

!!! note "REST only"

    The port-forward carries HTTP requests, so it can be used for the REST API only. The gRPC API (port `9000`) can be called from inside the platform, for example from a workspace.

## 1. Log in

If you are not logged in, or your session has expired (the CLI answers `401`), log in again:

```sh
dhcli login
```

Check that the service is running:

```sh
dhcli services -p tvm-test
```

## 2. Open the port-forward

In a **first terminal**, open the port-forward and keep it open during the test:

```sh
dhcli port-forward -p tvm-test -f yolo-function -l 18080
```

```
✔ Port-forward listening on localhost:18080
```

- `-f yolo-function` selects the most recent running service of the function. To select a specific run, pass its ID instead: `dhcli port-forward <run-id> -p tvm-test -l 18080`.
- `-l 18080` is the local port. Any free port works: use the same one in the next steps.

## 3. Check the service

In a **second terminal**:

```sh
curl http://localhost:18080/v2/health/ready
```

```json
{"ready":true}
```

Read the model signature:

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

## 4. Send a picture

Download a test picture:

```sh
curl -L -o bus.jpg https://ultralytics.com/images/bus.jpg
```

Save the following script as `client.py`. It reads the model signature, prepares the picture, calls the inference endpoint and prints the objects found.

```python
import json
import urllib.request

import numpy as np
from PIL import Image

URL = "http://localhost:18080"   # the port-forward
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

Run it:

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

Class `0` is *person* and class `5` is *bus* in the COCO dataset: the model found four people and the bus. The boxes are in the coordinates of the 640×640 input picture. The request takes a few seconds, because the picture travels as about 12 MB of JSON.

## 5. Use the ready-made test scripts

The `runtime-tvm` module of [digitalhub-core](https://github.com/scc-digitalhub/digitalhub-core) provides two complete test scripts in `runtimes/runtime-tvm/test_infer`, which also draw the results on the picture:

| Script | Model | Result |
| --- | --- | --- |
| `yolo.py` | YOLOv8 object detection, output `[1, 84, 8400]` | Boxes and class names drawn in `output/<function>.jpg` |
| `xinet.py` | YOLOv8-pose, people with 17 keypoints, output `[1, 56, N]` | Skeletons drawn in `output/<function>.jpg` |

With the port-forward open, point them to the local port with `--url`:

```sh
cd digitalhub-core/runtimes/runtime-tvm/test_infer
python3 yolo.py --url http://localhost:18080 --function yolo-function
```

Useful options:

| Option | Description |
| --- | --- |
| `--url` | Address that reaches the service, here the port-forward. |
| `--function` | Function of the service; also the model name, unless `--model` is set. |
| `--model` | Model name, when the run sets a `served_name` different from the function name. |
| `--image` | Local path or URL of the picture (default: `bus.jpg`). |
| `--conf` | Minimum confidence of the results. |
| `--stretch` | Stretch the picture to the model size instead of padding it (letterbox). |
| `--kp-conf` | `xinet.py` only: minimum visibility of the keypoints. |

For a pose model, the command is the same with `xinet.py` and the name of its function.

## 6. Clean up

- Press **Ctrl+C** in the first terminal to close the port-forward.
- Stop the service when you no longer need it:

    ```sh
    dhcli stop <run-id> -p tvm-test
    ```

The Models `yolo-function-ir` and `yolo-function-so` stay in the project: a new `serve` run can deploy the compiled model again at any time, without building or compiling it.
