# ETL with digitalhub-core and DBT scenario introduction

Here we explore a proper, realistic scenario. We collect some data regarding organizations, analyze and transform it, then expose the resulting dataset.

Access Jupyter from your Coder instance and create a new notebook. If a Jupyter workspace isn't already available, create one from its template.

Open a new notebook using the **`digitalhub-core`** kernel.

We'll now start writing code. Copy the snippets of code from here and paste them in your notebook, then execute them with *Shift+Enter*. After running, Jupyter will create a new code cell.

The notebook file covering this scenario, as well as files for individual functions, are available in the `documentation/examples/etl-core` path within the repository of this documentation.

## Setup

First, we initialize our environment and create a project.

Import required libraries:

Import required library:

```python
import digitalhub_core as dhcore
```

Create a project:

``` python
project = dhcore.get_or_create_project("project-dbt")
```

Check that the project has been created successfully:

``` python
print(project)
```

## Set data source

The data we will use is available as a CSV file on GitHub. It is a table of organizations, with columns for the organization name, country, and city.
The URL to the data is:

```python
url = "https://media.githubusercontent.com/media/datablist/sample-csv-files/main/files/organizations/organizations-1000.csv"
```

We can now create a dataitem to represent the data source that we want to operate transformation on. The DBT runtime will use the dataitem specifications to fetch the data and perform the `transform` task on it.

To create the dataitem, we call the `new_dataitem` method of the project object. We pass the following mandatory parameters:

```python
di = project.new_dataitem(name="organizations",
                          kind="dataitem",
                          path=url)
```

The parameters are:

- `name` is the identifier of the dataitem.
- `kind` is the type of the dataitem (at the moment we support only *dataitem* as kind)
- `path` is the path to the data source.

Please note that the dataitem is not the data itself, but contains a reference to the data. The dataitem is a Core object that represents the data source, and it is stored in the Core backend. The data itself are (eventually) present on the path specified in the dataitem.

## Set up the function

We can now set up the function that operates a tranformation on data with DBT.
Our function will be an SQL query that selects all the organizations from Algeria.

``` python
sql = """
WITH tab AS (
    SELECT  *
    FROM    {{ ref('organizations') }}
)
SELECT  *
FROM    tab
WHERE   tab."Country" = 'Algeria'
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
- the output dataitem (in this case, `algerian-organizations`) in the form of a dictionary with the key `dataitems` and the value a list of dataitem names. The output dataitem name must be only one, because the DBT runtime produces only one output table

``` python
run = function.run("transform",
                   inputs={"dataitems": ["organizations"]},
                   outputs={"dataitems": ["algerian-organizations"]})
```

We can check the status of the run:

```python
print(run.refresh().status)
```

If the status says `state: RUNNING`, wait some time and relaunch the refresh method. Once the function has finished (`state` should be `COMPLETED` or `ERRROR`), we can inspect the results:

```python
print(run)
```

Note that calling run.refresh() will update the run object with the latest information from the Core backend.

## Explore the results

We can now explore the results of the function.
First, we get the dataitem that was created during execution:

``` python
out_di = run.get_dataitems("algerian-organizations")
```

Then we can import the dataitem as a Pandas dataframe:

``` python
df = out_di.as_df()
```

We can now explore the dataframe:

``` python
df.head()
```
