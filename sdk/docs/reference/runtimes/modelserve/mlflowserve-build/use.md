---
render_macros: true
---

# Use an MLflow Build Run

After the build completes, retrieve the image produced by the run and use it to deploy the model.

```python
image = build_run.image
```

{{ member_doc("image", "digitalhub_runtime_modelserve.entities.run.mlflowserve_build_run.entity.RunMlflowserveBuildRun") }}

{{ page_navigation(("Run", "run.md"), ("Action", "action.md")) }}
