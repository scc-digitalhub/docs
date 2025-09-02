# ETL with digitalhub-core and DBT scenario introduction

Here we explore a proper, realistic scenario. We collect some data regarding organizations, analyze and transform it, then expose the resulting dataset.

Access Jupyter from your Coder instance and create a new notebook. Alternatively, the final notebook for this scenario can be found in the [tutorial repository](https://github.com/scc-digitalhub/digitalhub-tutorials/tree/main/s2-dbt).

## Setup

First, we initialize our environment and create a project.

Import required library:

```python
import digitalhub as dh
```

Create a project:

```python
project = dh.get_or_create_project("project-dbt-ci")
```

Check that the project has been created successfully:

```python
print(project)
```

## Set data source

The data we will use is available as a CSV file on GitHub. It is a generic sample table of employees.
The URL to the data is:

```python
url = "https://gist.githubusercontent.com/kevin336/acbb2271e66c10a5b73aacf82ca82784/raw/e38afe62e088394d61ed30884dd50a6826eee0a8/employees.csv"
```

We can now create a dataitem to represent the data source that we want to operate transformation on. The DBT runtime will use the dataitem specifications to fetch the data and perform the `transform` task on it.

To create the dataitem, we call the `new_dataitem` method of the project object. We pass the following mandatory parameters:

```python
di = project.new_dataitem(name="employees-dbt",
                          kind="table",
                          path=url)
```

The parameters are:

- `name` is the identifier of the dataitem.
- `kind` is the type of the dataitem (In this case, `table`, because our data is a table).
- `path` is the path to the data source.

Please note that the dataitem is not the data itself, but contains a reference to the data. The dataitem is a Core object that represents the data source, and it is stored in the Core backend. The data itself are (eventually) present on the path specified in the dataitem.

## Set up the function

We can now set up the function that operates a tranformation on data with DBT.
Our function will be an SQL query that selects all the employees of department 60.

```python
sql = """
WITH tab AS (
    SELECT  *
    FROM    {{ ref('employees') }}
)
SELECT  *
FROM    tab
WHERE   tab."DEPARTMENT_ID" = '50'
"""
```

We create the function from the project object:

```python
function = project.new_function(name="transform-employees",
                                kind="dbt",
                                code=sql)
```

The parameters are:

- `name` is the identifier of the function.
- `kind` is the type of the function. **Must be `dbt`**.
- `code` contains the code that is the SQL we'll execute in the function.

## Run the function

We can now run the function and see the results. To do this we use the `run` method of the function. To the method, we pass:

- the task we want to run (in this case, `transform`)
- the inputs map the refereced table in the DBT query (`{{ ref('employees') }}`) to one of our dataitems key. The Runtime will fetch the data and use dem as reference for the query.
- the output map the output table name. The name of the output table will be `department-50` and will be the sql query table name result and the output dataitem name.

```python
run = function.run("transform",
                   inputs={"employees": di.key},
                   outputs={"output_table": "department-50"},
                   wait=True)
```

We can check the status of the run:

```python
print(run.refresh().status)
```

If the status says `state: RUNNING`, wait some time and relaunch the refresh method. Once the function has finished (`state` should be `COMPLETED` or `ERROR`), we can inspect the results:

```python
print(run)
```

Note that calling `run.refresh()` will update the run object with the latest information from the Core backend.

## Explore the results

We can now explore the results of the function.
We can fetch the output table and explore it with `pandas`.

```python
df = run.output('department-50').as_df()
df.head()
```

In the next section, we will see how to convert this example in a workflow.
