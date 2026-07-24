# Flower App Train

The `train` action executes a complete federated learning training process using a Flower application that includes both client and server components. In local execution mode, it uses [flower's simulation](https://flower.ai/docs/framework/how-to-run-simulations.html).

## Overview

The runtime uses the command `flwr run` to start the Flower application.

There are different ways to create a Flower application function, depending on the source of the code:

1. **From a Git repository**: The source code is stored in a Git repository, and the `source` parameter is used to point to the repository URL. In this case, the `client_app` and `server_app` parameters **MUST NOT** be provided, as the code will be fetched from the repository. The repository **MUST** contain a valid `pyproject.toml` file that configures the Flower application. The run parameters are then used to override the configuration in the file by passing options to the `flwr` command with arguments `--federation-config` and `--run-config`.

2. **From local code references**: The Flower client and server code are provided directly using the `client_app` and `server_app` parameters. In this case, the `source` parameter **MUST NOT** be provided. The client and server code **MUST** be valid Flower implementations. The run parameters are used to create a `pyproject.toml` file that configures the Flower application.

## Quick example with bare minimum parameters

```python
import digitalhub as dh

# Use case referrencing Git repo source code
f = dh.new_function(
    name="my-flower-app",
    kind="flower-app",
    source="git+https://github.com/my-org/my-flower-app.git",
)
run = f.run(action="train")

# Use case using string source code
client_code = """
flower Client code here...
app = ClientClass(...)
"""

server_code = """
flower Server code here...
app = ServerClass(...)
"""
f = dh.new_function(
    name="my-flower-app",
    kind="flower-app",
    client_code=client_code,
    server_code=server_code,
    client_app="name-of-client-class-instance",
    server_app="name-of-server-class-instance",
)


# Use case with client and server in a file reference
f = dh.new_function(
    name="my-flower-app",
    kind="flower-app",
    client_src="path-to-client-file.py",
    server_src="path-to-server-file.py",
    client_app="name-of-client-class-instance",
    server_app="name-of-server-class-instance",
)
run = f.run(
    action="train",
    parameters={...},  # Parameters used to build the pyproject.toml
)
```

## Parameters

### Function Parameters

Must be specified when creating the function.

| Name | Type | Description |
| --- | --- | --- |
| project | str | Project name. Required only when creating from the library; otherwise **MUST NOT** be set. |
| name | str | Name that identifies the object. **Required.** |
| kind | str | Function kind. **Required. MUST BE `flower-app`** |
| uuid | str | Object ID in UUID4 format. |
| description | str | Description of the object. |
| labels | list[str] | List of labels. |
| embedded | bool | Whether the object should be embedded in the project. |
| [git_source](../../../configuration/code_src/git.md) | str | URI pointing to the **git** repo source code. For this runtime there is no need to specify a handler. |
| [client_code](#string-source-code) | str | Source code of the Flower client application as a string. |
| [server_code](#string-source-code) | str | Source code of the Flower server application as a string. |
| [client_src](#local-path-source-code) | str | Local path to the Flower client application source code. |
| [server_src](#local-path-source-code) | str | Local path to the Flower server application source code. |
| [client_app](#appcode) | str | Name of the Flower client application instance. |
| [server_app](#appcode) | str | Name of the Flower server application instance. |
| image | str | Custom Docker image for execution of Flower code. |
| base_image | str | Base Docker image to use. |
| requirements | list[str] | Additional Python package requirements. |

#### String source code

The `client_src` and `server_src` parameters contain the source code of the Flower client and server applications as strings. These strings must be valid Python code. The string source code will be encoded in base64 format and included in the `fab_source` field of the function specification.

#### Local path source code

The `client_src` and `server_src` parameters can also be specified as local paths to the Flower client and server application source code files. These paths must point to valid Python files. The files will be read and their content encoded in base64 format and included in the `fab_source` field of the function specification.

#### Appcode

The `client_app` and `server_app` parameters reference two distinct files that contains valid Flower client and server code respectively. The form they **MUST** take is:

```python
client_app = "name-of-ClientClass-instance"
server_app = "name-of-ServerClass-instance"
```

Where `ClientClass` and `ServerClass` are the classes implementing the Flower client and server respectively.

### Task Parameters

Can only be specified when calling `function.run()`.

| Name | Type | Description |
| --- | --- | --- |
| action | str | Task action. **Required. MUST BE `train`** |
| schedule | str | Quartz cron expression. |
| [volumes](../../../configuration/kubernetes/overview.md#volumes) | list[dict] | List of volumes. |
| [resources](../../../configuration/kubernetes/overview.md#resources) | dict | Resource limits/requests. |
| [envs](../../../configuration/kubernetes/overview.md#secrets-envs) | list[dict] | Environment variables. |
| [secrets](../../../configuration/kubernetes/overview.md#secrets-envs) | list[str] | List of secret names. |
| [profile](../../../configuration/kubernetes/overview.md#profile) | str | Profile template. |

### Run Parameters

Can only be specified when calling `function.run()`.

| Name | Type | Description |
| --- | --- | --- |
| local_execution | bool | Whether to run in local simulation mode. Default: `False`. |
| [parameters](#execution-parameters) | dict | Training configuration parameters. |
| federation | str | Name of the Flower federation for coordination. **Only for remote execution.** |
| superlink | str | SuperLink service endpoint. **Only for remote execution.** |
| root_certificates | str | Content of the root certificate as string. **Only for remote execution.** |

#### Execution parameters

The parameters are used to create the `pyproject.toml` file that configures the Flower application. The parameters depend on the specific Flower client and server implementations used.
Here follws a list of the reserved parameters name used in the file:

| Name | Type | Description |
| --- | --- | --- |
| name | str | Name of the Flower application. Default: `flower-app`. |
| version | str | Version of the Flower application. Default: `0.1.0`. |
| description | str | Description of the Flower application. Default: `Flower Application`. |
| publisher | str | Publisher of the Flower application. Default: `digitalhub-runtime-flower`. |
| dependencies | list[str] | List of Python package dependencies. |
| packages | list[str] | List of Python packages to include. Default: `["."]`. |

Other parameters are parsed with the following rules:

- If the key start with `option.`, the parameter is added to the `[tool.flwr.federations.local-simulation]` section.
- Otherwise, the parameter is added to the `[tool.flwr.app.config]` section.
- `serverapp` and `clientapp` in the `[tool.flwr.app.components]` section are parsed from the parameters of the function.

## Entity methods

### Run methods

There are no additional run methods for this action.
