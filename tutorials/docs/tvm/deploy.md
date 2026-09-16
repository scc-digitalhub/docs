# Build, compile and serve the model

In this part we upload the ONNX model, create a TVM function and run its three actions: `build`, `compile` and `serve`. Each action is a run; wait for a run to be **COMPLETED** before starting the next one.

With the CLI, keep the specification of each run in a small YAML file: the commands below expect them in the current folder.

## 1. Upload the model

=== "Console"

    Open **Models** and click `CREATE`. Choose the kind `model`, set the name `yolo` and upload `yolov8n.onnx` at the bottom of the form.

=== "CLI"

    ```sh
    dhcli upload model -p tvm-test -n yolo -f yolov8n.onnx
    dhcli list models -p tvm-test
    ```

The Model now points to a file ending with `.onnx`, so the TVM runtime will recognize the format by itself.

## 2. Create the function

The function tells the runtime which model to compile.

=== "Console"

    Open **Functions**, click `CREATE`, choose the kind `tvm` and set the name `yolo-function`. In the specification set:

    - **`model`**: the key of the `yolo` Model, shown in its detail page (for example `store://tvm-test/model/model/yolo:<id>`);
    - **`format`**: `auto`.

=== "CLI"

    Create `yolo-function.yaml`:

    ```yaml
    kind: tvm
    name: yolo-function
    spec:
      model: store://tvm-test/model/model/yolo
      format: auto
    ```

    A key without `:<id>` refers to the latest version of the Model. Create the function:

    ```sh
    dhcli create function -p tvm-test -f yolo-function.yaml
    ```

## 3. Build: ONNX to Relax IR

The `build` action converts the ONNX model into Relax IR, the intermediate representation of TVM. No option is needed for YOLOv8n; we only give the Job enough resources.

=== "Console"

    Open the function, select the `build` tab and click `CREATE`. In the first step set the resources to 4 CPUs and 8Gi of memory, then complete the form.

=== "CLI"

    Create `build.yaml`:

    ```yaml
    spec:
      resources:
        cpu: "4"
        mem: 8Gi
    ```

    Start the run and follow it:

    ```sh
    dhcli run tvm+build -p tvm-test -n yolo-function -f build.yaml
    dhcli list runs -p tvm-test
    dhcli log <run-id> -p tvm-test
    ```

When the run is **COMPLETED**:

- a new Model `yolo-function-ir` contains the IR (`model.relax.json`) and its `metadata.json`;
- the function field `ir_model` points to it, so the next action finds it automatically.

!!! note "Leave `target_opset` empty"

    The build options (`simplify`, `target_opset`, ...) are described in the [runtime reference](../../../runtimes/tvm/#build-options). Set `target_opset` only when you really need an opset conversion: ONNX cannot convert every operator to every version, and the build fails with `No Adapter From Version ...`.

## 4. Compile: Relax IR to model.so

The `compile` action turns the IR into a native library for a target architecture. We compile for any x86-64 CPU.

=== "Console"

    Select the `compile` tab of the function and click `CREATE`. Set **`target_architecture`** to `x86`, **`opt_level`** to `3`, and the resources to 4 CPUs and 8Gi of memory.

=== "CLI"

    Create `compile.yaml`:

    ```yaml
    spec:
      target_architecture: x86
      opt_level: 3
      resources:
        cpu: "4"
        mem: 8Gi
    ```

    ```sh
    dhcli run tvm+compile -p tvm-test -n yolo-function -f compile.yaml
    dhcli list runs -p tvm-test
    ```

When the run is **COMPLETED**, the new Model `yolo-function-so` contains `model.so` and `metadata.json`, and the function field `so_model` points to it.

!!! info "Other targets"

    The same IR can be compiled again for `arm64` or `armv7l`, to run the model on ARM devices such as a Raspberry Pi: see the [target architectures](../../../runtimes/tvm/#target-architectures).

## 5. Serve: deploy the model

The `serve` action deploys `model.so` as an Open Inference v2 service, on port `8080` (REST) and `9000` (gRPC).

=== "Console"

    Select the `serve` tab of the function and click `CREATE`. Set the resources to 2 CPUs and 2Gi of memory, and add the environment variable `TVM_NUM_THREADS` with value `2`.

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

`TVM_NUM_THREADS` makes TVM use as many threads as the CPUs of the pod. When the service is **RUNNING**, `dhcli services` shows its address:

```
NAME          ID                                 FUNCTION        KIND            SERVICE                                                         STATE
cloudy-lynx   7398740f73b14fdd957f10c2e54c8ed2   yolo-function   tvm+serve:run   s-tvmserve-7398740f73b14fdd957f10c2e54c8ed2.dev-platform:8080   RUNNING
```

The model is served with the name of the function, `yolo-function`. The address is internal to the platform: in the [next part](test.md) we reach it from our computer.
