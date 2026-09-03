# TVM IR

The `tvm-ir` kind stores a Relax IR model produced by `tvm` and `tvm+build`.

## TVM IR spec

The `tvm-ir` kind has the following specification parameters.

| Parameter | Type | Description | Default |
| --- | --- | --- | --- |
| [`path`](../../../configuration/paths/overview.md#entity-paths) | *str* | Path of the model, either on the local filesystem or in remote storage. | *required* |
| `framework` | *str \| None* | Model framework, for example `tvm`. | `None` |
| `algorithm` | *str \| None* | Model algorithm. | `None` |
| `parameters` | *dict \| None* | Model parameters. | `None` |
| `entry` | *str \| None* | Relax entry function, for example `main`. | `None` |
| `inputs` | *list[TensorSpec] \| None* | Input tensor signatures. | `None` |
| `outputs` | *list[TensorSpec] \| None* | Output tensor signatures. | `None` |
| `source_format` | *str \| None* | Source format: `auto`, `onnx`, `pytorch`, or `tvmscript`. | `None` |
| `keep_params_in_input` | *bool \| None* | Keep weights as input variables in `params.bin` instead of folding them into the IR. | `None` |
| `sanitize_input_names` | *bool \| None* | Sanitize input names in the ONNX frontend. | `None` |

### TensorSpec

| Parameter | Type | Description | Default |
| --- | --- | --- | --- |
| `name` | *str \| None* | Tensor name. | `None` |
| `dtype` | *str \| None* | Tensor data type, for example `float32`. | `None` |
| `shape` | *list[int] \| None* | Tensor shape; `-1` marks a symbolic dimension. | `None` |

## TVM IR methods

The `tvm-ir` kind has no additional methods.
