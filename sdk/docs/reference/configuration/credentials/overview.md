# Credentials handling

Credentials handling covers access to protected resources (APIs, databases, cloud storage, Git).
Credentials can be supplied via environment variables or `.dhcore.ini` configuration files.

## Environment variables

Set the variables in your shell or CI environment. Example:

```bash
export VAR_NAME=value

# Launch your script / jupyter notebook / etc
```

## Configuration file (.dhcore.ini)

You can also place credentials in the `.dhcore.ini` file under a profile. The file **MUST** be placed in user home directory. The file is structured as follows:

```text
[DEFAULT]
current_environment = local

[local]
dhcore_endpoint = http://192.168.58.2:30180
aws_endpoint_url = http://192.168.58.2:30080
...

[other-env]
dhcore_endpoint = http://other-env:30180
aws_endpoint_url = http://other-env:30080
...
```

The `current_environment` field in the `[DEFAULT]` section selects which credentials profile the SDK will use. There can be multiple profiles (e.g., `local`, `staging`, `production`) and the profile name is user defined. You can use the [`dhcore` CLI](https://scc-digitalhub.github.io/docs/cli/commands/) to manage profiles or the following SDK methods:

```python
import digitalhub as dh

# To read the current profile
dh.get_current_profile()

# To change the current profile
dh.set_current_profile("other-env")
```

## Credentials values

For the credentials fields and values, see each resource page below. Just note that git credentials are **not** stored in the `.dhcore.ini` file.

- [API DHCore](./dhcore.md) - Credentials and utilities for the DigitalHub platform API
- [S3 storage](./s3.md) - Credentials and utilities for S3 storage
- [Databases](./sql.md) - Credentials and utilities for SQL databases
- [Git repositories](./git.md) - Credentials for Git repositories

## Helpers and clients

For SDK helpers that manage credentials profiles, see [credentials helpers](./helpers.md).
For configured store clients, see [store clients](./store-clients.md).
