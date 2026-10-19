---
render_macros: true
---

# Use a ServiceGraph Run

ServiceGraph runs remotely. Refresh the Run and inspect its status until the service is ready. The service URL is available in `run.status.service`.

```python
run.refresh()
run.status

response = run.invoke(json={"inputs": [[...]]})
```

For synchronous pipelines with an HTTP source, `invoke()` uses the Run's service URL by default. An explicit `url` must start with the service URL. For streaming pipelines, connect a source such as RTSP or MJPEG and observe a configured output; expose additional ports when direct access to pipeline inputs or outputs is needed.

{{ page_navigation(("Run", "run.md"), ("Action", "action.md")) }}
