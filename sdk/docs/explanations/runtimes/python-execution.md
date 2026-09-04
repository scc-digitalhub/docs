# Execution Overview

This section explains how to execute a function in the Python runtime.
First, we list the function types and actions, then we examine the usage pattern, including local vs remote execution.
Finally, we provide links to detailed documentation for each parameter category.

## Function types and Actions

The Python runtime supports the following action set

| Function Kind | Supported Actions |
| --- | --- |
| `python` | `job`, `serve`, `build` |

## Usage Pattern

To execute a function, follow this pattern:

1. Implement a Python function (see [Function definition](../../reference/runtimes/python/python/define-function.md) for detailed instructions on creating Python, guardrail, and openinference handlers).
2. Use `dh.new_function()` or `project.new_function()` to create the function, passing **function parameters**.
3. Call `function.run()` with the desired action, passing **task parameters** and **run parameters**.

```python
# Create function with function parameters
function = dh.new_function(
    name="my-function",
    kind="python",
    code_src="handler.py",
    handler="main",
    python_version="PYTHON3_10"
)

# Execute with task and run parameters
run = function.run(
    action="job",  # Task parameter
    inputs={"data": dataitem.key},  # Run parameter
    parameters={"threshold": 0.5}  # Run parameter
)
```

You can control whether the execution happens locally on your machine or remotely on the platform by setting the `local_execution` parameter (see [Local vs Remote Execution](#local-vs-remote-execution) for details).

### Local vs Remote Execution

When executing a function, you can choose between **local execution** and **remote execution** by setting the `local_execution` parameter in the run parameters.

- **Local Execution** (`local_execution=True`): The function runs directly on your local machine. You need to have the required dependencies of your function installed locally.

- **Remote Execution** (`local_execution=False`, default): The function is executed on a remote server or cluster managed by the platform. Provide the dependencies in the function's `requirements` parameter or in a supported requirements file.

### Requirements and automatic builds

The `requirements` function parameter accepts a list of requirement strings or a path to one of these files:

- `requirements.txt` or `setup.py`, parsed as pip requirements
- `pyproject.toml`, read from `project.dependencies`
- `conda.yml` or `conda.yaml`, reading pip dependencies from the `dependencies.pip` section

When the function is saved, the SDK parses a requirements file and normalizes the resulting list. If an unversioned package is installed in the local environment, its installed version is added and a warning is logged. For example, `pandas` can become `pandas==<installed-version>` with a warning that the version was inferred from the local environment. Use an explicit version or version constraint to avoid this inference; pin an exact version for reproducible builds.

For remote `job` and `serve` runs, a non-empty `requirements` list requires a build so that the dependencies are installed in the execution image. Requirements are not installed during the run itself. With the default `auto_build=True`, the runtime calls `function.build()` when `spec.image` is `None`. It does not rebuild when an image is already configured, even if requirements are present; after changing requirements, call `function.build()` explicitly or provide an image that already contains them.

!!! note
    Note that some features, like serving functions, are only available with remote execution.

## Parameter Documentation

Here are links to the detailed documentation for each Python action:

- [Python Job](../../reference/runtimes/python/python/actions/python-job.md) — Execute a `python` function as a one-off task
- [Python Serve](../../reference/runtimes/python/python/actions/python-serve.md) — Deploy a `python` function as an HTTP endpoint
- [Python Build](../../reference/runtimes/python/python/actions/python-build.md) — Build a container image for a `python` function
