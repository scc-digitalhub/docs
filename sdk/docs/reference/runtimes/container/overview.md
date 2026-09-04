# Container runtime

The Container runtime enables launching pods, jobs and services on Kubernetes with custom images, commands and dependencies.

## Prerequisites

| Requirement | Details |
| --- | --- |
| Python | >= 3.10, < 3.15 |
| Package | `digitalhub-runtime-container` |

## Usage pattern

To execute a container workload, follow this pattern:

1. Use `dh.new_function()` or `project.new_function()` to create the function, passing function parameters.
2. Call `function.run()` with the desired action, passing task parameters and run parameters.

??? example "Create and run a container job"

	```python
	# Create function with function parameters
	function = dh.new_function(
		name="my-function",
		kind="container",
		image="my-image:latest",
		command="my-command"
	)

	# Execute with task and run parameters
	run = function.run(
		action="job",
		args=["arg1", "arg2"]
	)
	```

When a job or service needs additional dependencies, build the execution image before launching it. Configure the base image and the target image on the same `Function`, run `build()` with the required instructions, and then use that function for the `job` or `serve` run.

??? example "Build and run with dependencies"

	```python
	function = dh.new_function(
		name="my-function",
		kind="container",
		image="registry.example.com/my-function:latest",
		base_image="python:3.11-slim",
		command="python app.py"
	)

	function.build(
		instructions=["pip install numpy pandas"]
	)

	run = function.run(
		action="job",
		args=["input.csv"]
	)
	```

Use `action="serve"` instead of `action="job"` when the built image must run as a long-lived service. The `build()` and `run()` calls operate on the same `Function`.

Container functions are executed remotely on Kubernetes clusters managed by the platform.

## Action documentation

Review the detailed parameters for each container action:

<div class="list-cards" markdown>

- [**Job**](actions/container-job.md){ .list-card-link }

	Execute a container as a one-off job.

- [**Serve**](actions/container-serve.md){ .list-card-link }

	Deploy a container as a long-lived service.

- [**Build**](actions/container-build.md){ .list-card-link }

	Create a Docker image with custom instructions.

</div>

## Examples

<div class="list-cards" markdown>

- [**Container examples**](examples.md){ .list-card-link }

	Explore complete examples for container jobs, builds and services.

</div>
