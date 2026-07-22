# Git credentials

Credentials for accessing private Git repositories are used when the SDK fetches code as a code source. See [Code source](../code_src/git.md) for full details.

Credentials may be supplied as a token or as a username/password pair; tokens take precedence over username/password credentials.

To provide credentials to the execution environment, use one of two methods:

- Environment variables (suitable for local runs)
- DigitalHub Secret (recommended for remote/managed executions)

The credentials are injected into the function runtime environment as environment variables. Git credentials **are not** stored in the `.dhcore.ini` file.

## Environment variables

Set a token/username/password in the process environment before creating the function. This works for local functions.

```python
import os
import digitalhub as dh

os.environ["GIT_TOKEN"] = "ghp_..."
os.environ["GIT_USER"] = "my-username"
os.environ["GIT_PASSWORD"] = "my-password"

func = dh.new_function(
    name="f",
    kind="python",
    code_src="git+https://github.com/my/repo",
    handler="src.app:run",
)
func.run(..., local_execution=True)
```

## DigitalHub Secret

Store credentials securely in the platform as a `Secret` and reference the secret by name when running builds or jobs.

Example — create secrets in a project:

```python
import digitalhub as dh

project = dh.get_or_create_project("my-project")

secret_token = project.new_secret(name="GIT_TOKEN", secret_value="ghp_...")
secret_user = project.new_secret(name="GIT_USER", secret_value="my-username")
secret_password = project.new_secret(name="GIT_PASSWORD", secret_value="my-password")
```

Example — attach a secret to a run or build so the runtime injects it:

```python
# create function (no token in env)
func = dh.new_function(name="f",
                       kind="python",
                       code_src="git+https://github.com/my/repo",
                       handler="src.app:run",
                       python_version="PYTHON3_10")

# run a build or job and provide the secret name
run = func.run(action="build", secrets=["GIT_TOKEN"])
```
