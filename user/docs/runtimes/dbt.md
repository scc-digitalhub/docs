# DBT runtime

The DBT runtime allows you to run [DBT](https://www.getdbt.com/) transformations on your data. It is a wrapper around the DBT CLI tool.
The runtime introduces a function of kind `dbt` and a task of kind `transform`.

## Prerequisites

Python libraries:

- python 3.9 or 3.10
- digitalhub sdk
- dbt-postgres

We need first to install dbt:

```bash
pip install dbt-postgres==1.6.7 pandas==2.1.4
```

and then we can install digitalhub sdk and collect digitalhub dbt modules

```bash
git clone https://github.com/scc-digitalhub/digitalhub-sdk.git
cd digitalhub-sdk
pip install core/ data/ ./
pip install data/modules/dbt
```

If you want to exeute the dbt runtime only remotely, you can avoid to install dbt.

## Function

The DBT runtime introduces a function of kind `dbt` that allows you to execute sql dbt queries on your data.

### DBT function parameters

When you create a function of kind `dbt`, you need to specify the following mandatory parameters:

- **`project`**: the project name with which the function is associated. **Only** if you do not use the project context to create the function, e.g. `project.new_function()`.
- **`name`**: the name of the function
- **`kind`**: the kind of the function, **must** be `dbt`
- **`source`**: the source dictionary that contains the SQL query to run against the data

Optionally, you can specify the following parameters:

- **`uuid`**: the uuid of the function (this is automatically generated if not provided). **Must** be a valid uuid v4.
- **`description`**: the description of the function
- **`labels`**: the labels of the function
- **`git_source`**: the remote source of the function (git repository)
- **`embedded`**: whether the function is embedded or not. If `True`, the function is embedded (all the details are expressed) in the project. If `False`, the function is not embedded in the project.

For example:

```python
import digitalhub as dh

project = dh.get_or_create_project('my_project')

sql = """
SELECT * FROM {{ ref('my_table') }}
"""

dataitem = project.new_dataitem("my_dataitem", kind="table", path="path-to-some-data")

function = dh.new_function(
    kind='dbt',
    name='my_function',
    source={"code": sql}
)
```

## Task

The DBT runtime introduces a task of kind `transform` that allows you to run a DBT transformation on your data.

### Transform task parameters

When you want to execute a task of kind `transform`, you need to pass the following mandatory parameters to the function method `run()`:

- **`action`**: the action to perform. This must be `transform`.
- **`inputs`**: the list of referenced tables in the sql query mapped to the dataitem keys.
- **`outputs`**: a list containing **one** element that map the key `output_table` with a name of the output query table and output dataitem.

As optional, you can pass the following task parameters specific for remote execution:

- **`node_selector`**: a list of node selectors. The runtime will select the nodes to which the task will be scheduled.
- **`volumes`**: a list of volumes
- **`resources`**: a list of resources (CPU, memory, GPU)
- **`labels`**: a list of labels to attach to kubernetes resources
- **`affinity`**: node affinity
- **`tolerations`**: tolerations
- **`env`**: environment variables to inject in the container
- **`secrets`**: list of secrets to inject in the container
- **`backoff_limit`**: the number of retries when a job fails.
- **`schedule`**: the schedule of the job as a cron expression
- **`replicas`**: the number of replicas of the deployment

For example:

```python
run = function.run(
    action='transform',
    inputs=[{"my_table": my_dataitem.key}],
    outputs=[{"output_table": "my_output_table"}],
)
```

## Runtime workflow

The DBT runtime execution workflow is the following:

1. The runtime fetches the input dataitems by downloading them locally. The runtime tries to get the file from the `path` attribute in the dataitem specification. At the moment, we support the following path types:
     - `http(s)://<url>`
     - `s3://<bucket>/<path>`
     - `sql://<database>(/<schema-optional>)/<table>`
     - `<local-path>`
2. The runtime inserts the data into a temporary versioned table in the default postgres database. These tables are named `<dataitem-name>_v<dataitem-id>`, and will be deleted at the end of the execution.
3. The runtime creates all the necessary DBT artifacts (profiles.yml, dbt_project.yml, etc.) and runs the DBT transformation.
4. The runtime stores the output table into the default postgres database as result of the DBT execution. The table name is built from the `outputs` parameter. Then, the runtime creates a dataitem with the `outputs` name parameter and saves it into the Core backend. You can retrieve the dataitem with the `run.outputs()` method. In general, the output table versioned is named `<dataitem-output-name>_v<dataitem-output-id>` and is stored in the default postgres database passed to the runtime via env variable.

## Snippet example

```python
import digitalhub as dh

# Get or create project
project = dh.get_or_create_project("project-dbt")

# Create new input dataitem
url = "https://gist.githubusercontent.com/kevin336/acbb2271e66c10a5b73aacf82ca82784/raw/e38afe62e088394d61ed30884dd50a6826eee0a8/employees.csv"
di = project.new_dataitem(name="employees",
                          kind="table",
                          path=url)

# Create new function
sql = """
WITH tab AS (
    SELECT  *
    FROM    {{ ref('employees') }}
)
SELECT  *
FROM    tab
WHERE   tab."DEPARTMENT_ID" = '60'
"""
function = project.new_function(name="function-dbt",
                                kind="dbt",
                                source={"code": sql})

# Run function
run = function.run("transform",
                   inputs=[{"employees": di.key}],
                   outputs=[{"output_table": "department-60"}])

# Refresh run
run.refresh()
```
