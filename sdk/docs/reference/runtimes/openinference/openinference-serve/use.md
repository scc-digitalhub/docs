---
render_macros: true
---

# Use an OpenInference Service

Invoke the deployed endpoint with a request body that matches the function's input tensor schema.

```python
payload = {
    "inputs": [
        {
            "name": "input-0",
            "shape": [-1],
            "datatype": "BYTES",
            "data": ["hello world"],
        }
    ]
}
response = run.invoke(json=payload)
```

The response follows the output tensor schema declared by the function.

{{ member_doc("invoke", "digitalhub_runtime_python.entities.run.python_serve.entity.RunPythonRunServe") }}
{{ member_doc("output", "digitalhub_runtime_python.entities.run._base.entity.RunBaseRun") }}
{{ member_doc("outputs", "digitalhub_runtime_python.entities.run._base.entity.RunBaseRun") }}
{{ member_doc("result", "digitalhub_runtime_python.entities.run._base.entity.RunBaseRun") }}
{{ member_doc("results", "digitalhub_runtime_python.entities.run._base.entity.RunBaseRun") }}

{{ page_navigation(("Run", "run.md"), ("Action", "action.md")) }}
