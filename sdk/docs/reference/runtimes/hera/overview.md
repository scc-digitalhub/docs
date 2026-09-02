# Hera Runtime

The Hera runtime defines Workflow objects of kind `hera` and supports the `build` and `pipeline` task actions for workflow execution.

- **`hera`**: Execute Hera workflows on Kubernetes

## Prerequisites

**Supported Python versions:**

- Python ≥ 3.10, < 3.15

**Required packages:**

- `digitalhub-runtime-hera`

Install from PyPI:

```bash
pip install digitalhub-runtime-hera
```

## Usage overview

To execute Hera workflows on the platform:

1. Implement a pipeline function that returns a Hera `Workflow` object (see [Pipeline definition](define-pipeline.md) for detailed instructions on creating pipeline functions).
2. Use `dh.new_workflow()` or `project.new_workflow()` to create the workflow entity. The source must provide a handler and one of `code_src`, `code` or `base64`.
3. Execute the pipeline with `workflow.run(action="pipeline", auto_build=True)`. `WorkflowHera.run()` builds the workflow automatically when `workflow.spec.workflow` is `None`.
4. To separate compilation from execution, call `workflow.build()` first and then run `workflow.run(action="pipeline", auto_build=False)`. Hera is used by the remote process that builds and runs the workflow; it is not required in the client environment.

The runtime provides DSL helpers in `digitalhub_runtime_hera.dsl`. Use `step` and `container_template` to wrap DigitalHub functions into Hera steps and container templates. The DSL supports both `DAG` and `Steps` contexts. Both helpers require the `DHCORE_WORKFLOW_IMAGE` environment variable, which supplies the stepper image.

Core components:

- `step`: defines an individual workflow step inside a `DAG` or `Steps` context; it returns a Hera `Task` in a `DAG` and a Hera `Step` in `Steps`, and can declare inputs and outputs.
- `container_template`: constructs a Hera container template (image, command, args). It is used by `step` and also available for advanced custom templates.

See [how to](how-to.md) for detailed instructions on building and executing Hera workflows.
See [Examples](examples.md) for code samples.
