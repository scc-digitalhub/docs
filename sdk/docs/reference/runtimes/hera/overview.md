# Hera Runtime

The Hera runtime enables running Hera workflows on the platform. It defines Workflow objects of kind `hera` and supports `build` and `pipeline` task actions for workflow execution.

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
2. Use `dh.new_workflow()` or `project.new_workflow()` to create the workflow entity.
3. Build the pipeline by calling `workflow.run(action="build")` (required).
4. Execute the pipeline with `workflow.run(action="pipeline")`; a stepper will execute the Hera steps.

The runtime provides DSL helpers in `digitalhub_runtime_hera.dsl`. Use `step` and `container_template` to wrap digitalhub functions and workflows into Hera steps and container templates. The DSL supports both `DAG` and `Steps` contexts.

Core components:

- `step`: defines an individual workflow step inside a `DAG` or `Steps` context; it represents a task and can declare inputs, outputs and parameters.
- `container_template`: constructs a Hera container template (image, command, args). It is used by `step` and also available for advanced custom templates.

See [how to](how-to.md) for detailed instructions on building and executing Hera workflows.
See [Examples](examples.md) for code samples.
