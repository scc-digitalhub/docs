---
render_macros: true
---

# Create a ServiceGraph Function

Define a `servicegraph` Function with a YAML pipeline specification.

## Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| project | str | (✓) | Project name. Required only when creating from the library; otherwise **MUST NOT** be set. |
| name | str | ✓ | Name that identifies the object. |
| kind | str | ✓ | Function kind. Must be `servicegraph`. |
| uuid | str | | Object ID in UUID4 format. |
| description | str | | Description of the object. |
| labels | list[str] | | List of labels. |
| embedded | bool | | Whether to embed the object in the project. |
| [code_src](../../../configuration/code-sources.md#code-source-uri) | str | | URI pointing to the YAML pipeline definition. |
| [code](../../../configuration/code-sources.md#plain-text-source) | str | | Pipeline YAML provided as plain text. |
| base64 | str | | Pipeline definition encoded as base64. |
| image | str | | Docker image used to serve the pipeline. |

The pipeline must follow the specification in the [ServiceGraph project](https://github.com/scc-digitalhub/digitalhub-servicegraph).

## Example

```python
function = dh.new_function(
    name="my-servicegraph-service",
    kind="servicegraph",
    code_src="src/flow.yaml",
)
```

{{ page_navigation(("Action", "action.md"), ("Run", "run.md")) }}
