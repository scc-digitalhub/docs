# CLI

The Command-Line Interface (CLI) is a simple tool that offers a number of functionalities to set the platform up.

## Installation

Please refer to [this section](../tasks/cli.md#cli-installation) to install the CLI.

## Commands

Available commands and their parameters are listed here. When you provide *optional* parameters, make sure they are listed **before** *mandatory* ones.

!!! info "Run commands"

    Depending on the shell you are using, you may have to run the CLI with `./dhcli`.

### `register`
`register` takes the following parameters:

- `-n name` (Optional)
- `core_endpoint`

``` sh
dhcli register -n example http://localhost:8080
```
It will create a `.dhcore.ini` file (if it doesn't already exist) in the user's home directory, or, if not possible, in the current one. A section will be appended, using the provided name (or, if missing, the one returned by the endpoint), containing the environment's configuration. This environment will be set as default, unless one is already set.

### `list-env`
`list-env` lists available environments. It takes no parameters.

``` sh
dhcli list-env
```

### `use`
`use` takes the following parameters:

- `environment`

``` sh
dhcli use example
```
This will set the default environment.

### `login`
`login` is to be used after registering an environment with the `register` command. It takes the following parameters:

- `environment` (Optional)

``` sh
dhcli login example
```
It will read the corresponding section from the configuration file and start the log in procedure. It will update this section with the access token obtained. If no environment is specified, it will use the default one.

### `refresh`
`refresh` is to be used after the `login` command, to update `access_token` and `refresh_token`. It takes the following parameters:

- `environment` (Optional)

``` sh
dhcli refresh example
```
If no environment is specified, it will use the default one.

### `remove`
`remove` takes the following parameters:

- `environment`

``` sh
dhcli remove example
```
It will remove the section from the configuration file.

### `init`
`init` is used to install the platform's Python packages; therefore, Python must be installed. It takes the following parameters:

- `environment` (Optional)

``` sh
dhcli init example
```
It will match core's minor version as indicated in the specified environment. If no environment is specified, it will use the default one.
