---
render_macros: true
---

# Create a Flower Client Function

Define a `flower-client` Function with an image created by the client Build action.

## Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| project | str | (✓) | Project name. Required only when creating from the library; otherwise **MUST NOT** be set. |
| name | str | ✓ | Name that identifies the object. |
| kind | str | ✓ | Function kind. Must be `flower-client`. |
| uuid | str | | Object ID in UUID4 format. |
| description | str | | Description of the object. |
| labels | list[str] | | List of labels. |
| embedded | bool | | Whether to embed the object in the project. |
| image | str | | Flower client container image used for deployment. |
| base_image | str | | Base Docker image used by the client Build action. |
| [requirements](#requirements) | list[str] \| str | | Python requirements installed by the client Build action. |

## Requirements

Requirements can be a list of strings or a path to a supported requirements file. The SDK parses them when saving the Function. For an unversioned package available in the local environment, it may add the installed version; use an explicit version or constraint to avoid this inference. Include the requirements in the [Flower Client Build action](../flower-client-build/action.md) before deployment.

## Example

```python
function = dh.new_function(
    name="my-flower-client",
    kind="flower-client",
    image="my-registry/my-flower-client:latest",
)
```

{{ page_navigation(("Action", "action.md"), ("Run", "run.md")) }}
