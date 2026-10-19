---
render_macros: true
---

# Create a Python Function

Create a `python` function with a handler that follows the [shared handler contract](../../define-function.md).

## Parameters

| Name | Type | Description |
| --- | --- | --- |
| project | str | Project name. Required only when creating from the library; otherwise **MUST NOT** be set. |
| name | str | Name that identifies the object. **Required.** |
| kind | str | Function kind. Must be `python`. **Required.** |
| uuid | str | Object ID in UUID4 format. |
| description | str | Description of the object. |
| labels | list[str] | List of labels. |
| embedded | bool | Whether the object should be embedded in the project. |
| [code_src](../../../../configuration/code-sources.md#code-source-uri) | str | URI pointing to the source code. |
| [code](../../../../configuration/code-sources.md#plain-text-source) | str | Source code provided as plain text. |
| base64 | str | Source code encoded as base64. |
| [handler](../../../../configuration/code-sources.md#handler) | str | Function entrypoint. |
| init_function | str | Init function name for remote execution. |
| python_version | str | Python version: `PYTHON3_10`, `PYTHON3_11`, `PYTHON3_12`, or `PYTHON3_13`. **Required.** |
| lang | str | Source code language (informational). |
| image | str | Container image used to execute the function. |
| base_image | str | Base image (name:tag) used when building the execution image. |
| requirements | list[str] \| str | Pip requirements or a supported requirements file. See [requirements and automatic builds](../overview.md#requirements-and-automatic-builds). |

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

{{ member_doc("build", "digitalhub_runtime_python.entities.function._base.entity.FunctionBaseFunction") }}

{{ page_navigation(("Action", "action.md"), ("Run", "run.md")) }}
