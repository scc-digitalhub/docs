---
render_macros: true
---

# Run a Container Build

Call `function.run(action="build", ...)` to build the configured container image. Pass build and execution parameters as keyword arguments to the same call.

## Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| action | str | ✓ | Action to execute. Must be `build` |
| [volumes](../../../configuration/kubernetes.md#volumes) | list[dict] | | List of volumes. |
| [resources](../../../configuration/kubernetes.md#resources) | dict | | Resource values with optional `cpu`, `mem`, `gpu` and `disk` keys. Example: `{"cpu": "1", "mem": "512Mi"}`. |
| [envs](../../../configuration/kubernetes.md#secrets-and-envs) | list[dict] | | Environment variables. Example: `[{"name": "FOO", "value": "bar"}]`. |
| [secrets](../../../configuration/kubernetes.md#secrets-and-envs) | list[str] | | List of secret names. |
| [profile](../../../configuration/kubernetes.md#profile) | str | | Profile template. |
| [instructions](#instructions) | list[str] | | Build instructions executed as `RUN` lines in the generated Dockerfile. |
| base_image | str | | Optional override for the base image used by this build run. |
| image | str | | Optional target image name:tag to build/push. |
| args | list[str] | | Command-line arguments to pass to the container command. |

## Instructions

Instructions are executed as `RUN` instructions in the generated Dockerfile. For example:

```python
instructions = ["apt-get install -y git"]
```

## Example

```python
run = function.run(
    action="build",
    instructions=["pip install numpy", "pip install pandas"],
    args=["--help"]
)
```

## Build and run with dependencies

Configure the base image and target image on the same Function, build it with the required instructions, then run it as a job or service.

```python
function = dh.new_function(
    name="my-function",
    kind="container",
    image="registry.example.com/my-function:latest",
    base_image="python:3.11-slim",
    command="python app.py"
)

function.build(
    instructions=["pip install numpy pandas"]
)

run = function.run(
    action="job",
    args=["input.csv"]
)
```

{{ page_navigation(("Create", "create.md"), ("Use", "use.md")) }}
