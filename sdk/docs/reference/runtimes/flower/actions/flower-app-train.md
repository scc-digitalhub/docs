# Flower App Train

## Train reference

<div class="list-cards" markdown>

- [**Overview**](#overview){ .list-card-link } - Understand what the train action does.

- [**Function**](#function){ .list-card-link } - Create a Flower application Function.

- [**Task**](#task){ .list-card-link } - Configure the Flower training Task.

- [**Run**](#run){ .list-card-link } - Execute Flower training.

</div>

## Overview

The `train` action executes a complete federated learning training process using a Flower application that includes both client and server components. In local execution mode, it uses [flower's simulation](https://flower.ai/docs/framework/how-to-run-simulations.html).

The runtime uses the command `flwr run` to start the Flower application.

There are different ways to create a Flower application function, depending on the source of the code:

1. **From a Git repository**: The source code is stored in a Git repository, and the `git_source` parameter is used to point to the repository URL. In this case, the `client_app` and `server_app` parameters **MUST NOT** be provided, as the code will be fetched from the repository. The repository **MUST** contain a valid `pyproject.toml` file that configures the Flower application. The run parameters are then used to override the configuration in the file by passing options to the `flwr` command with arguments `--federation-config` and `--run-config`.

2. **From local code references**: The Flower client and server code are provided directly using the `client_app` and `server_app` parameters. In this case, the `git_source` parameter **MUST NOT** be provided. The client and server code **MUST** be valid Flower implementations. The run parameters are used to create a `pyproject.toml` file that configures the Flower application.

## Function

??? example "Create a function"

    Define the Function using a Git repository or local Flower client and server code.

    === "Parameters"

        | Name | Type | Description |
        | --- | --- | --- |
        | project | str | Project name. Required only when creating from the library; otherwise **MUST NOT** be set. |
        | name | str | Name that identifies the object. **Required.** |
        | kind | str | Function kind. **Required. MUST BE `flower-app`** |
        | uuid | str | Object ID in UUID4 format. |
        | description | str | Description of the object. |
        | labels | list[str] | List of labels. |
        | embedded | bool | Whether the object should be embedded in the project. |
        | [git_source](../../../configuration/code-sources.md#code-source-uri) | str | URI pointing to the **git** repo source code. For this runtime there is no need to specify a handler. |
        | [client_code](#string-source-code) | str | Source code of the Flower client application as a string. |
        | [server_code](#string-source-code) | str | Source code of the Flower server application as a string. |
        | [client_src](#local-path-source-code) | str | Local path to the Flower client application source code. |
        | [server_src](#local-path-source-code) | str | Local path to the Flower server application source code. |
        | [client_app](#appcode) | str | Name of the Flower client application instance. |
        | [server_app](#appcode) | str | Name of the Flower server application instance. |
        | image | str | Custom Docker image for execution of Flower code. |
        | base_image | str | Base Docker image to use. |
        | requirements | list[str] \| str | Additional Python package requirements or a supported requirements file path. |

        #### String source code

        The `client_code` and `server_code` parameters contain the source code of the Flower client and server applications as strings. These strings must be valid Python code. The string source code will be encoded in base64 format and included in the `fab_source` field of the function specification.

        #### Local path source code

        The `client_src` and `server_src` parameters can be specified as local paths to the Flower client and server application source code files. These paths must point to valid Python files. The files will be read and their content encoded in base64 format and included in the `fab_source` field of the function specification.

        #### Appcode

        The `client_app` and `server_app` parameters reference two distinct files that contains valid Flower client and server code respectively. The form they **MUST** take is:

        ```python
        client_app = "name-of-ClientClass-instance"
        server_app = "name-of-ServerClass-instance"
        ```

        Where `ClientClass` and `ServerClass` are the classes implementing the Flower client and server respectively.

        #### Requirements

        `requirements` accepts a list of requirement strings or a path to a supported requirements file: `requirements.txt`, `setup.py`, `pyproject.toml`, `environment.yml`, or `environment.yaml`. The SDK parses the requirements when the function is saved. For an unversioned package found in the local environment, it adds the installed version and logs a warning; use an explicit version or constraint to avoid this inference.

    === "Creation example"

        ```python
        import digitalhub as dh

        f = dh.new_function(
            name="my-flower-app",
            kind="flower-app",
            git_source="git+https://github.com/my-org/my-flower-app.git",
        )

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

        f = dh.new_function(
            name="my-flower-app",
            kind="flower-app",
            client_src="path-to-client-file.py",
            server_src="path-to-server-file.py",
            client_app="name-of-client-class-instance",
            server_app="name-of-server-class-instance",
        )
        ```

### Function methods

The Flower application Function does not add runtime-specific methods.

## Task

??? example "Create a task"

    === "Parameters"

        | Name | Type | Description |
        | --- | --- | --- |
        | action | str | Task action. **Required. MUST BE `train`** |
        | schedule | str | Quartz cron expression. |
        | [volumes](../../../configuration/kubernetes.md#volumes) | list[dict] | List of volumes. |
        | [resources](../../../configuration/kubernetes.md#resources) | dict | Resource limits/requests. |
        | [envs](../../../configuration/kubernetes.md#secrets-and-envs) | list[dict] | Environment variables. |
        | [secrets](../../../configuration/kubernetes.md#secrets-and-envs) | list[str] | List of secret names. |
        | [profile](../../../configuration/kubernetes.md#profile) | str | Profile template. |

    === "Creation example"

        ```python
        run = f.run(action="train")
        ```

### Task methods

The Flower training Task does not add runtime-specific methods.

## Run

??? example "Create a run"

    === "Parameters"

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

    === "Creation example"

        ```python
        run = f.run(
            action="train",
            local_execution=False,
            parameters={...},
        )
        ```

### Run methods

`run.local_execution()` returns whether the run uses local Flower simulation mode.
