---
render_macros: true
---

# Use a TVM Build Run

The build produces a Relax IR model. Store its key in the Function's `ir_model` field or pass it as `model_path` to the compile action.

```python
ir_model = "store://my-project/model/model-relax:version"

build_run = function.run(
    action="build",
    ir_model=ir_model,
    wait=True,
)

compile_run = function.run(
    action="compile",
    model_path=ir_model,
    target_architecture="auto",
)
```

{{ page_navigation(("Run", "run.md"), ("Action", "action.md")) }}
