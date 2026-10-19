---
render_macros: true
---

# Use a TVM Compile Run

Compilation produces a `model.so` artifact. Configure its store key with `so_model` or pass the key as `model_path` to the serve action.

```python
so_model = "store://my-project/model/model-so:version"

compile_run = function.run(
    action="compile",
    model_path="store://my-project/model/model-relax:version",
    so_model=so_model,
    target_architecture="auto",
    wait=True,
)

serve_run = function.run(
    action="serve",
    model_path=so_model,
    served_name="my-model",
)
```

{{ page_navigation(("Run", "run.md"), ("Action", "action.md")) }}
