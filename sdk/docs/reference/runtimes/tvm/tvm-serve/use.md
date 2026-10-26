---
render_macros: true
---

# Use a TVM Serving Run

Refresh the Run and inspect its status until the service is ready.

```python
run.refresh()
run.status
```

`run.status.service` describes the Kubernetes service. `run.status.inference_v2`
contains `model`, `baseUrl`, `inferenceUrl`, `modelMetadataUrl`, `modelReadinessUrl`,
`readinessUrl` and `livenessUrl`. The model name is `served_name`, otherwise the
Function name. Read metadata before constructing an inference tensor.

The default service URL is internal to Kubernetes. Use `dhcli port-forward` to
call REST from your computer; a browser cannot resolve a cluster-only hostname
by itself. See the [inference tutorial](https://scc-digitalhub.github.io/docs/0.16/tutorials/tvm/test/).

{{ page_navigation(("Run", "run.md"), ("Action", "action.md")) }}
