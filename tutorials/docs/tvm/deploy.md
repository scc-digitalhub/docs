# Build, compile and serve the model

In this part we upload the model, create a TVM function and run its three actions. Wait for build and compile Runs to become **COMPLETED** before the next step.
A serve Run remains **RUNNING** while the service is available.

With the CLI, each run reads its fields from a small YAML file; the commands expect the files in the current folder.

In the console, the **Task** step contains common settings such as resources and the
run profile. The **Run** step contains the options for that execution: conversion flags,
compile target/optimization/tuning, or serve model/image/workers. TVM options are no
longer task settings; values stored in old tasks are not inherited by new runs.

## 1. Upload the model

=== "Console"

    Open **Models** and click `CREATE`. Choose the kind `onnx`, enter the name `yolo` and upload `yolov8n.onnx` at the bottom of the form.

=== "CLI"

    ```sh
    dhcli upload model -p tvm-test -n yolo -f yolov8n.onnx
    dhcli list models -p tvm-test
    ```

The runtime recognizes the format by itself: from the kind `onnx` of the Model, or from the `.onnx` extension of the file uploaded with the CLI (a Model of the generic kind `model`).

## 2. Create the function

=== "Console"

    Open **Functions**, click `CREATE`, choose the kind `tvm` and enter the name `yolo-function`. In the specification:

    | Field | Value |
    | --- | --- |
    | `model` | the key of the `yolo` Model, shown in its detail page, e.g. `store://tvm-test/model/onnx/yolo:<id>` |
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

    A key without `:<id>` refers to the latest version of the Model. `dhcli upload` creates a Model of kind `model`, hence `model/model` in the key.

    ```sh
    dhcli create function -p tvm-test -f yolo-function.yaml
    ```

## 3. Build: ONNX to Relax IR

`build` converts the model into Relax IR. YOLOv8n needs no conversion option: we only give the Job enough resources. If the imported outputs lack shapes, the build automatically retries with onnxsim; see [Outputs without a shape](../../../runtimes/tvm/#outputs-without-a-shape).

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

When the run is **COMPLETED**, the Model `yolo-function-ir`, of kind `tvm-ir`, contains the IR, and the function field `ir_model` points to it.

!!! note "Leave `target_opset` empty"

    Set `target_opset` only if the model really needs an opset conversion: ONNX cannot convert every operator to every version, and the build fails with `No Adapter From Version ...`. All the build options are described in the [runtime reference](../../../runtimes/tvm/#build-options).

## 4. Compile for the cluster (AMD64)

`compile` turns the IR into `model.so` for a target architecture. First we compile for AMD64 (Intel/AMD 64-bit), to serve the model on the cluster.

The model destination is not the compiler node: the toolkit can compile this AMD64
model on AMD64 or ARM64. Only `amd64_native` requires an AMD64 compile node.
The profile menu comes from CORE's `runtime-tvm.yaml`; administrators can add profiles
without changing the SDK. Advanced runs can instead set a standard LLVM `target`
object and compiler options, as described in the [target guide](../../../runtimes/tvm/#configurable-profiles).

=== "Console"

    Select the **compile** tab of the function and click `CREATE`. Set `resources` in the
    **Task** step, then `target_architecture`, `tag` and **Advanced compilation** in the **Run** step:

    | Field | Value | Why |
    | --- | --- | --- |
    | `target_architecture`{: style="white-space: nowrap" } | `amd64` | requires x86-64-v2 (`amd64_v3` requires x86-64-v3, including AVX2 and FMA) |
    | `tag` | `amd64` | names the Model `yolo-function-amd64` |
    | `optimization.opt_level` | `3` | TVM pass optimization level; separate from MetaSchedule tuning |
    | `resources` | CPU `4`, memory `8Gi` | compiling needs memory |

=== "CLI"

    Create `compile-amd64.yaml`:

    ```yaml
    spec:
      target_architecture: amd64
      tag: amd64
      optimization:
        opt_level: 3
      resources:
        cpu: "4"
        mem: 8Gi
    ```

    ```sh
    dhcli run tvm+compile -p tvm-test -n yolo-function -f compile-amd64.yaml
    dhcli list runs -p tvm-test
    ```

When the run is **COMPLETED**, the Model `yolo-function-amd64`, of kind `tvm-so`, contains `model.so` and `metadata.json`, and the function field `so_model` points to it. If the compile node can execute the target, `metadata.json` contains its synthetic
CPU benchmark. Otherwise `benchmark.skipped` explains why it was not run. These
are compile-node measurements, not timings on an ARM device or over HTTP.

## 5. Serve

`serve` deploys the model in `so_model` as an Open Inference v2 service, on port `8080` (REST) and `9000` (gRPC).

=== "Console"

    Select the **serve** tab of the function and click `CREATE`:

    | Field | Value | Why |
    | --- | --- | --- |
    | `resources` | CPU `4`, memory `2Gi` | starting point; one worker uses the same four threads as compilation |

=== "CLI"

    Create `serve.yaml`:

    ```yaml
    spec:
      resources:
        cpu: "4"
        mem: 2Gi
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

The model is served with the name of the function, `yolo-function`. The platform starts the service on a node with the architecture of the model, here an AMD64 node. The next part shows how to [test it](test.md).

## 6. Compile for ARM devices (optional)

The same IR can be compiled for ARM devices, such as a Raspberry Pi. The Job runs on a toolkit-capable AMD64 or ARM64 node, selected through `profile`.
The target architecture chooses the generated code; it does not move the Job to that device. Check the device first:

```sh
uname -m          # kernel: aarch64 or armv7l
getconf LONG_BIT  # userspace bitness; ARM32 also needs ARMv7, hard-float and NEON
```

=== "arm64 (64-bit OS)"

    **Console**: in the **compile** tab click `CREATE` and enter:

    | Field | Value |
    | --- | --- |
    | `target_architecture`{: style="white-space: nowrap" } | `arm64` (or `arm64_pi5` for a Raspberry Pi 5) |
    | `tag` | `arm64` |
    | `optimization.cross_cc` | leave empty: the right compiler is chosen automatically |
    | `optimization.opt_level` | `3` |
    | `resources` | CPU `4`, memory `8Gi` |

    **CLI**: create `compile-arm64.yaml` and start the run:

    ```yaml
    spec:
      target_architecture: arm64
      tag: arm64
      optimization:
        opt_level: 3
      resources:
        cpu: "4"
        mem: 8Gi
    ```

    ```sh
    dhcli run tvm+compile -p tvm-test -n yolo-function -f compile-arm64.yaml
    ```

    Result: the Model `yolo-function-arm64`.

=== "arm32 (ARMv7-compatible 32-bit OS)"

    **Console**: in the **compile** tab click `CREATE` and enter:

    | Field | Value |
    | --- | --- |
    | `target_architecture`{: style="white-space: nowrap" } | `arm32` |
    | `tag` | `arm32` |
    | `optimization.cross_cc` | leave empty: the right compiler is chosen automatically |
    | `optimization.opt_level` | `3` |
    | `resources` | CPU `4`, memory `8Gi` |

    **CLI**: create `compile-arm32.yaml` and start the run:

    ```yaml
    spec:
      target_architecture: arm32
      tag: arm32
      optimization:
        opt_level: 3
      resources:
        cpu: "4"
        mem: 8Gi
    ```

    ```sh
    dhcli run tvm+compile -p tvm-test -n yolo-function -f compile-arm32.yaml
    ```

    Result: the Model `yolo-function-arm32`.

    This model runs with the ARMv7 Go or Rust runtime image on a device with a compatible
    32-bit OS, hard-float ABI and NEON. Serving through CORE on an ARM32 cluster node also
    requires an ARMv7-compatible init image; the default init image is AMD64/ARM64 only.

!!! warning "Serving after an ARM compile"

    Each compile writes its Model into `so_model`, and `serve` deploys `so_model` by default. After an ARM compile, `so_model` points to the ARM library, which the platform serves only on ARM nodes: without ARM nodes in the cluster the service stays **PENDING**. To serve the AMD64 build, set the serve field `model_path` to `store://tvm-test/model/tvm-so/yolo-function-amd64:<id>`. A service that is already running is not affected.

The ARM64 and ARM32 Models can run on compatible devices, as shown in [Test the model](test.md#run-the-model-on-a-raspberry-pi). They can also be served by the platform on matching cluster nodes, provided the runtime and init images both support the node architecture.
