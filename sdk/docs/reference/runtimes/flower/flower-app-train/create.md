---
render_macros: true
---

# Create a Flower Application Function

Create a `flower-app` Function from a Flower project in Git or provide the client and server application source directly.

## Parameters

| Name | Type | Description |
| --- | --- | --- |
| project | str | Project name. Required only when creating from the library; otherwise **MUST NOT** be set. |
| name | str | Name that identifies the object. **Required.** |
| kind | str | Function kind. Must be `flower-app`. **Required.** |
| uuid | str | Object ID in UUID4 format. |
| description | str | Description of the object. |
| labels | list[str] | List of labels. |
| embedded | bool | Whether to embed the object in the project. |
| [git_source](../../../configuration/code-sources.md#code-source-uri) | str | Git repository URI containing a Flower application and its `pyproject.toml`. Do not set `client_app` or `server_app` when using this source. |
| [client_code](#source-code) | str | Flower client source code as a Python string. |
| [server_code](#source-code) | str | Flower server source code as a Python string. |
| [client_src](#source-code) | str | Local path to a Flower client Python file. |
| [server_src](#source-code) | str | Local path to a Flower server Python file. |
| [client_app](#application-instances) | str | Name of the Flower client application instance. |
| [server_app](#application-instances) | str | Name of the Flower server application instance. |
| image | str | Custom Docker image for execution. |
| base_image | str | Base Docker image to use. |
| [requirements](#requirements) | list[str] \| str | Additional Python requirements or a supported requirements file path. |

## Source code

`client_code` and `server_code` contain valid Python source as strings. Alternatively, `client_src` and `server_src` point to local Python files. The source is encoded and included in the Function specification.

When using local source, omit `git_source`. When using a Git repository, omit the inline and local source fields.

## Application instances

`client_app` and `server_app` identify instances of the respective classes in the client and server code:

```python
client_app = "name-of-client-class-instance"
server_app = "name-of-server-class-instance"
```

## Requirements

Requirements can be a list of strings or a path to `requirements.txt`, `setup.py`, `pyproject.toml`, `environment.yml`, or `environment.yaml`. The SDK parses requirements when saving the Function. If an unversioned package is available in the local environment, its installed version may be added; use explicit versions or constraints to avoid that inference.

## Example

```python
function = dh.new_function(
    name="my-flower-app",
    kind="flower-app",
    git_source="git+https://github.com/my-org/my-flower-app.git",
)
```

{{ page_navigation(("Action", "action.md"), ("Run", "run.md")) }}
