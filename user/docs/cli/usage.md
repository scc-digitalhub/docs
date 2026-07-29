## CLI usage

!!! info "Run commands"

    Depending on the shell you are using, you may have to run the CLI with `./dhcli`.

The standard use flow of the CLI is as follows:

1. Register your instance's configuration. This creates a `.dhcore.ini` file in your home directory (or, if not possible, in the current one), where the configuration will be stored, to be used and updated by subsequent commands. The register command takes an optional `-e environment ` and a mandatory parameter `core_endpoint` — this is the base URL of your DigitalHub core (e.g. http://localhost:8080).

```sh
dhcli register http://localhost:8080
```

2. Log in. This will open a tab in your Internet browser, where you will have to carry out the log in procedure.

```sh
dhcli login
```

3. If you wish to install the python packages, `init` will do so, matching the platform's version.

```sh
dhcli init
```

In-detail descriptions of available commands can be found in [this dedicated section](../commands.md).

## Common scenarios

Typical uses of the CLI are connected to monitoring executions, managing resources and uploading/downloading artifacts and files.

### Upload/download a file/folder

The CLI enables users in uploading local files and folders as either new artifacts in the catalog or as new versions for the existing content, and also in downloading from the remote repository to the local store.

Given a local file named `abc.txt` and the cli already configured (with a valid session), the upload command can be used to both transfer the file (`-f` parameter) and create the entry in the catalog. Mandatory parameters are the **resource type** and the **name**.

```sh
dhcli upload -p myproject artifact -n abc -f abc.txt
```

The cli will create a new artifact named `abc` and upload the file to the repository.
The same approach can be used to upload folders, by passing the path

```sh
dhcli upload -p myproject artifact -n myfolder -f folder
```

For downloading the files back the `download` command reads the reference from the catalog and then transfers the file (or folder) from the repository back to local storage (`-d` parameter)

```sh
dhcli download -p myproject artifact -n myfolder -d folder
```


## Monitor a run

Given an active run (`RUNNING` state) the CLI enables the user in monitoring the status and fetching the logs.

```sh
dhcli -p myproject list runs -s RUNNING
dhcli -p myproject get run 7a2f5b50fee5454b98977ee4c19741dd -o short
```

will produce a summary like:
```
Name:        rapid-heron
State:       RUNNING
Kind:        vllmserve-text+serve:run
ID:          7a2f5b50fee5454b98977ee4c19741dd
Key:         store://myproject/run/vllmserve-text+serve:run/7a2f5b50fee5454b98977ee4c19741dd:7a2f5b50fee5454b98977ee4c19741dd
Created on:  2026-07-28T09:42:47.432Z
Created by:  ******
Updated on:  2026-07-28T13:37:08.955Z
Updated by:  ******
```

By using the `-o` modifier the user can get the full response in either *json* or *yaml* format, ready to be consumed by tools.


The `log` command fetches the stdout collected by the platform for the given run, with optional live follow (`-f`).


```sh
dhcli -p myproject log 7a2f5b50fee5454b98977ee4c19741dd -f
```


## Proxy and port-forward

The CLI integrates full support for port-forwarding and proxy to let users interact with services deployed in the platform from the local environment. Do note that services are available only inside the perimeter of the platform: external access is not available by default. Common scenarios are testing APIs, viewing and interacting with web consoles, consuming streams etc.

Services can be discovered by leveraging the `services` command in the CLI, for example

```sh
dhcli -p myproject services

NAME           ID                                 FUNCTION        KIND                       SERVICE                                                                    UPDATED                    STATE
rapid-heron    7a2f5b50fee5454b98977ee4c19741dd   wen             vllmserve-text+serve:run   s-vllmserve-textserve-7a2f5b50fee5454b98977ee4c19741dd.dev-platform:8000   2026-07-28T14:36:36.174Z   RUNNING
bright-lion    dc2ed22c8fd144e191cd8d1ea169d090   marimo          container+serve:run        s-containerserve-dc2ed22c8fd144e191cd8d1ea169d090.dev-platform:8080        2026-07-28T14:36:36.28Z    RUNNING
fresh-rabbit   f149076d1252409d87c4633c90e8aefd   nginx           container+serve:run        s-containerserve-f149076d1252409d87c4633c90e8aefd.dev-platform:8080        2026-07-28T14:36:36.291Z   RUNNING
speedy-otter   f2cc4c714f824bfba65049ec3d4426cb   gradioexample   container+serve:run        s-containerserve-f2cc4c714f824bfba65049ec3d4426cb.dev-platform:7860        2026-07-28T14:36:36.3Z     RUNNING

```

will give the list of currently RUNNING services in the given project. 


The `proxy` command can be used for HTTP services and interactive consoles: it will authorize the user browser and set up the connection for reaching a service exposed by a function run.
By executing:

```sh
dhcli -p myproject proxy --function wen
```
the cli will open the default browser, set up the connection through the remote proxy and authorize the session. The user will be able to interact with the remote service as if it was public.

The `port-forward` command can be used to open a bridge between a remote port and a local one, to expose remote services such as APIs for local consumption. By using the port forward any local client can interact with the remote service, without setting up a dedicated connection or authorization: the bridge set up by the CLI is authorized and kept open by the CLI.
By executing:
```sh
dhcli -p myproject port-forward --function wen
✔ Port-forward listening on localhost:45763

```
The cli will open the bridge and expose a automatically assigned local port which can then be used by any client without additional configuration (e.g curl, wget, postman etc).




## Scripting and non-interactive usage

The CLI can be integrated in scripts and custom procedures without the user intervention. To authorize the operation when the user can not perform the `login` action, user can generate a [Personal Access Token](../tasks/pat.md) and use it either as environment variable `DHCORE_PERSONAL_ACCESS_TOKEN` or as param `--pat`.

See the example below for a non-interactive script 

```sh
#!/bin/sh
DHCORE_ENDPOINT="https://core-endpoint"
DHCORE_PERSONAL_ACCESS_TOKEN=my-pat
DH_CONFIG="local-config.ini"

dhcliw() {
    DHCORE_ENDPOINT="${DHCORE_ENDPOINT}" \
    DHCORE_PERSONAL_ACCESS_TOKEN="${DHCORE_PERSONAL_ACCESS_TOKEN}" \
    DH_CONFIG="${DH_CONFIG}" \
    command dhcli "$@"
}

echo "Login to core ${DHCORE_ENDPOINT}..."
dhcliw login

echo "Fetching all projects..."
PROJECTS=$(dhcliw list projects | tail -n +2 | awk '{print $1}')
echo "Found projects: \n${PROJECTS}"

# pick the first project from the list if not empty
FIRST_PROJECT=$(echo "${PROJECTS}" | head -n 1)
if [ -z "${FIRST_PROJECT}" ]; then
    echo "No projects found"
    exit 1
fi

echo "Exporting project ${FIRST_PROJECT} as json to ${FIRST_PROJECT}.json..."
dhcliw get project "${FIRST_PROJECT}" -o json > "${FIRST_PROJECT}.json"

echo "Done."
exit


```



## Initializing a Python environment

The CLI can bootstrap a python environment (backed by Venv or UV) to support local development with the remote platform. When users perform `init` they will create (or activate) a local virtual environment with the correct version of the python sdk `digitalhub[full]` and the python runtime.
The SDK will read the same *configuration file* (`~/.dhcore.ini` by default) as the CLI and connect to the remote enviroment to perform executions, interact with the catalog or upload/download resources.

```sh
$ dhcli init 
...
Using venv path: dev-platform
uv found, using uv for venv and package management
Creating new venv at dev-platform
Newest patch version of digitalhub 0.15 will be installed, continue? Y/n

Installing digitalhub[full]>=0.15.0,<0.16 ...
Using Python 3.14.4 environment at: dev-platform
[...]
Installation complete.

$ python
Python 3.14.4 (main, Jun 18 2026, 14:25:02) [GCC 15.2.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> import digitalhub as dh
>>> proj = dh.get_or_create_project("myproject")

```


