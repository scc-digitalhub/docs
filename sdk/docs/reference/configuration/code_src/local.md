# Code source — Local file

Reference a single local file that contains the code you want to run.

## Quick checklist

- Does your codebase fit within a single file?
- For multi-file codebase, use a [git repository](./git.md) or a [S3 zip archive](./s3.md) to package the code and its dependencies.

## Supported formats

- `path/to/file.py`

## Behavior

- The runtime reads the local file, encodes it, and runs the specified handler.

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
