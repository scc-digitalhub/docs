---
render_macros: true
---

# Use a Guardrail Service

Check the service URL and run status through the returned `Run` entity. Guardrail request/response processing follows Envoy ExtProc; refer to the [handler guide](../../define-function.md#guardrail) for processing phases and response behavior.

```python
service_url = run.status.service["url"]
```

{{ member_doc("output", "digitalhub_runtime_python.entities.run._base.entity.RunBaseRun") }}
{{ member_doc("outputs", "digitalhub_runtime_python.entities.run._base.entity.RunBaseRun") }}
{{ member_doc("result", "digitalhub_runtime_python.entities.run._base.entity.RunBaseRun") }}
{{ member_doc("results", "digitalhub_runtime_python.entities.run._base.entity.RunBaseRun") }}

{{ page_navigation(("Run", "run.md"), ("Action", "action.md")) }}
