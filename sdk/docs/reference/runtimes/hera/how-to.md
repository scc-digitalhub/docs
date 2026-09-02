# Execution Overview

This section explains how to build and execute Hera workflows with the platform SDK.
First, we list the workflow type and actions, then we examine the supported usage pattern.
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
2. Use `dh.new_workflow()` or `project.new_workflow()` to create the workflow. Declare Hera workflow parameters inside the returned Hera `Workflow` object in the source code.
3. Call `workflow.run(action="pipeline", auto_build=True)` to build the workflow when needed and execute it. The `parameters` mapping contains values for the Hera workflow parameters declared in the source.
4. To separate build and execution, call `workflow.build()` first and then `workflow.run(action="pipeline", auto_build=False)`. The pipeline run is submitted to the remote platform process.

```python
# Create the workflow entity. Hera workflow parameters are declared in pipeline.py.
workflow = dh.new_workflow(
    name="my-workflow",
    kind="hera",
    code_src="pipeline.py",
    handler="pipeline"
)

# Build the workflow automatically, pass its workflow parameter, and wait for execution
run_pipeline = workflow.run(
    action="pipeline",
    auto_build=True,
    parameters={"url": "https://example.com"},
    wait=True,
)
```

For an explicit two-step flow:

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

## Parameter Documentation

Here are links to the detailed documentation for each Hera action:

- [Hera Build Action](actions/hera-build.md) — Build pipeline definition in Argo YAML format
- [Hera Pipeline Action](actions/hera-pipeline.md) — Execute the built pipeline on the platform
