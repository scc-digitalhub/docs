---
render_macros: true
---

# Python Parameters

## Supported Python versions

Functions can execute with versions `PYTHON3_10`, `PYTHON3_11`, `PYTHON3_12`, `PYTHON3_13` or `PYTHON3_14`.

## Requirements and builds

The `requirements` function parameter accepts requirement strings or a path to `requirements.txt`, `setup.py`, `pyproject.toml`, `conda.yml`, or `conda.yaml`.

```python
requirements = [
    "numpy>=1.21.0",
    "pandas==1.5.3",
    "scipy"
]

# or

requirements = "requirements.txt"

function = dh.new_function(
    name="my-python-function",
    kind="python",
    code_src="handler.py",
    handler="main",
    python_version="PYTHON3_12",
    requirements=requirements,
)
```

??? note "Automatic Version Resolution"
    If a package has no version, the SDK looks for it in the active local virtual environment, adds the installed version when available, and logs a warning. Use an explicit constraint or pin a version for reproducible builds.

    ```python
    # Example of automatic version resolution
    requirements = [
        "numpy",
        "pandas",
    ]

    function = dh.new_function(
        name="my-python-function",
        kind="python",
        code_src="handler.py",
        handler="main",
        python_version="PYTHON3_12",
        requirements=requirements,
    )

    # sdk will resolve the versions automatically
    # function.spec.requirements -> ["numpy==<resolved_version>", "pandas==<resolved_version>"]
    ```

!!! warning "Remote Execution Requirements"
    For remote Job and Serve runs, requirements must be installed in the execution image. This means that you need to execute an action `build` before running any jobs or services that include explicit dependencies.

    ```python
    # First build the function image
    function.run("build", wait=True)

    # Then run the job
    job_run = function.run("job", ...)

    # or run the serve
    serve_run = function.run("serve", ...)
    ```

{{ page_navigation(("Overview", "overview.md")) }}
