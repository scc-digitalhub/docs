# Workflow

We define a simple workflow, which will execute the ETL step:

```python
%%writefile "src/dbt_pipeline.py"

from digitalhub_runtime_hera.dsl import step
from hera.workflows import DAG, Parameter, Workflow


def pipeline():
    with Workflow(entrypoint="dag", arguments=Parameter(name="employees")) as w:
        with DAG(name="dag"):
            A = step(
                template={
                    "action": "transform",
                    "inputs": {"employees": "{{workflow.parameters.employees}}"},
                    "outputs": {"output_table": "department-50"},
                },
                function="transform-employees",
            )
    return w
```

Here we use the Hera-based DSL to represent the execution of our functions as steps of the workflow. The DSL ``step`` method maps to Hera templates and produces an Argo workflow descriptor which performs the remote execution of the corresponding job. Note that the syntax for ``step`` is similar to that of function execution.

Register the workflow:

```python
workflow = project.new_workflow(name="pipeline_dbt",
                                kind="hera",
                                code_src="src/dbt_pipeline.py",
                                handler="pipeline")
```

You **MUST** build the workflow before running it. This is necessary to compose the Argo descriptor which will be used to execute the workflow:

```python
run_build = workflow.run("build", wait=True)
```

The Argo descriptor is saved as encoded base64 string into the workflow spec under the *build* attribute.
Once the workflow is built, you can run it, passing the URL key as a parameter:

```python
workflow.run("pipeline", parameters={"employees": di.key}, wait=True)
```

It is possible to monitor the execution in the Core console.
