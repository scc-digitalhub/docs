---
render_macros: true
---

# Create a TVM Function for Compilation

The compile action uses the same `tvm` Function specification as the [build action](../tvm-build/create.md). Create the Function with its source model and generated `ir_model` and `so_model` references. Normally leave these empty and let
build/compile update them; an existing versioned reference can be supplied explicitly.

```python
import digitalhub as dh

function = dh.new_function(
    project="my-project",
    name="my-tvm-model",
    kind="tvm",
    model="s3://my-bucket/models/model.onnx",
    format="onnx",
)
```

{{ page_navigation(("Action", "action.md"), ("Run", "run.md")) }}
