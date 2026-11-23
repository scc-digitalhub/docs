---
render_macros: true
---

# Create a TVM Function for Compilation

The compile action uses the same `tvm` Function as the [build action](../tvm-build/create.md).
Create it with the source model and normally leave `ir_model` empty for Build to fill.
Compile reads that IR, or the IR selected by its Run's `ir_model_path`. Its compiled
Model key belongs to the Compile Run, not the Function.

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
