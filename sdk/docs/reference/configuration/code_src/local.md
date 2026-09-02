# Code source — Local file

Reference local code that is available when the Function is created.

## Quick checklist

- Does your codebase fit within a single file, directory or ZIP archive?
- For code stored elsewhere, use a [git repository](./git.md), [S3 ZIP archive](./s3.md) or [HTTP(S) source](./http.md).

## Supported formats

- `path/to/file.py`
- `path/to/package/`
- `path/to/archive.zip`

## Behavior

- The SDK validates local sources when the Function is created.
- A Python file is encoded into the Function specification.
- A directory is archived and uploaded to the configured default files store.
- A ZIP archive is uploaded to the configured default files store.
- The runtime then imports and runs the specified handler from the resulting source.

## Examples

Minimal handler file (file: `main.py`):

```python
from digitalhub_runtime_python import handler

@handler(outputs=["out"])
def myfunction(di):
    return di
```

Create the Function using the SDK:

```python
# SDK usage
func = dh.new_function(
    name="python-f",
    kind="python",
    code_src="main.py",
    handler="myfunction",
)
```
