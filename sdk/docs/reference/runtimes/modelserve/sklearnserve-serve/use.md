---
render_macros: true
---

# Use a Scikit-learn Serving Run

The service is executed remotely. Call `run.refresh()` and inspect `run.status` to check its progress. When ready, the status includes the service details.

By default, `invoke()` sends requests to the MLServer V2 inference endpoint at `http://<service_url>/v2/models/{model_name}/infer`. The default model name is `"model"`; pass `model_name` if the endpoint uses a different name. You can also pass an explicit `url`, which must start with the service URL.

```python
run.refresh()
run.status

response = run.invoke(
    model_name="my-model",
    json={"inputs": [...]}
)
```

{{ member_doc("invoke", "digitalhub_runtime_modelserve.entities.run.sklearnserve_run.entity.RunSklearnserveRun") }}

{{ page_navigation(("Run", "run.md"), ("Action", "action.md")) }}
