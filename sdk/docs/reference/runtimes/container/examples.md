# Examples

## Job

```python
import digitalhub as dh

project_name = "my-project"
project = dh.get_or_create_project(project_name)
function = project.new_function(
    kind="container",
    name="my_function",
    image="hello-world:latest",
)

run = function.run(
    action="job",
    run_as_user="8877",
    wait=True,
)
```

## Build

```python
import digitalhub as dh

project_name = "my-project"
project = dh.get_or_create_project(project_name)
function = project.new_function(
    kind="container",
    name="my_function",
    base_image="python:3.11-slim",
)
run = function.run(
    action="build",
    instructions=["RUN apt-get update && apt-get install -y git"],
    wait=True,
)
```

## Serve

```python
import digitalhub as dh

project_name = "my-project"
project = dh.get_or_create_project(project_name)
function = project.new_function(
    kind="container",
    name="my_function",
    image="hashicorp/http-echo:latest",
)
run = function.run(
    action="serve",
    replicas=2,
    service_ports=[{"port": 5678, "target_port": 5678}],
    service_name="http-echo",
    run_as_user="8877",
    wait=True,
)

response = run.invoke()
print(response.text)
```

## Tutorials

Find additional examples in the [tutorial repository](https://github.com/scc-digitalhub/digitalhub-tutorials) of the DSLab GitHub organization.
