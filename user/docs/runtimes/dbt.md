# DBT runtime

The **DBT runtime** allows you to run [DBT](https://www.getdbt.com/) transformations on your data. It is a wrapper around the DBT CLI tool.
The runtime introduces a function of kind `dbt` and a task of kind `transform`.

## Prerequisites

Python version and libraries:

- `python >= 3.9`
- `digitalhub-runtime-dbt`

The package is available on PyPI:

```bash
python -m pip install digitalhub-runtime-dbt # for remote execution only
python -m pip install digitalhub-runtime-dbt[local] # for local execution
```

## HOW TO

With the DBT runtime you can use the function's `run()` method to execute a DBT query you have defined.
The DBT runtime execution workflow follows roughly these steps:

1. The runtime fetches the input dataitems by downloading them locally. The runtime tries to get the file from the `path` attribute in the dataitem specification. At the moment, we support the following path types:
     - `http(s)://<url>`
     - `s3://<bucket>/<path>`
     - `sql://<database>(/<schema-optional>)/<table>`
     - `<local-path>`
2. The runtime inserts the data into a temporary versioned table in the default postgres database. These tables are named `<dataitem-name>_v<dataitem-id>`, and will be deleted at the end of the execution.
3. The runtime collect the source code of the DBT query and creates all the necessary DBT artifacts (profiles.yml, dbt_project.yml, etc.) and runs the DBT transformation.
4. The runtime stores the output table into the default postgres database as result of the DBT execution. The table name is built from the `outputs` parameter. Then, the runtime creates a dataitem with the `outputs` name parameter and saves it into the Core backend. You can retrieve the dataitem with the `run.outputs()` method. In general, the output table versioned is named `<dataitem-output-name>_v<dataitem-output-id>` and is stored in the default postgres database passed to the runtime via env variable.

### Source code

You can define a DBT query as usual, and store it in several ways.
You will then refernce the source code according to a specific `Function` parameter as shown in the following table:

| Format | Parameter | Type | Example |
| --- | --- | --- | --- |
| remote git repository | source | `str` | "git+https://github.com/some-user/some-repo" |
| zip s3 archive | source | `str` | "zip+s3://some-bucket/some-key.zip" |
| base64 encoded string | base64 | `str` | "encodedstring" |
| string | code | `str` | "select * from some_table" |

### Function

The DBT runtime introduces a function of kind `dbt` that allows you to execute sql dbt queries on your data.

#### Function parameters

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| project | str | Project name | required (if creating from library) |
| name | str | Name that identifies the object | required |
| kind | str | Kind of the object | required (must be `dbt`) |
| uuid | str | ID of the object in form of UUID | None |
| description | str | Description of the object | None |
| git_source | str | Remote git source for object | None |
| labels | list[str] | List of labels | None |
| embedded | bool | Flag to determine if object must be embedded in project | True |
| [code_src](#source) | str | URI pointer to source code | None |
| code | str | Source code (plain text)| None |
| base64 | str | Source code (base64 encoded)| None |
| handler | str | Function entrypoint | None |
| lang | str | Source code language (hint)| None |

##### Source

Source code can be specified with `code_src` as an URI. It can have three different type of schema:

| schema | value | description |
| --- | --- | --- |
| None | "path/to/file.ext" | Local file path |
| git+https | "git+https://github.com/some-user/some-repo" | Remote git repository |
| zip+s3 | "zip+s3://some-bucket/some-key.zip" | Remote zip s3 archive |

#### Function example

```python
import digitalhub as dh

project = dh.get_or_create_project("my_project")

sql = """
SELECT * FROM {{ ref("my_table") }}
"""

dataitem = project.new_dataitem("my_dataitem", kind="table", path="path-to-some-data")

function = dh.new_function(
    kind="dbt",
    name="my_function",
    source={"code": sql}
)
```

### Task

The DBT runtime introduces a task of kind `transform` that allows you to run a DBT transformation on your data.
A `Task` is created with the `run()` method, so it's not managed directly by the user. The parameters for the task creation are passed directly to the `run()` method, and may vary depending on the kind of task.

#### Task parameters

| Name | Type | Description | Default | Kind specific |
| --- | --- | --- | --- | --- |
| action | str | Task action. Must be one of: <li>`transform`</li> | required | |
| [node_selector](../tasks/kubernetes-resources.md#node_selector) | list[dict] | Node selector | None | |
| [volumes](../tasks/kubernetes-resources.md#volumes) | list[dict] | List of volumes | None | |
| [resources](../tasks/kubernetes-resources.md#resources) | dict | Resources restrictions | None | |
| [affinity](../tasks/kubernetes-resources.md#affinity) | dict | Affinity | None | |
| [tolerations](../tasks/kubernetes-resources.md#tolerations) | list[dict] | Tolerations | None | |
| [envs](../tasks/kubernetes-resources.md#envs) | list[dict] | Env variables | None | |
| [secrets](../tasks/kubernetes-resources.md#secrets) | list[str] | List of secret names | None | |

#### Task example

```python
run = function.run(
    action="transform",
    inputs={"my_table": my_dataitem.key},
    outputs={"output_table": "my_output_table"},
)
```

### Run

The `Run` object is, similar to the `Task`, created with the `run()` method.
The run's parameters are passed alongside the task's ones.

#### Run parameters

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| loacal_execution | bool | Flag to indicate if the run will be executed locally | False |
| inputs | dict | Input entity key. | None |
| outputs | dict | Outputs mapped. | None |
| parameters | dict | Extra parameters for a function. | None |

#### Run example

```python
run = function.run(
    action="job",
    inputs={
        "dataitem": dataitem.key
    },
    outputs={
        "dataitem": "mapped-name",
        "label": "some-label"
    }
)
```

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
    FROM    {{ ref("employees") }}
)
SELECT  *
FROM    tab
WHERE   tab."DEPARTMENT_ID" = "60"
"""
function = project.new_function(name="function-dbt",
                                kind="dbt",
                                source={"code": sql})

# Run function
run = function.run("transform",
                   inputs={"employees": di.key},
                   outputs={"output_table": "department-60"})

# Refresh run
run.refresh()
```
