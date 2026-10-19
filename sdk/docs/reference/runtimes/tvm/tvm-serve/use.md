---
render_macros: true
---

# Use a TVM Serving Run

Refresh the Run and inspect its status until the service is ready.

```python
run.refresh()
run.status
```

The service endpoint is available in `run.status.service`.

{{ page_navigation(("Run", "run.md"), ("Action", "action.md")) }}
