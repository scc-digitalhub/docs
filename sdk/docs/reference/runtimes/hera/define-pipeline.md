# Define a Hera Pipeline

This section describes how to define a Hera pipeline function. A pipeline function is a Python function that returns a Hera `Workflow` object. The function must not accept arguments; define workflow parameters inside the returned Hera `Workflow` object instead.

## Pipeline Function Anatomy

Define a pipeline by creating a Python function that returns a Hera `Workflow` object:

```python
from hera.workflows import Workflow, DAG, Parameter
from digitalhub_runtime_hera.dsl import step

def pipeline():
    # Create a new Workflow with an entrypoint DAG and parameters
    with Workflow(entrypoint="dag", arguments=Parameter(name="url")) as w:
        with DAG(name="dag"):
            # Define workflow steps here
            ...
    return w
```

## Typical Pipeline Structure

1. Create a `Workflow` Hera object and set the entrypoint (usually a DAG).
2. Use a `DAG` or `Steps` context to define the workflow structure.
3. Add steps via `step(...)`, providing templates, function names, inputs/outputs and parameters.
4. Chain steps using Hera operators to define dependencies.
5. Return the `Workflow` Hera object.

## DSL Components

The runtime provides DSL helpers in `digitalhub_runtime_hera.dsl`:

### `step` function

`step(**step_kwargs)` creates a workflow step inside a DAG or Steps context. It returns a Hera `Task` inside a `DAG` and a Hera `Step` inside `Steps`. Main arguments:

| Parameter | Type | Example | Description |
| --- | --- | --- | --- |
| template | dict | {"action": "job"} | Parameters template to pass to the DigitalHub function run. The `action` key is required. To pass inputs from other steps use the `{{inputs.parameters.parameter_name}}` template syntax. |
| function | str | "download-data" | Name of the DigitalHub function to execute. |
| function_id | str | "abc123" | Function ID (optional). |
| name | str | "step1" | Step name. |
| [inputs](#step-inputs-and-outputs) | dict | {"some-input": ANOTHER_STEP.get_parameter("some-output")} | Step inputs. Keys become Hera Parameters; values can reference other steps' outputs. |
| [outputs](#step-inputs-and-outputs) | list | ["output1"] | Step outputs. These become Hera Outputs and Artifacts. |

Other keyword arguments are forwarded to the underlying container template. `step` must be called inside a `DAG` or `Steps` context. The function is resolved when the workflow is built, and `DHCORE_WORKFLOW_IMAGE` must be set to create the container template.

#### Step Inputs and Outputs

Step inputs are defined via the `inputs` argument to `step(...)`. This is a dictionary where keys are input names and values can reference outputs from other steps using the `get_parameter(...)` method. For example:

```python

# Here the step A (let say a python function) produces an output named "data"
A = step(template={"action":"job"}, function="step-a", outputs=["data"])

# Step B consumes the output "data" from step A as its input. Because "data" is an output of step A, we use A.get_parameter("data") to reference it. Note that the input name "input_data" in step B can be different from the output name "data" in step A.
# In the template of step B, we use the template syntax {{inputs.parameters.data-from-b}} to refer to the input parameter.
# The "inputs" provided in template of step B belongs to the spec of the function "step-b", in this case a python function.
B = step(template={"action":"job", "inputs": {"parameter-name": "{{inputs.parameters.data-from-b}}"}}, function="step-b", inputs={"data-from-b": A.get_parameter("data")})
```

### `container_template` function

`container_template(...)` builds a Hera container template for a workflow step. It returns a Hera `Container` object and requires `template` and `function`. Unlike `step`, its `inputs` argument is a list of input names. Use it directly for advanced scenarios or custom templates. `DHCORE_WORKFLOW_IMAGE` must be set; the value is used as the stepper image.

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
