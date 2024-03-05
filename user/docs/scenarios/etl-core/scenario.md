# ETL with digitalhub-core and DBT scenario introduction

Here we explore a proper, realistic scenario. We collect some data regarding organizations, analyze and transform it, then expose the resulting dataset.

Access Jupyter from your Coder instance and create a new notebook. If a Jupyter workspace isn't already available, create one from its template.

Open a new notebook using the **`digitalhub-core`** kernel.

We'll now start writing code. Copy the snippets of code from here and paste them in your notebook, then execute them with *Shift+Enter*. After running, Jupyter will create a new code cell.

The notebook file covering this scenario, as well as files for individual functions, is available in the `documentation/examples/etl-core` path within the repository of this documentation, or in the path `tutorials/08-dbt-demo.ipynb` of the Jupyter instance.

## Setup

First, we initialize our environment and create a project.

Import required library:

```python
import digitalhub as dh
```

Create a project:

``` python
project = dh.get_or_create_project("project-dbt")
```

Check that the project has been created successfully:

``` python
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
di = project.new_dataitem(name="employees",
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

``` python
sql = """
WITH tab AS (
    SELECT  *
    FROM    {{ ref('employees') }}
)
SELECT  *
FROM    tab
WHERE   tab."DEPARTMENT_ID" = '60'
"""
```

We create the function from the project object:

``` python
function = project.new_function(name="function-dbt",
                                kind="dbt",
                                sql=sql)
```

The parameters are:

- `name` is the identifier of the function.
- `kind` is the type of the function. **Must be `dbt`**.
- `sql` is the SQL query that will be executed by the function.

## Run the function

We can now run the function and see the results. To do this we use the `run` method of the function. To the method, we pass:

- the task we want to run (in this case, `transform`)
- the input dataitem(s) (in this case, `organizations`) in the form of a dictionary with the key `dataitems` and the value a list of dataitem names
- the output dataitem (in our case, `department-60`) in the form of a dictionary with the key `dataitems` and the value a list of dataitem names. The output dataitem name must be only one, because the DBT runtime produces only one output table

``` python
run = function.run("transform",
                   inputs={"dataitems": ["employees"]},
                   outputs={"dataitems": ["department-60"]})
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
First, we get the dataitem that was created during execution:

``` python
outputs = run.results()
out_di = outputs.get_dataitem_by_key("department-60")
```

Then we can import the dataitem as a Pandas dataframe:

``` python
df = out_di.as_df()
```

We can now explore the dataframe:

``` python
df.head()
```
