# TVM Runtime

The **TVM runtime** turns a trained model into fast native code with [Apache TVM](https://tvm.apache.org/) and serves it through the [Open Inference v2](https://github.com/kserve/open-inference-protocol) protocol, over both REST and gRPC.

It takes a model in **ONNX** or **TFLite** format, compiles it for a CPU target (x86 servers, 64-bit or 32-bit ARM devices) and deploys the result as a service, without writing any code or building any container image.

The runtime defines three actions, meant to be run one after the other:

| Action | What it does | Runs as | Result |
| --- | --- | --- | --- |
| `build` (`tvm+build`) | Converts the source model into TVM's intermediate representation (Relax IR) | Kubernetes Job | A Model with the Relax IR |
| `compile` (`tvm+compile`) | Compiles the Relax IR into a native library, `model.so`, for a target architecture | Kubernetes Job | A Model with `model.so` |
| `serve` (`tvm+serve`) | Deploys the compiled model behind an Open Inference v2 endpoint | Kubernetes Deployment and Service | An inference service |

## How it works

```
 source model          build                compile                    serve
 ONNX / TFLite  ───►  Relax IR Model  ───►  model.so Model  ───►  Open Inference v2 service
 (store:// or s3://)   (Job)                 (Job, per target)       REST :8080 · gRPC :9000
```

- **The function keeps track of the pipeline.** When `build` completes, the platform writes the key of the new Relax IR Model into the function field `ir_model`; when `compile` completes, it writes the key of the compiled Model into `so_model`. The next action reads that field, so the three actions can be run without copying any key by hand.
- **One build, many targets.** The Relax IR does not depend on the hardware: the same IR can be compiled several times, once per target architecture, each time producing a separate compiled Model.
- **Everything is a Model.** Both the IR and the compiled library are stored as Model entities in the platform storage, with their input and output signature, so they can be inspected, versioned and reused.
- **No image per model.** The serve action starts a generic serve image and downloads the compiled Model into it at startup. Two serve images are available, written in Go (default) and in Rust: see [Serving runtimes](#serving-runtimes).

---

## Function

A TVM function (kind `tvm`) describes the model to compile and serve.

| Field | Required | Description |
| --- | --- | --- |
| `model` | yes | The source model: the `store://` key of a Model, or an `s3://` or `https://` path. |
| `format` | no | `auto` (default), `onnx` or `tflite`. With `auto` the format is taken from the file extension (`.onnx`, `.tflite`). |
| `ir_model` | no | Key of the Relax IR Model. Written by the `build` action. |
| `so_model` | no | Key of the compiled Model. Written by the `compile` action. |

!!! note "When to set the format"

    The format can be detected only when the path of the model ends with `.onnx` or `.tflite`. If the Model points to a folder or to a file without extension, set `format` explicitly.

Example:

```yaml
kind: tvm
name: yolo-function
spec:
  model: store://my-project/model/model/yolo:35gbycneycd1fc0bmu3tnqqn
  format: auto
```

---

## Build action

The `build` action runs a Job that converts the source model into Relax IR and stores the result as a new Model named `<function>-ir`.

The conversion steps are:

=== "ONNX"

    1. Load the ONNX model.
    2. Optionally convert it to another operator set version (`target_opset`).
    3. Optionally simplify the graph with onnxsim (`simplify`).
    4. Run the ONNX shape inference.
    5. Convert the graph into Relax IR, with `float32` as default data type.
    6. Save the IR and its `metadata.json`, and publish the Model.

=== "TFLite"

    1. Load the TFLite model.
    2. Convert it into Relax IR. Full-integer quantized models are supported; dynamic-range quantized models are not.
    3. Save the IR and its `metadata.json`, and publish the Model.

### Build options

All options are optional. The conversion options apply to **ONNX** models only: the TFLite conversion ignores them.

| Option | Default | Description |
| --- | --- | --- |
| `simplify` | `false` | Simplify the graph with onnxsim before converting it. |
| `target_opset` | — | Convert the model to this ONNX operator set version first. Leave it empty unless the model needs it: the conversion fails when ONNX has no converter for one of the operators. |
| `opset_override` | model opset | Operator set version the TVM importer should assume, instead of the one declared by the model. |
| `strict_shape_inference` | `false` | Run the ONNX shape inference in strict mode. |
| `data_prop` | `false` | Propagate constant values during shape inference, to resolve more shapes. |
| `keep_params_in_input` | `false` | Keep the weights out of the graph, in a separate `params.bin` file. The `compile` action embeds them again. |
| `sanitize_input_names` | `true` | Rewrite the input names into valid identifiers. |
| `image` | toolkit image | Use another image for this run. |

### Build output

| File | Content |
| --- | --- |
| `model.relax.json` | The Relax IR, read by the `compile` action. |
| `model.relax.ir` | A readable text dump of the IR, for debugging. |
| `metadata.json` | Input and output tensors, source format and conversion settings. |
| `params.bin` | The weights, only with `keep_params_in_input: true`. |

---

## Compile action

The `compile` action runs a Job that compiles the Relax IR into `model.so` for the chosen target and stores the result as a new Model named `<function>-so` (or `<function>-<tag>`). The compiled Model is linked to the IR Model it comes from.

By default it compiles the IR in the function field `ir_model`; use `model_path` to compile another IR Model.

### Target architectures

| `target_architecture` | Runs on |
| --- | --- |
| `cpu` (default) | Generic code for the architecture of the node running the compile Job. |
| `x86` | Any x86-64 CPU with SSE4.2 (x86-64-v2). |
| `arm64` | 64-bit ARM devices (aarch64), such as a Raspberry Pi 4 or 5 with a 64-bit OS. |
| `armv7l` | 32-bit ARM devices with hardware floating point (armhf), such as a Raspberry Pi with a 32-bit OS. |

The ARM targets are cross-compiled: the Job links the library with the ARM compiler included in the toolkit image, so they can be compiled on an x86 cluster.

!!! note "Where a compiled model can run"

    A `model.so` runs only on the CPU architecture it was compiled for. To serve an ARM model in the platform, the cluster needs nodes of that architecture; otherwise, compile for `x86` or `cpu`.

### Compile options

All options are optional.

| Option | Default | Description |
| --- | --- | --- |
| `model_path` | function `ir_model` | `store://` key of the IR Model to compile. |
| `target_architecture` | `cpu` | Target architecture, see the table above. |
| `opt_level` | `3` | TVM optimization level, from 0 to 3. |
| `exec_mode` | `bytecode` | How the model graph is executed: `bytecode` (interpreted by the Relax virtual machine) or `compiled` (native code). |
| `relax_pipeline` | `default` | Name of the Relax optimization pipeline. |
| `tir_pipeline` | `default` | Name of the TIR optimization pipeline. |
| `cross_cc` | set by target | C++ cross compiler used to link `model.so`. It is set automatically for `arm64` and `armv7l`: set it only to use another compiler. |
| `system_lib` | `false` | Advanced: build a system-library module. Such a module cannot be loaded by the serve images. |
| `params_path` | `params.bin` of the IR | Path, inside the Job, of the weights file to embed. |
| `tag` | `so` | Suffix of the compiled Model name (`<function>-<tag>`), also saved in `metadata.json`. |
| `image` | toolkit image | Use another image for this run. |

### Compile output

| File | Content |
| --- | --- |
| `model.so` | The compiled model. |
| `metadata.json` | The IR metadata plus `target`, `opt_level`, `exec_mode`, `relax_pipeline`, `tir_pipeline` and `tag`. |

---

## Serve action

The `serve` action deploys the compiled Model as a service. An init container downloads `model.so` and `metadata.json` into the pod, and the serve image loads them and exposes the model over Open Inference v2:

- **REST** on port `8080`;
- **gRPC** on port `9000` (service `inference.GRPCInferenceService` of the [KServe v2 protocol](https://github.com/kserve/open-inference-protocol)).

By default it serves the compiled Model in the function field `so_model`; use `model_path` to serve another compiled Model.

### Serve options

All options are optional.

| Option | Default | Description |
| --- | --- | --- |
| `model_path` | function `so_model` | `store://` key of the compiled Model to serve. |
| `served_name` | function name | Name of the model in the API, as in `/v2/models/<served_name>`. Letters, digits, `.`, `_` and `-`. |
| `replicas` | `1` | Number of pods. |
| `workers` | `1` | Inference requests handled in parallel by each pod. Each worker loads its own copy of the model. |
| `service_type` | `ClusterIP` | Kubernetes Service type: `ClusterIP`, `NodePort` or `LoadBalancer`. |
| `service_name` | — | Extra Service name, `<function>-<service_name>`. |
| `image` | Go serve image | Use another serve image, for example the Rust one. |

Once the run is **RUNNING**, the service address is available in the `status.service` field of the run, for example `s-tvmserve-<run-id>.<namespace>:8080`. When the run serves the latest version of the function, the Service is also reachable as `<function>-latest`.

!!! info "How to access"

    Like every service of the platform, the endpoint is reachable only from inside the platform (workspaces, other functions, the console). To call it from your own computer, open a port-forward with the [CLI](../components/cli.md): `dhcli port-forward -p <project> -f <function> -l 8080`. The port-forward carries REST requests only.

### Endpoints

| What | REST | gRPC |
| --- | --- | --- |
| Server live | `GET /v2/health/live` | `ServerLive` |
| Server ready | `GET /v2/health/ready` | `ServerReady` |
| Server metadata | `GET /v2` | `ServerMetadata` |
| Model ready | `GET /v2/models/<name>/ready` | `ModelReady` |
| Model metadata | `GET /v2/models/<name>` | `ModelMetadata` |
| Inference | `POST /v2/models/<name>/infer` | `ModelInfer` |

Model metadata, as returned by `GET /v2/models/yolo-function`:

```json
{
  "name": "yolo-function",
  "versions": ["1"],
  "platform": "tvm",
  "inputs": [{ "name": "images", "datatype": "FP32", "shape": [1, 3, 640, 640] }],
  "outputs": [{ "name": "output0", "datatype": "FP32", "shape": [1, 84, 8400] }]
}
```

Inference request and response (values shortened):

```json
{
  "inputs": [
    { "name": "images", "datatype": "FP32", "shape": [1, 3, 640, 640], "data": [0.45, 0.47, ...] }
  ]
}
```

```json
{
  "model_name": "yolo-function",
  "outputs": [
    { "name": "output0", "datatype": "FP32", "shape": [1, 84, 8400], "data": [5.2, 11.8, ...] }
  ]
}
```

Rules for the requests:

- `data` holds the tensor values in row-major order, flat or nested.
- Inputs are matched by name when every input has a name and the names match the model; otherwise they are matched by position.
- Supported data types: `FP32`, `FP64`, `INT8`, `INT16`, `INT32`, `INT64`, `UINT8`, `UINT16`, `UINT32`, `UINT64`. `FP16` is not supported.

### Quantized models

When the model inputs or outputs are `int8` or `uint8` (a full-integer TFLite model or a QDQ ONNX model), the REST model metadata also returns the quantization parameters, so that a client can convert the values: `real = (quantized - zero_point) * scale`.

```json
{
  "name": "images",
  "datatype": "INT8",
  "shape": [1, 224, 224, 3],
  "parameters": { "scale": [0.003921568859368563], "zero_point": [-128] }
}
```

Per-axis quantization returns one value per channel, plus `quantized_dimension`. The gRPC metadata does not carry these parameters.

---

## Common run options

Every action accepts the standard Kubernetes options of the platform: `resources`, `envs`, `secrets`, `volumes` and `profile` (see [Kubernetes resources](../tasks/kubernetes-resources.md)). Suggested resources:

| Action | CPU | Memory | Notes |
| --- | --- | --- | --- |
| `build` | 2–4 | 4–8 Gi | Grows with the model size. |
| `compile` | 4 | 8 Gi | Compiling and linking need memory: with low limits the Job is killed (exit code 137). |
| `serve` | 1–4 | 1–2 Gi | Set `TVM_NUM_THREADS` to the requested CPUs, see [Serving runtimes](#serving-runtimes). |

`resources.disk` sets the size of the working volume of the Jobs (default `4Gi`).

---

## Serving runtimes

The `serve` action can use two serve images. They read the same model folder, expose the same endpoints on the same ports and accept the same requests, so they can be swapped with the `image` option without changing anything else.

| | Go (default) | Rust |
| --- | --- | --- |
| Image | `ghcr.io/scc-digitalhub/tvm-runtime-go:0.25` | `ghcr.io/scc-digitalhub/tvm-runtime-rust:0.25` |
| Source | [digitalhub-serverless](https://github.com/scc-digitalhub/digitalhub-serverless) | [digitalhub-tvm-rust](https://github.com/scc-digitalhub/digitalhub-tvm-rust) |
| Server | Nuclio processor with a native `tvm` runtime and the `openinference` trigger | Standalone `tvm-serve` server |
| How it calls TVM | Go, through cgo and the TVM C API | Rust, through the TVM C API |
| Parallel requests | One Nuclio worker per `workers`, each with its own model copy | One thread per `workers`, each with its own model copy |
| Maximum REST request | 512 MB | 1 GiB |
| Maximum gRPC message | 512 MB | 512 MB |
| Extra response field | — | `parameters.inference_time_ms` |
| Platforms | `linux/amd64`, `linux/arm64`, `linux/arm/v7` | `linux/amd64`, `linux/arm64`, `linux/arm/v7` |

Neither image contains Python: the model runs in-process on the TVM runtime libraries. The serve pod is configured with these environment variables:

| Variable | Default | Description |
| --- | --- | --- |
| `TVM_MODEL_DIR` | `/shared/model` | Folder with `model.so` and `metadata.json`. Set by the platform. |
| `TVM_MODEL_NAME` | `model` | Model name in the API. Set by the platform from `served_name`. |
| `TVM_SERVE_WORKERS` | `1` | Parallel workers. Set by the platform from `workers`. |
| `TVM_NUM_THREADS` | one per detected core | Threads TVM uses for each inference. Not set by the platform: add it to `envs`, for example `resources.cpu` divided by `workers`, so that the threads do not exceed the CPUs of the pod. |

!!! note "Use images of the same release"

    Compile and serve with images of the same release (for example `tvm-toolkit:0.25` and `tvm-runtime-go:0.25`): a `model.so` built with another TVM version may fail to load.

---

## Models produced

The `build` and `compile` actions publish their results as Models, named `<function>-ir` and `<function>-so`. Depending on the SDK version in the toolkit image, they are created with the TVM kinds `tvm-ir` and `tvm-so`, or with the generic kind `model`. In both cases the framework is `tvm`, the algorithm is `tvm-relax-ir` or `tvm-compiled-so`, and the specification contains the model signature:

| Field | Description |
| --- | --- |
| `entry` | Function of the model to call, usually `main`. |
| `inputs`, `outputs` | Tensors, each with `name`, `dtype` and `shape`; quantized tensors also have `scale`, `zero_point` and `quantized_dimension`. |
| `source_format`, `keep_params_in_input`, `sanitize_input_names` | How the IR was built (IR Model). |
| `target`, `opt_level`, `manifest` | How the library was compiled, and the full `metadata.json` (compiled Model). |

With the generic kind `model`, these fields are stored under `parameters`.

---

## Platform configuration

Administrators can change the images used by the runtime with these environment variables of the Core:

| Variable | Default | Description |
| --- | --- | --- |
| `RUNTIME_TVM_BUILDER_ONNX` | `ghcr.io/scc-digitalhub/tvm-toolkit:0.25` | Image of the `build` action for ONNX models. |
| `RUNTIME_TVM_BUILDER_TFLITE` | `ghcr.io/scc-digitalhub/tvm-toolkit:0.25` | Image of the `build` action for TFLite models. |
| `RUNTIME_TVM_COMPILER` | `ghcr.io/scc-digitalhub/tvm-toolkit:0.25` | Image of the `compile` action. |
| `RUNTIME_TVM_SERVE` | `ghcr.io/scc-digitalhub/tvm-runtime-go:0.25` | Image of the `serve` action. |
| `RUNTIME_TVM_HOME_DIR` | `/shared` | Working folder inside the pods. |
| `RUNTIME_TVM_VOLUME_SIZE` | `4Gi` | Default size of the working volume. |
| `RUNTIME_TVM_USER_ID`, `RUNTIME_TVM_GROUP_ID` | platform user and group | User and group the pods run as. |

The toolkit image ([digitalhub-tvm-toolkit](https://github.com/scc-digitalhub/digitalhub-tvm-toolkit)) contains Apache TVM with LLVM, the ARM cross compilers, the ONNX and TFLite importers and the platform SDK. The scripts executed by the Jobs are not part of the image: the Core adds them to each Job.

---

## Troubleshooting

| Problem | Cause and solution |
| --- | --- |
| The compile Job is killed (`OOMKilled`, exit code 137) | Not enough memory: set `resources` to at least `mem: 8Gi` and `cpu: "4"`. |
| Build error `No Adapter From Version <n> for <operator>` | `target_opset` asks for a conversion that ONNX cannot do. Remove `target_opset`, or choose a version supported by all the operators. |
| Build error `cannot detect the TVM source format` | The model path has no `.onnx` or `.tflite` extension: set `format` in the function. |
| `tvm+compile needs an IR model` | Run `build` first, or set `model_path` to an IR Model. |
| `tvm+serve needs a compiled .so model` | Run `compile` first, or set `model_path` to a compiled Model. |
| The serve pod restarts right after starting | The model was compiled for another architecture, with another TVM release, or as `system_lib`. Compile again for the node architecture, with images of the same release. |
| `404` on `/v2/models/<name>` | The name is not the `served_name` of the run (by default, the function name). |
| The endpoint cannot be reached from your computer | Services are internal to the platform: use `dhcli port-forward`, or call them from a workspace. |

---

## Management with SDK

Check the [SDK TVM runtime documentation](https://scc-digitalhub.github.io/sdk-docs/reference/runtimes/tvm/overview/) for more information.

## See Also

- [Tutorial: compile and serve an ONNX model with TVM](../../tutorials/tvm/intro/)
- [Serving Machine Learning Models](../ml-tasks/serving-ml-models.md)
- [Invoke, use, and expose services](../tasks/services.md)
- [CLI](../components/cli.md)
