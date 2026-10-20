---
render_macros: true
---

# Create a Ray Function

Define a `ray` Function with its Python source, entrypoint and dependencies.

## Parameters

| Name | Type | Description |
| --- | --- | --- |
| project | str | Project name. Required only when creating from the library; otherwise **MUST NOT** be set. |
| name | str | Name that identifies the object. **Required.** |
| kind | str | Function kind. Must be `ray`. **Required.** |
| uuid | str | Object ID in UUID4 format. |
| description | str | Description of the object. |
| labels | list[str] | List of labels. |
| embedded | bool | Whether to embed the object in the project. |
| [code_src](../../../configuration/code-sources.md#code-source-uri) | str | URI pointing to the source code. |
| [code](../../../configuration/code-sources.md#plain-text-source) | str | Source code provided as plain text. |
| base64 | str | Source code encoded as base64. |
| [handler](../../../configuration/code-sources.md#handler) | str | Function entrypoint. |
| image | str | Container image used to execute the function. |
| [base_image](#base-image) | str | Base image (name:tag) used to build the execution image. |
| [requirements](#requirements) | list[str] \| str | Python requirements or a supported requirements file path. |
| ray_version | str | Ray version to use. |

## Base image

The base image is the foundation used to build the execution image. Some base images may be restricted by cluster security policies; check with the cluster administrator.

## Requirements

Requirements can be a list of strings or a path to `requirements.txt`, `setup.py`, `pyproject.toml`, `conda.yml`, or `conda.yaml`. The SDK parses requirements when saving the Function. If a package is available in the local environment without a version, the SDK may add its installed version; use explicit versions or constraints to avoid this inference.

For remote jobs, non-empty requirements must be installed in the execution image. Build the Function first or provide an image that already contains the required packages.

## Example

```python
function = dh.new_function(
    name="ray-training",
    kind="ray",
    code_src="src/ray_train.py",
    handler="ray_handler",
    requirements=["torch==2.2.2", "numpy==1.24.1"],
)
```

{{ page_navigation(("Action", "action.md"), ("Run", "run.md")) }}
