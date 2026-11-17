---
render_macros: true
---

# Use a TVM Compile Run

Compilation publishes a Model containing `model.so` and `metadata.json`.
Read its key from the Compile Run's `status.outputs.compiled_so` and pass it to
the Serve Run. The Function keeps the IR reference, so different targets can use
the same IR without replacing each other's compiled Model selection.

```python
compile_run = function.run(
    action="compile",
    target_architecture="auto",
    wait=True,
)

serve_run = function.run(
    action="serve",
    model_path=compile_run.status.to_dict()["outputs"]["compiled_so"],
    served_name="my-model",
    wait=True,
)
```

To serve another compiled Model, use its versioned key in `model_path`, for example
`store://my-project/model/tvm-so/model-so:version`. A new Compile does not change
an existing Serve Run.

{{ page_navigation(("Run", "run.md"), ("Action", "action.md")) }}
