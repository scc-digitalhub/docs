# Hera runtime

The Hera runtime defines Workflow objects of kind `hera` and supports `build` and `pipeline` actions for workflow execution on Kubernetes.

## Prerequisites

| Requirement | Details |
| --- | --- |
| Python | >= 3.10, < 3.15 |
| Package | `digitalhub-runtime-hera` |

## Usage pattern

To execute a Hera workflow, follow this pattern:

1. Implement a pipeline function that returns a Hera `Workflow` object (see [Pipeline definition](define-pipeline.md) for detailed instructions on creating pipeline functions).
2. Use `dh.new_workflow()` or `project.new_workflow()` to create the workflow. Declare Hera workflow parameters inside the returned Hera `Workflow` object in the source code.
3. Call `workflow.run(action="pipeline", auto_build=True)` to build the workflow when needed and execute it. The `parameters` mapping contains values for the Hera workflow parameters declared in the source.

??? example "Build and run a Hera workflow"

	```python
	workflow = dh.new_workflow(
		name="my-workflow",
		kind="hera",
		code_src="pipeline.py",
		handler="pipeline"
	)

	run_pipeline = workflow.run(
		action="pipeline",
		auto_build=True,
		parameters={"url": "https://example.com"},
		wait=True,
	)
	```

To separate compilation from execution, call `workflow.build()` first and then run `workflow.run(action="pipeline", auto_build=False)`. Hera is used by the remote process that builds and runs the workflow; it is not required in the client environment.

??? example "Build and run in two steps"

	```python
	run_build = workflow.build(wait=True)
	run_pipeline = workflow.run(
		action="pipeline",
		auto_build=False,
		parameters={"url": "https://example.com"},
		wait=True,
	)
	```

The build run returns the generated Argo Workflows YAML as a base64-encoded value under `run_build.results()["workflow"]`.

## DSL helpers

The runtime provides DSL helpers in `digitalhub_runtime_hera.dsl`. Use `step` and `container_template` to wrap DigitalHub functions into Hera steps and container templates. The DSL supports both `DAG` and `Steps` contexts. Both helpers require the `DHCORE_WORKFLOW_IMAGE` environment variable, which supplies the stepper image.

Core components:

- `step`: defines an individual workflow step inside a `DAG` or `Steps` context; it returns a Hera `Task` in a `DAG` and a Hera `Step` in `Steps`, and can declare inputs and outputs.
- `container_template`: constructs a Hera container template (image, command, args). It is used by `step` and also available for advanced custom templates.

## Action documentation

Review the detailed parameters for each Hera action:

<div class="list-cards" markdown>

- [**Build**](actions/hera-build.md){ .list-card-link }

	Build a pipeline definition in Argo YAML format.

- [**Pipeline**](actions/hera-pipeline.md){ .list-card-link }

	Execute a built pipeline on the platform.

</div>

## Examples

<div class="list-cards" markdown>

- [**Hera examples**](examples.md){ .list-card-link }

	Explore complete examples for building and executing Hera workflows.

</div>
