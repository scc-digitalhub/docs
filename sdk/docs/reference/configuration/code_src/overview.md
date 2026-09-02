# Code source — overview

A code source tells the runtime where to find executable code for a Function or Workflow.

## Quick types

- `code` — inline plain-text source (short scripts). See [Plain text](#plain-text-source)
- `code_src` — URI or local path to a source (local file/directory/ZIP, git repo, S3 ZIP, HTTP/HTTPS). See [Code source URI](#code-source-uri).

## Quick checklist

- Small snippet? use `code`.
- Files or archives stored remotely or in VCS? use `code_src` and pick the appropriate scheme.

## Plain text source

Provide `code` as a string containing the source code.

Example

```python
my_code = """
def myfunction(di):
    return di
"""

func = dh.new_function(name="python-function", kind="python", code=my_code, handler="myfunction")
```

## Code source URI

`code_src` points to a local source, remote file or archive. Pick the form that matches where your code lives:

- Local file, directory or ZIP — `path/to/source` — details: [Local file](./local.md)
- Git repo — `git+http://...` or `git+https://...` — details: [Git repository](./git.md)
- S3 ZIP — `zip+s3://...`, `zip+s3a://...` or `zip+s3n://...` — details: [S3 zip archive](./s3.md)
- HTTP(S) file or ZIP — `http://...` / `https://...` / `zip+http://...` / `zip+https://...` — details: [HTTP(S)](./http.md)

## Handler

The `handler` defines the function entrypoint. Rules:

- For inline (`code`), base64 and local files: use the function name (e.g. `myfunction`).
- For repos/archives/remote ZIPs: use `module.path:func` or `path.to.file:func` depending on runtime.

## Initialization function

Set `init_function` to an optional callable that the runtime imports from the same module as `handler`. It is invoked for initialization before the main handler is used.

```python
func = dh.new_function(
    name="python-function",
    kind="python",
    code="""
def initialize():
    pass

def myfunction(di):
    return di
""",
    handler="myfunction",
    init_function="initialize",
)
```

Example (git repo)

`handler="src.pipeline:main"` — runtime imports `src/pipeline.py` and calls `main`.
