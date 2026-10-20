---
render_macros: true
---

# Use a Python Job Run

Use `output(s)` to access entity outputs and `result(s)` to access primitive results returned by the handler.

```python
entity_output = run.output("output-name")
all_outputs = run.outputs()
primitive_result = run.result("result-name")
all_results = run.results()
```

{{ member_doc("output", "digitalhub_runtime_python.entities.run._base.entity.RunBaseRun") }}
{{ member_doc("outputs", "digitalhub_runtime_python.entities.run._base.entity.RunBaseRun") }}
{{ member_doc("result", "digitalhub_runtime_python.entities.run._base.entity.RunBaseRun") }}
{{ member_doc("results", "digitalhub_runtime_python.entities.run._base.entity.RunBaseRun") }}

{{ page_navigation(("Run", "run.md"), ("Action", "action.md")) }}
