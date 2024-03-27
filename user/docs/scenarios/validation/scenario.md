# Validation with digitalhub-core and Nefertem scenario introduction

This scenario demonstrates how to use digitalhub-core and Nefertem to validate data.

Access Jupyter from your Coder instance and create a new notebook. If a Jupyter workspace isn't already available, create one from its template.

Open a new notebook using the **`digitalhub-core`** kernel.

We'll now start writing code. Copy the snippets of code from here and paste them in your notebook, then execute them with *Shift+Enter*. After running, Jupyter will create a new code cell.

The notebook file covering this scenario, as well as files for individual functions, are available in the `documentation/examples/validation`path within the repository of this documentation.

## Setup

First, we initialize our environment and create a project.

Import required library:

```python
import digitalhub as dh
```

Create a project:

```python
project = dh.get_or_create_project("project-nefertem")
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

We can now create a dataitem to represent the data source that we want to operate transformation on. The Nefertem runtime will use the dataitem specifications to fetch the data and perform the `validate` task on it.

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

We can now set up the function that operates a validation task on the dataitem.
First we define the *constraint* that we want to validate. A *constaint* is a rule that we wanto to check against the data. In this case, we want to check that the `SALARY` column is of type `int`. We define the *constraint* as a dictionary:

```python
constraint = {
  'constraint': 'type',
  'field': 'SALARY',
  'field_type': 'number',
  'name': 'check_value_integer',
  'title': '',
  'resources': ['employees'],
  'type': 'frictionless',
  'value': 'number',
  'weight': 5
}
```

With the *constraint* defined, we can now create the function from the project object. We pass the following parameters:

```python
function = project.new_function(name="function-nefertem",
                                kind="nefertem",
                                constraints=[constraint])
```

The parameters are:

- `name` is the identifier of the function.
- `kind` is the type of the function. **Must be `nefertem`**.
- `constraints` is the list of constraints that we want to validate.

## Run the function

We can now run the function and see the results. To do this we use the `run` method of the function. To the method, we pass:

- the task we want to run (in this case, `validate`)
- framework we want to use (in this case, `frictionless`)
- the inputs map the resource defined in the constraint with our dataitem key. The runtime will collect the data referenced in the dataitem path an treat that data as Nefertem `DataResource`.

```python
run = function.run("validate",
                   framework="frictionless",
                   inputs=[{"employees": di.key}])
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

We can now explore the results of the function. A Neferetem run produces various artifacts, like reports produced by Nefertem and the framework used for validation (in our case, a Frictionless report).
We can get the artifact list from the run:

```python
artifacts = run.outputs()


print(artifacts)
```

If we want to get the report, we can get it from the artifact and read it:

```python
path = artifacts[0]["run-metadata"].download()

with open(path) as f:
    print(f.read())
```
