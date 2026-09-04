# Code sources

A code source tells the runtime where to find executable code for a Function or Workflow.
Use inline `code` for short scripts, or `code_src` for files, archives and remote repositories.

## Quick reference

| Source | `code_src` | Typical handler |
| --- | --- | --- |
| Plain text | Not required | `myfunction` |
| Local file, directory or ZIP | `path/to/source` | `myfunction` |
| Git repository | `git+https://...` | `module.path:func` |
| S3 ZIP archive | `zip+s3://...` | `module.path:func` |
| HTTP(S) file or ZIP | `https://...` or `zip+https://...` | `main` or `module:func` |

## Plain text source

Provide `code` as a string containing the source code.

```python
my_code = """
def myfunction(di):
    return di
"""

func = dh.new_function(
    name="python-function",
    kind="python",
    code=my_code,
    handler="myfunction",
)
```

## Code source URI

`code_src` points to a local source, remote file or archive. Select the tab that matches where the code lives.

=== "Local file"

    Format

    ``` bash
    path/to/file.py
    path/to/package/
    path/to/archive.zip
    ```

    Behavior

    - The SDK validates local sources when the Function is created.
    - A Python file is encoded into the Function specification.
    - A directory is archived and uploaded to the configured default files store.
    - A ZIP archive is uploaded to the configured default files store.
    - The runtime imports and runs the specified handler from the resulting source.

    Example

    ```python
    func = dh.new_function(
        name="python-f",
        kind="python",
        code_src="main.py",
        handler="myfunction",
    )
    ```

=== "Git repository"

    Format

    ``` bash
    # The optional fragment selects a reference after cloning.
    git+https://github.com/user/repo#branch-or-tag-or-commit
    ```

    Behavior

    - The runtime clones the repository at run or build time.
    - It imports the module or file indicated by the `handler`.
    - The `handler` typically follows `module.submodule:function` or `path.to.file:callable` syntax.

    Example

    ```python
    func = dh.new_function(
        name="worker",
        kind="python",
        code_src="git+https://github.com/my/repo#main",
        handler="src.app:handler",
    )
    ```

    For private repositories, configure [Git credentials](credentials.md).

=== "S3 ZIP archive"

    Format

    ``` bash
    zip+s3://bucket/path/to/archive.zip
    ```

    Behavior

    - The runtime downloads and extracts the ZIP archive.
    - The `handler` must reference a module and callable using `module:callable`.

    Example

    ```python
    func = dh.new_function(
        name="worker",
        kind="python",
        code_src="zip+s3://my-bucket/my-code.zip",
        handler="app.main:handler",
    )
    ```

    For private buckets, configure [S3 credentials](credentials.md).

=== "HTTP(S) file or ZIP"

    Format

    ``` bash
    https://host/path/file.py
    zip+https://host/path/archive.zip
    ```

    Behavior

    - A plain file is fetched and the top-level handler name is imported.
    - A ZIP archive is extracted and the handler uses `module:callable` syntax.

    Example

    ```python
    plain_file = dh.new_function(
        name="hello",
        kind="python",
        code_src="https://example.com/my_function.py",
        handler="main",
    )

    zip_archive = dh.new_function(
        name="worker",
        kind="python",
        code_src="zip+https://example.com/code_bundle.zip",
        handler="pkg.handlers:process",
    )
    ```

## Handler

The `handler` defines the function entrypoint:

- For inline `code`, base64 and local files, use the function name (for example `myfunction`).
- For repositories and remote ZIPs, use `module.path:func` or `path.to.file:func` depending on the runtime.
- For a Git repository, `handler="src.pipeline:main"` imports `src/pipeline.py` and calls `main`.
