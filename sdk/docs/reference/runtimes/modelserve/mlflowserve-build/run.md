---
render_macros: true
---

# Build an MLflow Serving Image

Call `function.run(action="build", ...)` to build the MLflow model-serving image.

## Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| action | str | ✓ | Action to execute. Must be `build` |
| [volumes](../../../configuration/kubernetes.md#volumes) | list[dict] | | List of volumes. |
| [resources](../../../configuration/kubernetes.md#resources) | dict | | Resource limits and requests. |
| [envs](../../../configuration/kubernetes.md#secrets-and-envs) | list[dict] | | Environment variables. |
| [secrets](../../../configuration/kubernetes.md#secrets-and-envs) | list[str] | | List of secret names. |
| [profile](../../../configuration/kubernetes.md#profile) | str | | Profile template. |
| [replicas](../../../configuration/kubernetes.md#replicas) | int | | Number of replicas. |
| [service_type](../../../configuration/kubernetes.md#service-port-and-type) | str | | Service type. |
| service_name | str | | Service name. |
| [instructions](#instructions) | list[str] | | Build instructions executed as `RUN` lines in the generated Dockerfile. |

## Instructions

Instructions are executed as `RUN` instructions in the generated Dockerfile. For example:

```python
instructions = ["apt-get install -y git"]
```

## Example

```python
build_run = function.run(
    action="build",
    instructions=["pip install -r requirements.txt"]
)
```

{{ page_navigation(("Create", "create.md"), ("Use", "use.md")) }}
