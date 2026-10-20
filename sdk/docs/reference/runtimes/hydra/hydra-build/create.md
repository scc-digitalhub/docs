---
render_macros: true
---

# Create a Hydra Function

Define a `hydra` Function with its Python source, configuration and execution settings.

## Parameters

| Name | Type | Description |
| --- | --- | --- |
| project | str | Project name. Required only when creating from the library; otherwise **MUST NOT** be set. |
| name | str | Name that identifies the object. **Required.** |
| kind | str | Function kind. Must be `hydra`. **Required.** |
| uuid | str | Object ID in UUID4 format. |
| description | str | Description of the object. |
| labels | list[str] | List of labels. |
| embedded | bool | Whether to embed the object in the project. |
| [code_src](../../../configuration/code-sources.md#code-source-uri) | str | URI pointing to the source code. |
| [code](../../../configuration/code-sources.md#plain-text-source) | str | Source code provided as plain text. |
| base64 | str | Source code encoded as base64. |
| config_src | str | URI pointing to the Hydra configuration. |
| config | str | Configuration YAML provided as plain text. |
| config_base64 | str | Configuration YAML encoded as base64. |
| config_path | str | Configuration folder path relative to the function source folder. |
| [handler](../../../configuration/code-sources.md#handler) | str | Function entrypoint. |
| [init_function](#lifecycle-functions) | str | Init function name for remote execution. |
| [complete_function](#lifecycle-functions) | str | Finalize function name for remote execution. |
| [python_version](#python-versions) | str | Python version to use. **Required.** |
| lang | str | Source code language (informational). |
| image | str | Container image used to execute the function. |
| [base_image](#base-image) | str | Base image (name:tag) used to build the execution image. |
| [requirements](#requirements) | list[str] \| str | Python requirements or a supported requirements file path. |

## Python versions

Supported values are `PYTHON3_10`, `PYTHON3_11`, `PYTHON3_12`, and `PYTHON3_13`.

## Lifecycle functions

`init_function` names the function called by the init wrapper. `complete_function` names the function called by the finalizer wrapper.

## Base image

The base image (name and tag) is used as the foundation for the execution image. Some base images may be restricted by cluster security policies; check with the cluster administrator.

## Requirements

Requirements can be a list of strings or a path to `requirements.txt`, `setup.py`, `pyproject.toml`, `conda.yml`, or `conda.yaml`. The SDK parses requirements when saving the Function. If a package is available in the local environment without a version, the SDK may add its installed version; use explicit versions or constraints to avoid this inference.

## Example

```python
function = dh.new_function(
    name="my-hydra-function",
    kind="hydra",
    code_src="./example/my_app.py",
    config_src="./example/config-dh.yaml",
    python_version="PYTHON3_13",
    handler="my_app",
)
```

{{ page_navigation(("Action", "action.md"), ("Run", "run.md")) }}
