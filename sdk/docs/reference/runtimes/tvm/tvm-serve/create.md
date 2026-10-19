---
render_macros: true
---

# Create a TVM Function for Serving

The serve action uses the same `tvm` Function specification as the [build action](../tvm-build/create.md). Create the Function with its source model and optional `ir_model` and `so_model` store keys.

```python
function = dh.new_function(
    name="my-tvm-model",
    kind="tvm",
    model="s3://my-bucket/models/model.onnx",
    format="onnx",
)
```

{{ page_navigation(("Action", "action.md"), ("Run", "run.md")) }}
