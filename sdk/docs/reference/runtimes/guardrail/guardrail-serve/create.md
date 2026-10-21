---
render_macros: true
---

# Create a Guardrail Function

See the [Python handler definition](../../python/define-function.md) for general handler structure and the [Guardrail handler definition](../handler.md) for ExtProc-specific behavior.

## Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| project | str | (✓) | Project name. Required only when creating from the library; otherwise **MUST NOT** be set. |
| name | str | ✓ | Name that identifies the object. |
| kind | str | ✓ | Function kind. Must be `guardrail`. |
| uuid | str | | Object ID in UUID4 format. |
| description | str | | Description of the object. |
| labels | list[str] | | List of labels. |
| embedded | bool | | Whether the object should be embedded in the project. |
| [code_src](../../../configuration/code-sources.md#code-source-uri) | str | | URI pointing to the source code. |
| [code](../../../configuration/code-sources.md#plain-text-source) | str | | Source code provided as plain text. |
| base64 | str | | Source code encoded as base64. |
| [handler](../../../configuration/code-sources.md#handler) | str | | Function entrypoint. |
| init_function | str | | Init function name for remote execution. |
| [python_version](../../python/params.md#supported-python-versions) | str | ✓ | Execution Python version. |
| lang | str | | Source code language (informational). |
| image | str | | Container image used to execute the function. |
| base_image | str | | Base image (name:tag) used when building the execution image. |
| [requirements](../../python/params.md#requirements-and-builds) | list[str] \| str | | Pip requirements or a supported requirements file. |
| processing_mode | str | ✓ | Mode: `preprocessor`, `postprocessor`, or `wrapprocessor`. |

## Example

```python
function = dh.new_function(
    name="request-guardrail",
    kind="guardrail",
    code_src="guardrail.py",
    handler="process",
    python_version="PYTHON3_10",
    processing_mode="preprocessor",
)
```

{{ page_navigation(("Action", "action.md"), ("Run", "run.md")) }}
