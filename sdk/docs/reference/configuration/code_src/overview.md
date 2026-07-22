# Code source — overview

A code source tells the runtime where to find executable code for a Function or Workflow.

## Quick types

- `code` — inline plain-text source (short scripts). See [Plain text](#plain-text-source).
- `code_src` — URI to a source (local file, git repo, S3 ZIP, HTTP/HTTPS). See [Code source URI](#code-source-uri).

## Quick checklist

- Small snippet? use `code`.
- Files or archives stored remotely or in VCS? use `code_src` and pick the appropriate scheme.

## Plain text source {#plain-text-source}

Provide `code` as a string containing the source code.

Example

```python
my_code = """
def myfunction(di):
    return di
"""

func = dh.new_function(name="python-function", kind="python", code=my_code, handler="myfunction")
```

## Code source URI {#code-source-uri}

`code_src` points to a file or archive. Pick the scheme that matches where your code lives:

- Local single file — `path/to/file.py` — details: [Local file](./local.md)
- Git repo — `git+https://...` — details: [Git repository](./git.md)
- S3 ZIP — `zip+s3://bucket/key.zip` — details: [S3 zip archive](./s3.md)
- HTTP(S) file or ZIP — `https://...` / `zip+https://...` — details: [HTTP(S)](./http.md)

## Handler {#handler}

The `handler` defines the function entrypoint. Rules:

- For inline (`code`), base64 and local files: use the function name (e.g. `myfunction`).
- For repos/archives/remote ZIPs: use `module.path:func` or `path.to.file:func` depending on runtime.

Example (git repo)

`handler="src.pipeline:main"` — runtime imports `src/pipeline.py` and calls `main`.
