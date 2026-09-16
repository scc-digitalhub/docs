# Compiled models with TVM: introduction

This scenario shows how to take a trained model, compile it into fast native code with the [TVM runtime](../../../runtimes/tvm/) and serve it through the Open Inference v2 protocol. The model is **YOLOv8n**, an object detector exported to ONNX.

The scenario has two parts:

1. [**Build, compile and serve**](deploy.md): upload the ONNX model, create a TVM function and run its three actions.
2. [**Test the model**](test.md): reach the service from your computer with a CLI port-forward and send it a picture.

```
 yolov8n.onnx ──► Model "yolo" ──► build ──► compile ──► serve ──► dhcli port-forward ──► your computer
                                   (IR)      (model.so)  (REST :8080)                     curl / Python
```

Every step can be done from the console or from the command line. The command-line version uses the platform [CLI](../../../components/cli/) (`dhcli`).

## Names used in this scenario

| What | Name |
| --- | --- |
| Project | `tvm-test` |
| Source Model | `yolo` |
| Function | `yolo-function` |
| Compiled Model | `yolo-function-so` (created by the platform) |

Use your own names if you prefer: the commands only need to be changed accordingly.

## Prerequisites

- Access to the platform, and a project you can work in. To create the project from the CLI: `dhcli create project -n tvm-test`.
- The [CLI](../../../components/cli/), version 0.15 or later (for the `port-forward` command), registered on your platform and logged in:

    ```sh
    dhcli register https://core.my-digitalhub-instance.it
    dhcli login
    ```

- Python 3 with `numpy` and `Pillow`, to test the model.
- The ONNX model. You can export YOLOv8n with the Ultralytics package:

    ```sh
    pip install ultralytics
    yolo export model=yolov8n.pt format=onnx
    ```

    This creates `yolov8n.onnx`, with input `images` `[1, 3, 640, 640]` and output `output0` `[1, 84, 8400]`.
