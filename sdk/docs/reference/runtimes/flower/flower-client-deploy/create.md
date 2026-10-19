---
render_macros: true
---

# Create a Flower Client Function

Define a `flower-client` Function with an existing image or the source settings used by an automatic build.

## Parameters

| Name | Type | Description |
| --- | --- | --- |
| project | str | Project name. Required only when creating from the library; otherwise **MUST NOT** be set. |
| name | str | Name that identifies the object. **Required.** |
| kind | str | Function kind. Must be `flower-client`. **Required.** |
| uuid | str | Object ID in UUID4 format. |
| description | str | Description of the object. |
| labels | list[str] | List of labels. |
| embedded | bool | Whether to embed the object in the project. |
| image | str | Existing Flower client container image. If omitted, `auto_build=True` builds it before deployment. |
| base_image | str | Base Docker image used for an automatic build. |
| [requirements](#requirements) | list[str] \| str | Python requirements used for an automatic build. |

## Requirements

Requirements can be a list of strings or a path to a supported requirements file. The SDK parses them when saving the Function. For an unversioned package available in the local environment, it may add the installed version; use an explicit version or constraint to avoid this inference.

## Example

```python
function = dh.new_function(
    name="my-flower-client",
    kind="flower-client",
    image="my-registry/my-flower-client:latest",
)
```

{{ member_doc("build", "digitalhub_runtime_flower.entities.function._base.entity.FunctionFlowerBuild") }}

{{ page_navigation(("Action", "action.md"), ("Run", "run.md")) }}
