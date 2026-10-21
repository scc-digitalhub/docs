---
render_macros: true
---

# Use a TVM Build Run

The build produces a Relax IR model and CORE updates the Function's `ir_model`
reference. The next compile uses that reference automatically.

```python
build_run = function.run(
    action="build",
    wait=True,
)

compile_run = function.run(
    action="compile",
    target_architecture="auto",
    wait=True,
)
```

To compile a different existing IR, set the compile Run's `model_path`, for example
`store://my-project/model/tvm-ir/model-ir:version`.

{{ page_navigation(("Run", "run.md"), ("Action", "action.md")) }}
