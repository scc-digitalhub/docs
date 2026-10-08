# Ray runtime

The Ray runtime enables the execuiton of Python application using [Ray](https://ray.io) framework on top of the dynamically created Ray cluster.

## Prerequisites

| Requirement | Details |
| --- | --- |
| Package Python requirement | >= 3.10, < 3.15 |
| Package | `digitalhub-runtime-ray` |

1. Implement Ray application, optionally making explicit the entry point function to pass references to the platform entities (project and run). 
2. Define the configuration of the cluster (mininamum, initial, maximum number of worker nodes, the resources to be allocated by each node).
3. Use `dh.new_function()` or `project.new_function()` to create the Ray function, passing function parameters and configuration definition.
4. Call `function.run()` with the desired action, passing task parameters and run parameters.

??? example "Create and run a Ray function"

	```python
	# Create function with function parameters


	func = project.new_function(
		"test-ray-function", 
		kind="ray", 
		code_src="./src/ray_train.py", 
		handler="ray_handler",
		requirements=["torch==2.2.2", "torchvision==0.17.2", "numpy==1.24.1"]
	) 


	# Execute with task and run parameters
	run = func.run(action="job", 
		replicas=1,
		min_replicas=1,
		max_replicas=4,
		parameters={"epochs": 10}
	)

	```

## Requirements and automatic builds

The `requirements` function parameter accepts a list of requirement strings or a path to one of these files:

- `requirements.txt` or `setup.py`, parsed as pip requirements
- `pyproject.toml`, read from `project.dependencies`
- `conda.yml` or `conda.yaml`, reading pip dependencies from the `dependencies.pip` section

When the function is saved, the SDK parses a requirements file and normalizes the resulting list. If a package is specified without a version, the SDK looks for it in the active local virtual environment, adds the installed version when available, and logs a warning. Use an explicit version or version constraint to avoid this inference; pin an exact version for reproducible builds.

For `job` runs, a non-empty `requirements` list requires a build so that the dependencies are installed in the execution image. With the default `auto_build=True`, the runtime calls `function.build()` when `spec.image` is `None`. It does not rebuild when an image is already configured, even if requirements are present; after changing requirements, call `function.build()` explicitly or provide an image that already contains them.


## Action documentation

Review the detailed parameters for each Hydra action:

<div class="list-cards" markdown>

- [**Job**](actions/ray-job.md){ .list-card-link }

	Execute a Ray function as a one-off task in multirun mode.


- [**Build**](actions/ray-build.md){ .list-card-link }

	Build a container image for a Ray function.

</div>

## Examples

<div class="list-cards" markdown>

- [**Hydra examples**](examples.md){ .list-card-link }

	Explore complete examples for Ray jobs and builds.

</div>
