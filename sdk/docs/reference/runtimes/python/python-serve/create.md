---
render_macros: true
---

# Create a Python Function

See the [handler definition](../define-function.md) for the handler structure and behavior.

## Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| project | str | (✓) | Project name. Required only when creating from the library; otherwise **MUST NOT** be set. |
| name | str | ✓ | Name that identifies the object. |
| kind | str | ✓ | Function kind. Must be `python`. |
| uuid | str | | Object ID in UUID4 format. |
| description | str | | Description of the object. |
| labels | list[str] | | List of labels. |
| embedded | bool | | Whether the object should be embedded in the project. |
| [code_src](../../../configuration/code-sources.md#code-source-uri) | str | | URI pointing to the source code. |
| [code](../../../configuration/code-sources.md#plain-text-source) | str | | Source code provided as plain text. |
| base64 | str | | Source code encoded as base64. |
| [handler](../../../configuration/code-sources.md#handler) | str | | Function entrypoint. |
| init_function | str | | Init function name for remote execution. |
| [python_version](../params.md#supported-python-versions) | str | ✓ | Execution Python version. |
| lang | str | | Source code language (informational). |
| image | str | | Container image used to execute the function. |
| base_image | str | | Base image (name:tag) used when building the execution image. |
| [requirements](../params.md#requirements-and-builds) | list[str] \| str | | Pip requirements or a supported requirements file. |

## Example

```python
function = dh.new_function(
    name="my-python-function",
    kind="python",
    code_src="handler.py",
    handler="main",
    python_version="PYTHON3_10",
)
```

{{ page_navigation(("Action", "action.md"), ("Run", "run.md")) }}
