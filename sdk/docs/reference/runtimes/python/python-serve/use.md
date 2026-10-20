---
render_macros: true
---

# Use a Python Service Run

Invoke the deployed endpoint with `run.invoke()`. The method returns a `requests.Response`; the service URL is available from `run.status.service["url"]`.

```python
response = run.invoke(json={"some-function-parameter": value})
service_url = run.status.service["url"]
```

{{ member_doc("invoke", "digitalhub_runtime_python.entities.run.python_serve.entity.RunPythonRunServe") }}
{{ member_doc("output", "digitalhub_runtime_python.entities.run._base.entity.RunBaseRun") }}
{{ member_doc("outputs", "digitalhub_runtime_python.entities.run._base.entity.RunBaseRun") }}
{{ member_doc("result", "digitalhub_runtime_python.entities.run._base.entity.RunBaseRun") }}
{{ member_doc("results", "digitalhub_runtime_python.entities.run._base.entity.RunBaseRun") }}

{{ page_navigation(("Run", "run.md"), ("Action", "action.md")) }}
