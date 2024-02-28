# Container runtime

The Container runtime allows you to deploy deployments, jobs and services on Kubernetes.

## Prerequisites

Python libraries:

- python 3.9 or 3.10
- digitalhub sdk

Install digitalhub sdk and collect digitalhub container modules:

```bash
pip install digitalhub
git clone https://github.com/scc-digitalhub/digitalhub-sdk.git
pip install digitalhub-sdk/core/modules/container/ --no-deps
```

## Function

The Container runtime introduces a function of kind `container` that allows you to deploy deployments, jobs and services on Kubernetes.

### Container function parameters

When you create a function of kind `container`, you must specify the following mandatory parameters:

- **`project`**: the project name with which the function is associated. **Only** if you do not use the project context to create the function, e.g. `project.new_function()`.
- **`name`**: the name of the function
- **`kind`**: the kind of the function, **must** be `container`
- **`image`**: the container image to deploy

Optionally, you can specify the following parameters:

- **`uuid`**: the uuid of the function (this is automatically generated if not provided). **Must** be a valid uuid v4.
- **`description`**: the description of the function
- **`labels`**: the labels of the function
- **`source_remote`**: the remote source of the function (git repository)
- **`embedded`**: whether the function is embedded or not. If `True`, the function is embedded (all the details are expressed) in the project. If `False`, the function is not embedded in the project.
- **`base_image`**: the base container image.
- **`command`**: the command to run inside the container.
- **`entrypoint`**: the entrypoint to run inside the container.
- **`args`**: the arguments to pass to the entrypoint.

For example:

```python
import digitalhub as dh

project = dh.get_or_create_project('my_project')
function = dh.new_function(
    kind='dbt',
    name='my_function',
    image="hello-world:latest"
)
```

## Task

The Container runtime introduces three task's kinds:

- `job`: to deploy a job
- `deploy`: to deploy a deployment
- `serve`: to deploy a service

### Run and task parameters

When you want to execute a task, you **must** pass the following mandatory parameters to the function method `run()`:

- **`action`**: the action to perform. Can be `job`, `deploy` or `serve`.

As optional, you can pass the following task parameters specific for remote execution:

- **`node_selector`**: a list of node selectors. The runtime will select the nodes to which the task will be scheduled.
- **`volumes`**: a list of volumes
- **`resources`**: a list of resources (CPU, memory, GPU)
- **`labels`**: a list of labels to attach to kubernetes resources
- **`affinity`**: node affinity
- **`tolerations`**: tolerations
- **`env`**: environment variables to inject in the container
- **`secrets`**: list of secrets to inject in the container

For the `serve` action, you can also pass the following task parameters:

- **`service_ports`**: a list of ports to expose
- **`service_type`**: the type of service

For example:

```python
run = function.run(
    action='job'
)
```

## Notes

The Container runtime does not support local execution.

## Snippet example

```python
import digitalhub as dh

proj = dh.get_or_create_project("project-container")

# Run container
func_cont = proj.new_function(name="function-container",
                              kind="container",
                              image="hello-world:latest")
run_cont = func_cont.run("job")


# Serve stremlit service
func_serve = proj.new_function(name="function-serve",
                               kind="container",
                               image="ghcr.io/scc-digitalhub/digitalhub-core-streamlit:latest")
run_serve = func_serve.run("serve",
                           service_ports= [{"port": 8085, "target_port": 8501}],
                           service_type="NodePort")
```
