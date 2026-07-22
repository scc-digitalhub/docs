# Code source — HTTP(S) file or ZIP

Use an HTTP(S) URL to point the runtime at either a single Python source file or a ZIP archive containing a package.

## Quick checklist

- Is the URL reachable from the runtime environment?
- Is the content a single Python file or a ZIP archive? Use `zip+https://...` for archives.

## Supported formats

- Plain file: `https://host/path/file.py`
- ZIP archive: `zip+https://host/path/archive.zip`

## Behavior

- Plain file: the runtime fetches the file and imports the top-level handler name you provide (for example `handler='main'`).
- ZIP archive: the runtime extracts the archive and imports the handler in the form `module:callable` (for example `handler='pkg.module:func'`).

## Examples

```python
# Plain file (single module)
func = dh.new_function(
    name='hello',
    kind='python',
    code_src='https://example.com/my_function.py',
    handler='main',
)

# ZIP archive (package inside archive)
func = dh.new_function(
    name='worker',
    kind='python',
    code_src='zip+https://example.com/code_bundle.zip',
    handler='pkg.handlers:process',
)
```
