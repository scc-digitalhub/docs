# Code source

In several runtime objects, it is possible to execute a program (e.g. a function, a query or a workflow) written in a source. This source can be a single code file, a plain text string or a base64 encoded string, a zip archive or a git repository.
Beside the source, you need also to define a [`handler`](#handler), which is the entrypoint of the code.

## Code source definition

In the SDK, there are three different types of source code:

- [`code`](#plain-text-source) which is a plain string source.
- [`base64`](#base64-encoded-source) which is a base64 encoded string source.
- [`code_src`](#code-source-uri) which is a code source URI.

### Plain text source

You can define a plain text source using the `code` parameter.

Here follow an example of a plain text source with the [Python runtime](../runtimes/python.md):

```python
my_code = """
from digitalhub_runtime_python import handler

@handler(outputs=["filtered"])
def myfunction(di: Dataitem, col1: str):
    df = di.as_df()
    df = df[["col1"]]
    return df
"""

func = dh.new_function(project="my-project",
                       name="python-function",
                       kind="python",
                       python_version="PYTHON3_9",
                       code=my_code,
                       handler="myfunction")
```

In this case the function will execute the code in the `my_code` variable.

### Base64 encoded source

You can define a base64 encoded source using the `base64` parameter.

Here follow an example of a base64 encoded source with the [Python runtime](../runtimes/python.md):

```python
# Same function as above encoded in base64
base64_code = "ZnJvbSBkaWdpdGFsaHViX3J1bnRpbWVfcHl0aG9uIGltcG9ydCBoYW5kbGVyCgpAaGFuZGxlcihvdXRwdXRzPVsiZmlsdGVyZWQiXSkKZGVmIG15ZnVuY3Rpb24oZGk6IERhdGFpdGVtLCBjb2wxOiBzdHIpOgogICAgZGYgPSBkaS5hc19kZigpCiAgICBkZiA9IGRmW1siY29sMSJdXQogICAgcmV0dXJuIGRm"

func = dh.new_function(project="my-project",
                       name="python-function",
                       kind="python",
                       python_version="PYTHON3_9",
                       base64=base64_code,
                       handler="myfunction")
```

In this case the function will execute the code in the `base64_code` variable.

### Code source URI

You can define a code source URI using the `code_src` parameter.
We support the following types of URIs:

- [Local file path](#local-file-path)
- [Git repository](#remote-git-repository)
- [S3 zip archive](#remote-zip-s3-archive)

#### Local file path

The local file path can be specified with the `path/to/file.ext` format.

```python
my_code = "src/my-func.py"

func = dh.new_function(project="my-project",
                       name="python-function",
                       kind="python",
                       python_version="PYTHON3_9",
                       code_src=my_code,
                       handler="myfunction")
```

In this case the function will import the code in the `src/my-func.py` file, encodes it in base64 and then executes it. If the file is not found, the function will raise an exception.

#### Remote git repository

The remote git repository can be specified with the `git+https://repo-host.com/some-user/some-repo` format.
The anteposition `git+` is required, the rest of the URL is the repository URL.

```python
my_repo = "git+https://repo-host/some-user/some-repo"

func = dh.new_function(project="my-project",
                       name="python-function",
                       kind="python",
                       python_version="PYTHON3_9",
                       code_src=my_repo,
                       handler="path:function")
```

When a git repository is specified, the function try to clone the repository and execute the code in the specified in the `handler` entrypoint (See below). If the repository does not exist, the function will raise an exception.

##### Credentials

You may need credentials to access the repository. The credentials can be specified in three environment variables: `GIT_TOKEN`, `GIT_USER`and `GIT_PASSWORD`.

!!! note
    You **must** set the env variable **before** defining the function. Token auth is recommended and takes precedence over basic auth. Please also verify that the repo provider supports basic auth.

###### Token

The token is a plain string. It will be passed in the URL according to the git provider.

Example:

```python
# GitHub token
os.environ["GIT_TOKEN"] = "github_pat_..."

# GitLab token
os.environ["GIT_TOKEN"] = "glpat..."

# function definition
```

###### User and password

User and password are plain strings.

```python
os.environ["GIT_USER"] = "some-user"
os.environ["GIT_PASSWORD"] = "some-password"

# function definition
```

#### Remote zip s3 archive

The remote zip s3 archive can be specified with the `zip+s3://some-bucket/some-key.zip` format. The anteposition `zip+` is required, the rest of the URL is an S3 URL in the form `s3://some-bucket/some-key.zip`.
The code source is archived in a zip file, which is unpacked at runtime.

```python
my_archive = "zip+s3://some-bucket/some-key.zip"

func = dh.new_function(project="my-project",
                       name="python-function",
                       kind="python",
                       python_version="PYTHON3_9",
                       code_src=my_archive,
                       handler="path:function")
```

## Handler

The `handler` parameter is the entrypoint of the code. There are some rules to follow when defining it.

If the source code is:

- [Plain text](#plain-text-source)
- [Base64 encoded](#base64-encoded-source)
- [Local file path](#local-file-path)

Then the entrypoint should be the **function name**.

```python
my_code = """
def myfunction():
    ...
"""

func = dh.new_function(...,
                       code=my_code,
                       handler="myfunction")
```

If the source code is:

- [S3 zip archive](#remote-zip-s3-archive)
- [Git repository](#remote-git-repository)

Then the entrypoint should be the path to the file where the code is stored (expressed with `.` separator) and the name of the function separated by a `:`.

```python
my_code = "git+https://repo-host/some-user/some-repo"

func = dh.new_function(...,
                       code_src=my_code,
                       handler="src.subdir.etc:myfunction")
```
