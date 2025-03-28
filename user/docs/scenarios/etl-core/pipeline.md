# Workflow

We define a simple workflow, which will execute the ETL step:

```python
%%writefile "src/dbt_pipeline.py"

from digitalhub_runtime_kfp.dsl import pipeline_context

def myhandler(url):
    with pipeline_context() as pc:
        s1_dataset = pc.step(name="dbt",
                             function="function-dbt",
                             action="transform",
                             inputs={"employees":url},
                             outputs={"output_table": "department-50"})
```

Here in the definition we use a simple DSL to represent the execution of our functions as steps of the workflow. The DSL ``step`` method generates a KFP step that internally makes the remote execution of the corresponding job. Note that the syntax for step is similar to that of function execution.

Register the workflow:

```python
workflow = project.new_workflow(name="pipeline_dbt",
                                kind="kfp",
                                code_src="src/dbt_pipeline.py",
                                handler="myhandler")
```

You **MUST** build the workflow before running it. This is necessary to compose the Argo descriptor which will be used to execute the workflow:

```python
run_build = workflow.run("build", wait=True)
```

The Argo descriptor is saved as encoded base64 string into the workflow spec under the *build* attribute.
Once the workflow is built, you can run it, passing the URL key as a parameter:

```python
workflow.run("pipeline", parameters={"url": di.key}, wait=True)
```

It is possible to monitor the execution in the Core console.
