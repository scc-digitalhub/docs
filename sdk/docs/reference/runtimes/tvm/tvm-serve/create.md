---
render_macros: true
---

# Create a TVM Function for Serving

The serve action uses the same `tvm` Function as the [build action](../tvm-build/create.md).
The Function holds the source model and the IR reference produced by Build.
After Compile completes, pass its `status.outputs.compiled_so` key in the Serve
Run's required `model_path`. The compiled Model is not stored on the Function.

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
