# Execution Overview

This section explains how to execute Hera workflows on the platform.
First, we list the workflow types and actions, then we examine the usage pattern.
Finally, we provide links to detailed documentation for each parameter category.

## Workflow types and Actions

There is one workflow kind in the Hera runtime:

- `hera`: Execute Hera workflows on Kubernetes

The kind supports specific actions.

| Workflow Kind | Supported Actions |
| --- | --- |
| `hera` | `build`, `pipeline` |

## Usage Pattern

To execute a Hera workflow, follow this pattern:

1. Implement a pipeline function that returns a Hera `Workflow` object (see [Pipeline definition](define-pipeline.md) for detailed instructions on creating pipeline functions).
2. Use `dh.new_workflow()` or `project.new_workflow()` to create the workflow, passing **workflow parameters**.
3. Call `workflow.run(action="build")` to build the pipeline definition (required).
4. Call `workflow.run(action="pipeline")` to execute the built pipeline, passing **task parameters** and **run parameters**.

```python
# Create workflow with workflow parameters
workflow = dh.new_workflow(
    name="my-workflow",
    kind="hera",
    code_src="pipeline.py",
    handler="pipeline"
)

# Build the pipeline
run_build = workflow.run(
    action="build"
)

# Execute the pipeline
run_pipeline = workflow.run(
    action="pipeline",
    parameters={"url": "https://example.com"}
)
```

Hera workflows are executed remotely on Kubernetes clusters managed by the platform.

## Parameter Documentation

Here are links to the detailed documentation for each Hera action:

- [Hera Build Action](actions/hera-build.md) — Build pipeline definition in Argo YAML format
- [Hera Pipeline Action](actions/hera-pipeline.md) — Execute the built pipeline on Kubernetes
