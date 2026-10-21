---
render_macros: true
---

# Use a TVM Compile Run

Compilation produces a `model.so` artifact and CORE updates `function.so_model`.
The next serve uses that reference automatically.

```python
compile_run = function.run(
    action="compile",
    target_architecture="auto",
    wait=True,
)

serve_run = function.run(
    action="serve",
    served_name="my-model",
    wait=True,
)
```

To serve a different compiled model, set the serve Run's `model_path`, for example
`store://my-project/model/tvm-so/model-so:version`.

{{ page_navigation(("Run", "run.md"), ("Action", "action.md")) }}
