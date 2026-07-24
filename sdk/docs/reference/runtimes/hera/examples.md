# Examples

## Pipeline Definition Example

```python
from hera.workflows import Workflow, DAG, Parameter
from digitalhub_runtime_hera.dsl import step

def pipeline():
    # Create a new Workflow with an entrypoint DAG and a parameter
    with Workflow(entrypoint="dag", arguments=Parameter(name="url")) as w:
        with DAG(name="dag"):
            # First step: takes the workflow parameter and outputs a dataset
            A = step(template={"action":"job", "inputs": {"url": "{{workflow.parameters.url}}"}},
                     function="download-data",
                     outputs=["dataset"])

            # Subsequent steps consume A's output
            B = step(template={"action":"job", "inputs": {"di": "{{inputs.parameters.di}}"}},
                     function="process-spire",
                     inputs={"di": A.get_parameter("dataset")})

            C = step(template={"action":"job", "inputs": {"di": "{{inputs.parameters.di}}"}},
                     function="process-measures",
                     inputs={"di": A.get_parameter("dataset")})

            # Chain the steps
            A >> [B, C]

    return w
```

## Workflow Creation Example

```python
import digitalhub as dh

project = dh.get_or_create_project("my_project")

# From project
workflow = project.new_workflow(
    name="workflow",
    kind="hera",
    code_src="pipeline.py",
    handler="pipeline"
)

# Or from sdk
workflow = dh.new_workflow(
    project="my-project",
    name="workflow",
    kind="hera",
    code_src="pipeline.py",
    handler="pipeline"
)
```

## Run Examples

```python
# Build the pipeline
run_build = workflow.run(
    action="build"
)

# Execute the pipeline
run_pipeline = workflow.run(action="pipeline")
```

## Tutorials

Find additional examples in the [tutorial repository](https://github.com/scc-digitalhub/digitalhub-tutorials) of the DSLab GitHub organization.
