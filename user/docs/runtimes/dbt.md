# DBT runtime

The DBT runtime allows you to run [DBT](https://www.getdbt.com/) transformations on your data. It is a wrapper around the DBT CLI tool.
The runtime introduces a function of kind `dbt` and a task of kind `transform`.

## Prerequisites

Python libraries:

- python >= 3.9
- digitalhub-core
- digitalhub-core-dbt

If you want to execute DBT transformation locally, you need to install digitalhub-core-dbt with `local` flag:

```bash
pip install digitalhub-core-dbt[local]
```

Otherwise, only remote execution with Core backed available is possible.

## Function

The DBT runtime introduces a function of kind `dbt` that allows you to execute sql dbt queries on your data.

### DBT function parameters

When you create a function of kind `dbt`, you need to specify the following mandatory parameters:

- **`project`**: the project name with which the function is associated. **Only** if you do not use the project context to create the function, e.g. `project.new_function()`.
- **`name`**: the name of the function
- **`kind`**: the kind of the function, **must** be `dbt`
- **`sql`**: the SQL query to run against the data

Optionally, you can specify the following parameters:

- **`uuid`**: the uuid of the function (this is automatically generated if not provided). **Must** be a valid uuid v4.
- **`description`**: the description of the function
- **`labels`**: the labels of the function
- **`source_remote`**: the remote source of the function (git repository)
- **`source_code`**: pointer to the source code of the function
- **`embedded`**: whether the function is embedded or not. If `True`, the function is embedded (all the details are expressed) in the project. If `False`, the function is not embedded in the project.

For example:

```python
import digitalhub_core as dhcore

sql = """
SELECT * FROM {{ ref('my_table') }}
"""

function = dhcore.new_function(
    kind='dbt',
    name='my_function',
    sql=sql
)
```

## Task

The DBT runtime introduces a task of kind `transform` that allows you to run a DBT transformation on your data.

### Transform task parameters

When you want to execute a task of kind `transform`, you need to pass the following mandatory parameters to the function method `run()`:

- **`action`**: the action to perform. This must be `transform`.
- **`inputs`**: the list of **dataitem names** used as input for the transformation. The corresponding dataitem objects must be present in the backend, whether it's local or Core backend.
- **`outputs`**: a list containing **one** element that represents the output table name. A dataitem with that name will be created by the runtime if the transformation is successful.

For example:

```python
run = function.run(
    action='transform',
    inputs={"dataitems": ["my_table"]},
    outputs={"dataitems": ["my_output_table"]},
)
```

## Runtime workflow

The DBT runtime execution workflow is the following:

1. The runtime fetches the input dataitems by downloading them locally. The runtime tries to get the file from the `path` attribute. At the moment, we support the following path types:
     - `http(s)://<url>`
     - `s3://<bucket>/<path>`
     - `sql://<database>(/<schema-optional>)/<table>`
     - `<local-path>`
2. The runtime inserts the data into a temporary versioned table in the default postgres database. These tables are named `<dataitem-name>_v<dataitem-id>`, and will be deleted at the end of the execution.
3. The runtime creates all the necessary DBT artifacts (profiles.yml, dbt_project.yml, etc.) and runs the DBT transformation.
4. The runtime stores the output table into the default postgres database as result of the DBT execution. The table name is built from the `outputs` parameter. Then, the runtime creates a dataitem with the `outputs` name parameter and saves it into the Core backend. You can retrieve the dataitem with the `run.get_dataitem()` method. In general, the output table is named `<dataitem-output-name>_v<dataitem-output-id>` and is stored in the default postgres database passed to the runtime via env variable.

## Snippet example

```python
import digitalhub_core as dhcore

# Get or create project
project = dhcore.get_or_create_project("project-dbt")

# Create new input dataitem
url = "https://media.githubusercontent.com/media/datablist/sample-csv-files/main/files/organizations/organizations-1000.csv"
di = project.new_dataitem(name="organizations",
                          kind="dataitem",
                          path=url)

# Create new function
sql = """
WITH tab AS (
    SELECT  *
    FROM    {{ ref('organizations') }}
)
SELECT  *
FROM    tab
WHERE   tab."Country" = 'Algeria'
"""
function = project.new_function(name="algerian-organizations",
                                kind="dbt",
                                sql=sql)

# Run function
run = function.run("transform",
                   inputs={"dataitems": ["organizations"]},
                   outputs={"dataitems": ["algerian-organizations"]})
```
