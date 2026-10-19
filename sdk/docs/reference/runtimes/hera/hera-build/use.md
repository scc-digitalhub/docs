---
render_macros: true
---

# Use a Hera Build Run

The build run returns the generated Argo Workflows YAML, encoded as base64, under the `workflow` result.

```python
workflow_yaml_base64 = run.result("workflow")
```

{{ member_doc("result", "digitalhub_runtime_hera.entities.run._base.entity.RunHeraRun") }}
{{ member_doc("results", "digitalhub_runtime_hera.entities.run._base.entity.RunHeraRun") }}

{{ page_navigation(("Run", "run.md"), ("Action", "action.md")) }}
