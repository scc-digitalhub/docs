# Container runtime

The **Container runtime** allows you to create deployments, jobs and services on Kubernetes.

## Prerequisites

Python version and libraries:

- `python >= 3.9`
- `digitalhub-runtime-container`

The package is available on PyPI:

```bash
python -m pip install digitalhub-runtime-container
```

## HOW TO

With the Container runtime you can launch pods and services on Kubernetes. It is built having **remote online execution** capabilities.

### Function

The Container runtime introduces a function of kind `container` that allows you to deploy deployments, jobs and services on Kubernetes.

he syntax for creating a `Function` is the same as the [new_function](../entities/functions/crud.md) method.

#### Function parameters

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| project | str | Project name | required (if creating from library) |
| name | str | Name that identifies the object | required |
| kind | str | Kind of the object | required (must be `container`) |
| uuid | str | ID of the object in form of UUID | None |
| description | str | Description of the object | None |
| git_source | str | Remote git source for object | None |
| labels | list[str] | List of labels | None |
| embedded | bool | Flag to determine if object must be embedded in project | True |
| image | str | The image to use | None |
| base_image | str | The base container image | None (required if task is `build`) |
| command | str | The command to run inside the container | None |
| args | list[str] | The arguments to pass to the command | None |

For example:

```python
import digitalhub as dh

project = dh.get_or_create_project('my_project')
function = dh.new_function(
    kind='container',
    name='my_function',
    image="hello-world:latest"
)
```

### Task

The Container runtime introduces three task's kinds:

- `job`: to deploy a job
- `deploy`: to deploy a deployment
- `serve`: to deploy a service
- `build`: to build a docker image

#### Task parameters

| Name | Type | Description | Default | Kind specific |
| --- | --- | --- | --- | --- |
| action | str | Task action. Must be one of: <li>`job`</li><li>`deploy`</li><li>`build`</li><li>`build`</li> | required | |
| [node_selector](../tasks/kubernetes-resources.md#node_selector) | list[dict] | Node selector | None | |
| [volumes](../tasks/kubernetes-resources.md#volumes) | list[dict] | List of volumes | None | |
| [resources](../tasks/kubernetes-resources.md#resources) | dict | Resources restrictions | None | |
| [affinity](../tasks/kubernetes-resources.md#affinity) | dict | Affinity | None | |
| [tolerations](../tasks/kubernetes-resources.md#tolerations) | list[dict] | Tolerations | None | |
| [envs](../tasks/kubernetes-resources.md#envs) | list[dict] | Env variables | None | |
| [secrets](../tasks/kubernetes-resources.md#secrets) | list[str] | List of secret names | None | |
| backoff_limit | int | Backoff limit | None | `job` |
| schedule | str | Backoff limit | None | `job` |
| instructions | list[str] | Build instructions to be executed as RUN instructions in Dockerfile.<br>Example: `apt install git -y` | None | `build` |
| replicas | int | Number of replicas | None | `deploy`, `serve` |
| service_port| list[dict] | Service port where to expose the service. Must be: [{port: port, target_port: target_port}, ...] | `NodePort` | `serve` |
| service_type| str | Service type. Must be one of: <li>`ClusterIP`</li><li>`LoadBalancer`</li><li>`NodePort`</li> | `NodePort` | `serve` |


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
