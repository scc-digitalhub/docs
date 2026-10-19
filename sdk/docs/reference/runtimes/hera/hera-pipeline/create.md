---
render_macros: true
---

# Create a Hera Workflow

Define a Workflow with a Python source and a handler that returns a Hera `Workflow`. The handler takes no arguments; declare workflow parameters inside the Hera object.

## Parameters

| Name | Type | Description |
| --- | --- | --- |
| project | str | Project name. Required only when creating from the library; otherwise **MUST NOT** be set. |
| name | str | Name that identifies the object. **Required.** |
| kind | str | Workflow kind. Must be `hera`. **Required.** |
| uuid | str | Object ID in UUID4 format. |
| description | str | Description of the object. |
| labels | list[str] | List of labels. |
| embedded | bool | Whether to embed the object in the project. |
| [code_src](../../../configuration/code-sources.md#code-source-uri) | str | URI pointing to the source code. |
| [code](../../../configuration/code-sources.md#plain-text-source) | str | Source code provided as plain text. |
| base64 | str | Source code encoded as base64. |
| [handler](../../../configuration/code-sources.md#handler) | str | Function entrypoint. **Required.** It must return a Hera `Workflow` and accept no arguments. |
| lang | str | Source code language. Only `python` is supported; defaults to `python`. |

See the [pipeline definition guide](../define-pipeline.md) for the function structure and DSL helpers.

## Example

```python
workflow = dh.new_workflow(
    name="my-workflow",
    kind="hera",
    code_src="pipeline.py",
    handler="pipeline",
)
```

{{ member_doc("build", "digitalhub_runtime_hera.entities.workflow.hera.entity.WorkflowHera") }}

{{ page_navigation(("Action", "action.md"), ("Run", "run.md")) }}
