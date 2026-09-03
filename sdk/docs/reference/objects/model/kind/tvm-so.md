# TVM SO

The `tvm-so` kind stores a compiled shared-object model produced by `tvm+compile`.

## TVM SO spec

The `tvm-so` kind has the following specification parameters.

| Parameter | Type | Description | Default |
| --- | --- | --- | --- |
| [`path`](../../../configuration/paths/overview.md#entity-paths) | *str* | Path of the model, either on the local filesystem or in remote storage. | *required* |
| `framework` | *str \| None* | Model framework, for example `tvm`. | `None` |
| `algorithm` | *str \| None* | Model algorithm. | `None` |
| `parameters` | *dict \| None* | Model parameters. | `None` |
| `entry` | *str \| None* | Model entry function. | `None` |
| `inputs` | *list[TensorSpec] \| None* | Input tensor signatures. | `None` |
| `outputs` | *list[TensorSpec] \| None* | Output tensor signatures. | `None` |
| `target` | *str \| None* | TVM hardware target used to compile the shared object. | `None` |
| `opt_level` | *int \| None* | TVM optimization level used during compilation, from 0 to 3. | `None` |
| `manifest` | *dict \| None* | Parsed `manifest.json` produced by the compile job. | `None` |

### TensorSpec

| Parameter | Type | Description | Default |
| --- | --- | --- | --- |
| `name` | *str \| None* | Tensor name. | `None` |
| `dtype` | *str \| None* | Tensor data type, for example `float32`. | `None` |
| `shape` | *list[int] \| None* | Tensor shape; `-1` marks a symbolic dimension. | `None` |

## TVM SO methods

The `tvm-so` kind has no additional methods.
