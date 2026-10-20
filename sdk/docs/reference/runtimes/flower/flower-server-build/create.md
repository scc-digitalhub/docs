---
render_macros: true
---

# Create a Flower Server Function

Define a `flower-server` Function with its source dependencies and optional image settings.

## Parameters

| Name | Type | Description |
| --- | --- | --- |
| project | str | Project name. Required only when creating from the library; otherwise **MUST NOT** be set. |
| name | str | Name that identifies the object. **Required.** |
| kind | str | Function kind. Must be `flower-server`. **Required.** |
| uuid | str | Object ID in UUID4 format. |
| description | str | Description of the object. |
| labels | list[str] | List of labels. |
| embedded | bool | Whether to embed the object in the project. |
| image | str | Custom image name for the built container. |
| base_image | str | Base Docker image to use for the build. |
| [requirements](#requirements) | list[str] \| str | Additional Python requirements or a supported requirements file path. |

## Requirements

Requirements can be a list of strings or a path to a supported requirements file. The SDK parses them when saving the Function. For an unversioned package available in the local environment, it may add the installed version; use an explicit version or constraint to avoid this inference.

## Example

```python
function = dh.new_function(
    name="my-flower-server",
    kind="flower-server",
    base_image="some-base-image",
    requirements=["flwr==1.17.0"],
)
```

{{ page_navigation(("Action", "action.md"), ("Run", "run.md")) }}
