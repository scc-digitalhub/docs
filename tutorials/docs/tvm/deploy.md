# Build, compile and serve the model

In this part we upload the model, create a TVM function and run its three actions. Each action is a **run**: wait until a run is **COMPLETED** before starting the next one.

With the CLI, each run reads its fields from a small YAML file; the commands expect the files in the current folder.

## 1. Upload the model

=== "Console"

    Open **Models** and click `CREATE`. Choose the kind `model`, enter the name `yolo` and upload `yolov8n.onnx` at the bottom of the form.

=== "CLI"

    ```sh
    dhcli upload model -p tvm-test -n yolo -f yolov8n.onnx
    dhcli list models -p tvm-test
    ```

The Model path ends with `.onnx`, so the runtime recognizes the format by itself.

## 2. Create the function

=== "Console"

    Open **Functions**, click `CREATE`, choose the kind `tvm` and enter the name `yolo-function`. In the specification:

    | Field | Value |
    | --- | --- |
    | `model` | the key of the `yolo` Model, shown in its detail page, e.g. `store://tvm-test/model/model/yolo:<id>` |
    | `format` | `auto` |

=== "CLI"

    Create `yolo-function.yaml`:

    ```yaml
    kind: tvm
    name: yolo-function
    spec:
      model: store://tvm-test/model/model/yolo
      format: auto
    ```

    A key without `:<id>` refers to the latest version of the Model.

    ```sh
    dhcli create function -p tvm-test -f yolo-function.yaml
    ```

## 3. Build: ONNX to Relax IR

`build` converts the model into Relax IR. YOLOv8n needs no conversion option: we only give the Job enough resources.

=== "Console"

    Open the function, select the **build** tab and click `CREATE`. In the first step:

    | Field | Value |
    | --- | --- |
    | `resources` | CPU `4`, memory `8Gi` |

    Leave the other fields empty and complete the form.

=== "CLI"

    Create `build.yaml`:

    ```yaml
    spec:
      resources:
        cpu: "4"
        mem: 8Gi
    ```

    ```sh
    dhcli run tvm+build -p tvm-test -n yolo-function -f build.yaml
    dhcli list runs -p tvm-test
    dhcli log <run-id> -p tvm-test
    ```

When the run is **COMPLETED**, the Model `yolo-function-ir` contains the IR, and the function field `ir_model` points to it.

!!! note "Leave `target_opset` empty"

    Set `target_opset` only if the model really needs an opset conversion: ONNX cannot convert every operator to every version, and the build fails with `No Adapter From Version ...`. All the build options are described in the [runtime reference](../../../runtimes/tvm/#build-options).

## 4. Compile for the cluster (x86)

`compile` turns the IR into `model.so` for a target architecture. First we compile for x86, to serve the model on the cluster.

=== "Console"

    Select the **compile** tab of the function and click `CREATE`:

    | Field | Value | Why |
    | --- | --- | --- |
    | `target_architecture`{: style="white-space: nowrap" } | `x86` | runs on any x86-64 node |
    | `tag` | `x86` | names the Model `yolo-function-x86` |
    | `opt_level` | `3` | full optimization |
    | `resources` | CPU `4`, memory `8Gi` | compiling needs memory |

=== "CLI"

    Create `compile-x86.yaml`:

    ```yaml
    spec:
      target_architecture: x86
      tag: x86
      opt_level: 3
      resources:
        cpu: "4"
        mem: 8Gi
    ```

    ```sh
    dhcli run tvm+compile -p tvm-test -n yolo-function -f compile-x86.yaml
    dhcli list runs -p tvm-test
    ```

When the run is **COMPLETED**, the Model `yolo-function-x86` contains `model.so` and `metadata.json`, and the function field `so_model` points to it.

## 5. Serve

`serve` deploys the model in `so_model` as an Open Inference v2 service, on port `8080` (REST) and `9000` (gRPC).

=== "Console"

    Select the **serve** tab of the function and click `CREATE`:

    | Field | Value | Why |
    | --- | --- | --- |
    | `resources` | CPU `2`, memory `2Gi` | enough for YOLOv8n |
    | `envs` | `TVM_NUM_THREADS` = `2` | as many TVM threads as CPUs |

=== "CLI"

    Create `serve.yaml`:

    ```yaml
    spec:
      resources:
        cpu: "2"
        mem: 2Gi
      envs:
        - name: TVM_NUM_THREADS
          value: "2"
    ```

    ```sh
    dhcli run tvm+serve -p tvm-test -n yolo-function -f serve.yaml
    dhcli services -p tvm-test
    ```

When the service is **RUNNING**, `dhcli services` shows it:

```
NAME          ID                                 FUNCTION        KIND            SERVICE                                                         STATE
cloudy-lynx   7398740f73b14fdd957f10c2e54c8ed2   yolo-function   tvm+serve:run   s-tvmserve-7398740f73b14fdd957f10c2e54c8ed2.dev-platform:8080   RUNNING
```

The model is served with the name of the function, `yolo-function`. The next part shows how to [test it](test.md).

## 6. Compile for ARM devices (optional)

The same IR can be compiled for ARM devices, such as a Raspberry Pi. The Job still runs on the cluster: the ARM library is cross-compiled. Check the device first:

```sh
uname -m     # aarch64 -> use arm64 · armv7l -> use armv7l
```

=== "arm64 (64-bit OS)"

    **Console**: in the **compile** tab click `CREATE` and enter:

    | Field | Value |
    | --- | --- |
    | `target_architecture`{: style="white-space: nowrap" } | `arm64` |
    | `tag` | `arm64` |
    | `cross_cc` | leave empty: the right compiler is chosen automatically |
    | `opt_level` | `3` |
    | `resources` | CPU `4`, memory `8Gi` |

    **CLI**: create `compile-arm64.yaml` and start the run:

    ```yaml
    spec:
      target_architecture: arm64
      tag: arm64
      opt_level: 3
      resources:
        cpu: "4"
        mem: 8Gi
    ```

    ```sh
    dhcli run tvm+compile -p tvm-test -n yolo-function -f compile-arm64.yaml
    ```

    Result: the Model `yolo-function-arm64`.

=== "armv7l (32-bit OS)"

    **Console**: in the **compile** tab click `CREATE` and enter:

    | Field | Value |
    | --- | --- |
    | `target_architecture`{: style="white-space: nowrap" } | `armv7l` |
    | `tag` | `armv7l` |
    | `cross_cc` | leave empty: the right compiler is chosen automatically |
    | `opt_level` | `3` |
    | `resources` | CPU `4`, memory `8Gi` |

    **CLI**: create `compile-armv7l.yaml` and start the run:

    ```yaml
    spec:
      target_architecture: armv7l
      tag: armv7l
      opt_level: 3
      resources:
        cpu: "4"
        mem: 8Gi
    ```

    ```sh
    dhcli run tvm+compile -p tvm-test -n yolo-function -f compile-armv7l.yaml
    ```

    Result: the Model `yolo-function-armv7l`.

!!! warning "Serving after an ARM compile"

    Each compile writes its Model into `so_model`, and `serve` deploys `so_model` by default. After an ARM compile, `so_model` points to the ARM library, which does not run on the cluster: to start a new service, set the serve field `model_path` to `store://tvm-test/model/model/yolo-function-x86`. A service that is already running is not affected.

The ARM Models are run on the device, as shown in [Test the model](test.md#run-the-model-on-a-raspberry-pi).
