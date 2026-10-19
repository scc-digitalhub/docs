---
render_macros: true
---

# Use a vLLM Speech Run

The service is executed remotely. Call `run.refresh()` and inspect `run.status` to check its progress. When ready, the status includes the service details. Use `list_endpoints()` to inspect the model's available endpoints, then call `invoke()` to send a request.

```python
run.refresh()
run.status

endpoints = run.list_endpoints()
response = run.invoke(json={"inputs": [...]})
```

{{ member_doc("invoke", "digitalhub_runtime_modelserve.entities.run.vllmservespeech_run.entity.RunVllmservespeechRun") }}
{{ member_doc("list_endpoints", "digitalhub_runtime_modelserve.entities.run.vllmservespeech_run.entity.RunVllmservespeechRun") }}

{{ page_navigation(("Run", "run.md"), ("Action", "action.md")) }}
