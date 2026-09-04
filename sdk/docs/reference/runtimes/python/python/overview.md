# Python runtime

The Python runtime enables you to execute user-defined Python handlers for general-purpose jobs and services. It is managed by the `digitalhub-runtime-python` package.

## Prerequisites

| Requirement | Details |
| --- | --- |
| Package Python requirement | >= 3.10, < 3.15 |
| Execution Python versions | `PYTHON3_10`, `PYTHON3_11`, `PYTHON3_12`, `PYTHON3_13` |
| Package | `digitalhub-runtime-python` |

## Usage pattern

To execute a Python-based handler on the platform:

1. Implement the handler as described in [handler definition](../define-function.md).
2. Use `dh.new_function()` or `project.new_function()` to create the function, passing function parameters.
3. Call `function.run()` with the desired action, passing task parameters and run parameters.

??? example "Create and run a Python function"

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
		action="job",
		inputs={"data": dataitem.key},
		parameters={"threshold": 0.5}
	)
	```

## Local vs remote execution

Set `local_execution` in the run parameters to choose where the function runs.

- **Local execution** (`local_execution=True`): The function runs on the local machine, where its dependencies must already be installed.
- **Remote execution** (`local_execution=False`, default): The function runs on a server or cluster managed by the platform. Provide dependencies through the function's `requirements` parameter or a supported requirements file.

## Requirements and automatic builds

The `requirements` function parameter accepts a list of requirement strings or a path to one of these files:

- `requirements.txt` or `setup.py`, parsed as pip requirements
- `pyproject.toml`, read from `project.dependencies`
- `conda.yml` or `conda.yaml`, reading pip dependencies from the `dependencies.pip` section

When the function is saved, the SDK parses a requirements file and normalizes the resulting list. If a package is specified without a version, the SDK looks for it in the active local virtual environment, adds the installed version when available, and logs a warning. Use an explicit version or version constraint to avoid this inference; pin an exact version for reproducible builds.

For remote `job` and `serve` runs, a non-empty `requirements` list requires a build so that the dependencies are installed in the execution image. With the default `auto_build=True`, the runtime calls `function.build()` when `spec.image` is `None`. It does not rebuild when an image is already configured, even if requirements are present; after changing requirements, call `function.build()` explicitly or provide an image that already contains them.

!!! note
	Serving functions are available only with remote execution.

## Action documentation

Review the detailed parameters for each Python action:

<div class="list-cards" markdown>

- [**Job**](actions/python-job.md){ .list-card-link }

	Execute a Python function as a one-off task.

- [**Serve**](actions/python-serve.md){ .list-card-link }

	Deploy a Python function as an HTTP endpoint.

- [**Build**](actions/python-build.md){ .list-card-link }

	Build a container image for a Python function.

</div>

## Examples

<div class="list-cards" markdown>

- [**Python examples**](examples.md){ .list-card-link }

	Explore complete examples for Python jobs, services and builds.

</div>
