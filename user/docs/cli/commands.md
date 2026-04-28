# CLI commands

Available CLI commands and their parameters are listed here. In these examples, the executable is named `dhcli`.

If you need to install the CLI, refer to [this section](../components/cli.md).

!!! info "Run commands"

    Depending on the shell you are using, you may have to run the CLI with `./dhcli`.

!!! info "Configuration file"

    Commands read from and write to `.dhcore.ini`, located in the user's home directory by default. The path can be overridden by setting the `DH_CONFIG` environment variable.

### Global flags
The following flags are available on every command:

- `-v, --verbose` *Optional*. Boolean. Enable verbose output.
- `--debug` *Optional*. Boolean. Enable HTTP debug logging (implies verbose).

!!! info "Project fallback"

    Commands that take `-p project` will fall back to the `PROJECT_NAME` environment variable if the flag is omitted.

### `register`
`register` takes the following parameters:

- `-e environment` *Optional*. Name of the environment to register. If missing, the `dhcore_name` returned by the endpoint is used.
- `-f, --force` *Optional*. Boolean. Override an existing environment that points to a different endpoint.
- `endpoint` **Mandatory**. Trailing `/` is added automatically if missing.

``` sh
dhcli register -e example http://localhost:8080
```
It will create a `.dhcore.ini` file (if it doesn't already exist) in the user's home directory, or, if not possible, in the current one. The endpoint's `.well-known/configuration` and `.well-known/openid-configuration` are fetched and stored in a section named after the environment. This environment will be set as default, unless one is already set. If a section with the same name already exists with a different endpoint, the command will refuse to overwrite it unless `--force` is set.

### `list-env`
`list-env` lists available environments. It takes no parameters.

``` sh
dhcli list-env
```

### `use`
`use` takes the following parameters:

- `environment` **Mandatory**

``` sh
dhcli use example
```
This will set the default environment.

### `login`
`login` is to be used after registering an environment with the `register` command. It takes the following parameters:

- `-e environment` *Optional*.

``` sh
dhcli login -e example
```
It will read the corresponding section from the configuration file and start the log in procedure (OAuth2 PKCE flow). It will update this section with the access token obtained. If no environment is specified, it will use the default one.

### `refresh`
`refresh` is to be used after the `login` command, to update `access_token` and `refresh_token`. It takes the following parameters:

- `-e environment` *Optional*

``` sh
dhcli refresh -e example
```
If no environment is specified, it will use the default one.

### `remove`
`remove` takes the following parameters:

- `environment` **Mandatory**

``` sh
dhcli remove example
```
It will remove the section from the configuration file.

### `init`
`init` creates or activates a Python virtual environment and installs the platform's Python packages (`digitalhub[full]` and `digitalhub-runtime-python`). Python 3.9–3.12 must be available as `python3`. It takes the following parameters:

- `-e environment` *Optional*
- `--pre` *Optional*. Boolean. Include pre-release (beta) versions when installing packages.
- `path` *Optional*. Filesystem path of the virtual environment. If missing, the current environment name is used; if that is also empty, the current directory is used.

``` sh
dhcli init ./venv
```
It will match core's minor version as indicated in the specified environment. If no environment is specified, it will use the default one. If the path already contains a valid venv, dependencies are installed without recreating it. The command will ask for confirmation before installing.

### `create`
`create` will create an instance of the indicated resource on the platform. It takes the following parameters:

- `-e environment` *Optional*
- `-p project` *Optional* (ignored) when creating projects, **mandatory** otherwise.
- `-f yaml_file_path` **Mandatory** when creating resources other than projects, *alternative* to `-n` for projects.
- `-n name` *Optional* (ignored) when creating resources other than projects, *alternative* to `-f` for projects.
- `-r, --reset-id` *Optional*. Boolean. If set, the `id` specified in the file is ignored and a new one is generated server-side.
- `resource` **Mandatory**

The type of resource to create is mandatory. The project flag `-p` is only mandatory when creating resources other than projects (artifacts, models, etc.). For projects, you may omit the file path and just use the `-n` flag to specify the name. The `--reset-id` flag, when set, ensures the created object has a randomly-generated ID, ignoring the `id` field if present in the input file (this is not relevant to projects).

Create a project:
``` sh
dhcli create -f samples/project.yaml projects
```

Create an artifact, while resetting its ID:
``` sh
dhcli create -p my-project -f samples/artifact.yaml -r artifacts
```

### `list`
`list` returns a list of resources of the specified type. It takes the following parameters:

- `-e environment` *Optional*
- `-o output_format` *Optional*. Accepts `short`, `json`, `yaml`. Defaults to `short`.
- `-p project` *Optional* (ignored) for projects, **mandatory** otherwise.
- `-n name` *Optional*. If present, will return all versions of specified resource. If missing, will return the latest version of all matching resources.
- `-k kind` *Optional*. Filter by kind.
- `-s state` *Optional*. Filter by state.
- `resource` **Mandatory**

`output_format` determines how the output will be formatted. The default value, `short`, is meant to be used to quickly check resources in the terminal, while `json` and `yaml` will format the output accordingly, making it ideal to write to file.

List all projects:

``` sh
dhcli list projects
```

List all artifacts in a project:

``` sh
dhcli list -p my-project artifacts
```

Note that you can easily write the results to file by redirecting standard output:
``` sh
dhcli list -o yaml -p my-project artifacts > output.yaml
```

### `get`
`get` returns the details of a single resource. It takes the following parameters:

- `-e environment` *Optional*
- `-o output_format` *Optional*. Accepts `short`, `json`, `yaml`. Defaults to `short`.
- `-p project` *Optional* (ignored) for projects, **mandatory** otherwise.
- `-n name` *Ignored* if `id` is present, otherwise will return the latest version of the resource matching the name.
- `resource` **Mandatory**
- `id` *Alternative* to `-n name`.

At least one of `id` or `-n name` should be provided to identify the resource. Similarly to the `list` command, `output_format` determines how the output will be formatted. The default value, `short`, is meant to be used to quickly check resources in the terminal, while `json` and `yaml` will format the output accordingly, making it ideal to write to file.

Get project:

``` sh
dhcli get projects my-project
```

Get artifact:
``` sh
dhcli get -p my-project artifacts my-artifact-id
```

Get artifact and write to file:
``` sh
dhcli get -o yaml -p my-project artifacts my-artifact-id > output.yaml
```

### `update`
`update` will update a resource with a new definition. It takes the following parameters:

- `-e environment` *Optional*
- `-p project` *Optional* (ignored) for projects, **mandatory** otherwise.
- `-f yaml_file_path` **Mandatory**
- `resource` **Mandatory**
- `id` **Mandatory**

Update a project:
``` sh
dhcli update -f samples/project.yaml projects my-project
```

Update an artifact:
``` sh
dhcli update -p my-project -f samples/artifact.yaml artifacts my-artifact-id
```

### `delete`
`delete` will delete a resource. It takes the following parameters:

- `-e environment` *Optional*
- `-p project` *Optional* (ignored) for projects, **mandatory** otherwise.
- `-n name` *Alternative* to `id`, will delete all versions of a resource.
- `-y, --confirm` *Optional*. Boolean. If omitted, confirmation will be asked.
- `-c, --cascade` *Optional*. Boolean, only applies to projects. When set, all resources belonging to the project will also be deleted.
- `resource` **Mandatory**
- `id` *Alternative* to `-n name`, will delete a specific version. For projects, since versions do not apply, this is synonym with `name`.

Delete a project and all of its resources:
``` sh
dhcli delete -c projects my-project
```

Delete an artifact, skip confirmation:
``` sh
dhcli delete -p my-project -y artifacts my-artifact-id
```

### `run`
Creates a run of the specified function. It takes the following parameters:

- `-e environment` *Optional*
- `-p project` **Mandatory**
- `-n, --fn-name name_of_function` *Ignored* if `--fn-id` is specified, otherwise **mandatory** and will run the latest version of the function.
- `-i, --fn-id id` *Alternative* to `--fn-name`.
- `-f yaml_file_path` *Optional*, can contain additional parameters for the run.
- `task` **Mandatory**. Must contain a valid task, such as `python+build`.

Create a `python+build` run of latest version of `my-function`:
``` sh
dhcli run -p my-project -n my-function python+build
```

### `log`
Returns the logs of a run. The resource type is implicitly `runs`. It takes the following parameters:

- `-e environment` *Optional*
- `-p project` **Mandatory**
- `-c container` *Optional*. ID of the container to read logs from. If not specified, the main container is derived from the run's task.
- `-f, --follow` *Optional*. Boolean. Will keep updating the printed logs periodically (every 5 seconds) if set.
- `id` **Mandatory**. ID of the run.

Retrieve and follow logs from the main container of a run:
``` sh
dhcli log -p my-project -f my-run-id
```

### `metrics`
Returns metrics for the specified resource. It takes the following parameters:

- `-e environment` *Optional*
- `-p project` **Mandatory**
- `-c container` *Optional*, ID of the container to read metrics from. If not specified, the main container will be picked.
- `resource` **Mandatory**
- `id` **Mandatory**

Retrieve metrics from the main container of a run:
``` sh
dhcli metrics -p my-project run my-run-id
```

### `stop`
Stops a run. The resource type is implicitly `runs`. It takes the following parameters:

- `-e environment` *Optional*
- `-p project` **Mandatory**
- `id` **Mandatory**. ID of the run.

Stop a run:
``` sh
dhcli stop -p my-project my-run-id
```

### `download`
Downloads a resource. It takes the following parameters:

- `-e environment` *Optional*
- `-p project` **Mandatory**
- `-n name` *Alternative* to `id`, will download latest version.
- `-d, --destination output_filename_or_dir` *Optional*, base directory or filename for downloaded resources, will be created if missing.
- `-o output_format` *Optional*. Accepts `short`, `json`, `yaml`. Affects the printed metadata, not the downloaded payload.
- `-v, --verbose` *Optional*. Boolean. Verbose progress/logging.
- `resource` **Mandatory**
- `id` *Alternative* to `-n name`.

Download an artifact:
``` sh
dhcli download -p my-project -d downloaded_artifacts artifact my-artifact-id
```

### `upload`
Uploads a resource to S3. The destination bucket defaults to `datalake` and can be overridden via the `s3_bucket` configuration entry. It takes the following parameters:

- `-e environment` *Optional*
- `-p project` **Mandatory**
- `-n name` Must be specified when creating a new artifact.
- `-f input_filename_or_dir` **Mandatory**, path to input file or directory.
- `-v, --verbose` *Optional*. Boolean. Verbose progress/logging.
- `resource` **Mandatory**
- `id` Must be omitted for new artifacts; used to update an existing artifact.

Upload an artifact:
``` sh
dhcli upload -p my-project -f artifacts/artifact.csv -n my-artifact artifact
```

### `services`
Lists runs filtered by `action=serve`. It takes the following parameters:

- `-e environment` *Optional*
- `-o output_format` *Optional*. Accepts `short`, `json`, `yaml`. Defaults to `short`.
- `-p project` **Mandatory**
- `-n name` *Optional*. If present, will return all versions of the specified service.
- `-k kind` *Optional*. Filter by kind.
- `-s state` *Optional*. Filter by state. Defaults to `RUNNING` when not specified.

List services in a project:
``` sh
dhcli services -p my-project
```

### `proxy`
Starts a local HTTP proxy that forwards requests to the `baseUrl` resolved from a run, going through the configured remote proxy with the appropriate `Authorization` header. It takes the following parameters:

- `-e environment` *Optional*
- `-p project` **Mandatory**
- `-l, --local-port port` *Optional*. Local port to listen on. If missing, a random port is chosen.
- `run-id` **Mandatory**

Start a proxy for a run:
``` sh
dhcli proxy -p my-project my-run-id
```

### `config`
Prints the non-secret configuration of the current (or specified) environment.

- `-e environment` *Optional*
- `-o output_format` *Optional*. Accepts `short`, `json`, `yaml`. Defaults to `short`.

``` sh
dhcli config
```

### `credentials`
Prints the credentials (secret values) stored for the current (or specified) environment.

- `-e environment` *Optional*
- `-o output_format` *Optional*. Accepts `short`, `json`, `yaml`. Defaults to `short`.

``` sh
dhcli credentials
```
