---
render_macros: true
---

# Create a Container Function for a Build

Define a Function with the container image and build settings.

## Parameters

| Name | Type | Description |
| --- | --- | --- |
| project | str | Project name. Required only when creating from the library; otherwise **MUST NOT** be set. |
| name | str | Name that identifies the object. **Required.** |
| kind | str | Function kind. **Required. Must be `container`** |
| uuid | str | Object ID in UUID4 format. |
| description | str | Description of the object. |
| labels | list[str] | List of labels. |
| embedded | bool | Whether the object should be embedded in the project. |
| [code_src](../../../configuration/code-sources.md#code-source-uri) | str | URI pointing to the source code. |
| [code](../../../configuration/code-sources.md#plain-text-source) | str | Source code provided as plain text. |
| base64 | str | Source code encoded as base64. |
| [handler](../../../configuration/code-sources.md#handler) | str | Function entrypoint. |
| lang | str | Source code language (informational). |
| image | str | Container image to use for execution (name:tag). |
| base_image | str | Base image used when building the execution image. |
| image_pull_policy | str | Kubernetes image pull policy: `Always`, `IfNotPresent` or `Never`. |
| command | str | Command to run inside the container. |

## Example

```python
function = dh.new_function(
    name="my-build",
    kind="container",
    base_image="python:3.9"
)
```

## Function methods

{{ member_doc("build", "digitalhub_runtime_container.entities.function.container.entity.FunctionContainer") }}

{{ page_navigation(("Action", "action.md"), ("Run", "run.md")) }}
