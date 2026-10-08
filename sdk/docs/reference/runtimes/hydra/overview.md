# Hydra runtime

The Hydra runtime enables the execuiton of Python jobs using [Hydra](https://hydra.cc) framework.

## Prerequisites

| Requirement | Details |
| --- | --- |
| Package Python requirement | >= 3.10, < 3.15 |
| Execution Python versions | `PYTHON3_10`, `PYTHON3_11`, `PYTHON3_12`, `PYTHON3_13` |
| Package | `digitalhub-runtime-hydra` |

1. Define the Hydra application with the ``@hydra.main`` decorator. 
2. Define the structured baseline configuration (single file or a folder).
3. Define the pre-/post-processing logic (using `init` and `complete` function declarations) to be applied if necessary to the Hydra application.
4. Use `dh.new_function()` or `project.new_function()` to create the Hydra function, passing function parameters and configuration definition.
5. Call `function.run()` with the desired action, passing task parameters and run parameters.

??? example "Create and run a Hydra function"

	```python
	# Create function with function parameters


	func = project.new_function(
		"test-hydra-function", 
		kind="hydra", 
		code_src="./example/my_app.py", 
		config_src="./example/config-dh.yaml", 
		python_version="PYTHON3_13", 
		handler="my_app",
		init_function="init",
		complete_function="complete",
		requirements=["hydra-optuna-sweeper==1.2.0"]
	) 


	# Execute with task and run parameters
	run = func.run(action="job", 
		parameters={
			"hydra.sweeper.n_trials": 5
		},
		workers=5,
		local_execution=False, wait=True
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

For remote `job` runs, a non-empty `requirements` list requires a build so that the dependencies are installed in the execution image. With the default `auto_build=True`, the runtime calls `function.build()` when `spec.image` is `None`. It does not rebuild when an image is already configured, even if requirements are present; after changing requirements, call `function.build()` explicitly or provide an image that already contains them.


## Action documentation

Review the detailed parameters for each Hydra action:

<div class="list-cards" markdown>

- [**Job**](actions/hydra-job.md){ .list-card-link }

	Execute a Hydra function as a one-off task in multirun mode.


- [**Build**](actions/hydra-build.md){ .list-card-link }

	Build a container image for a Hydra function.

</div>

## Examples

<div class="list-cards" markdown>

- [**Hydra examples**](examples.md){ .list-card-link }

	Explore complete examples for Hydra jobs and builds.

</div>
