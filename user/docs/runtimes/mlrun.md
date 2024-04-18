# Mlrun runtime

The mlrun runtime allows you to execute [mlrun](https://www.mlrun.com/) function. It's a wrapper around mlrun methods.
The runtime introduces a function of kind `mlrun` and a task of kind `job`.

## Prerequisites

Python libraries:

- python 3.9 or 3.10
- digitalhub sdk
- mlrun

We need first to collect digitalhub mlrun modules:

```bash
git clone https://github.com/scc-digitalhub/digitalhub-sdk.git
cd digitalhub-sdk
pip install core/ data/ ml/ ./
pip install -r ml/modules/mlrun/requirements-wrapper.txt
pip install -r ml/modules/mlrun
```

If you want to exeute the mlrun runtime only remotely, you can avoid to install the requirement-wrapper.

## Function

The mlrun runtime introduces a function of kind `mlrun` that allows you to execute sql mlrun queries on your data.

### Mlrun function parameters

When you create a function of kind `mlrun`, you need to specify the following mandatory parameters:

- **`project`**: the project name with which the function is associated. **Only** if you do not use the project context to create the function, e.g. `project.new_function()`.
- **`name`**: the name of the function
- **`kind`**: the kind of the function, **must** be `mlrun`
- **`source`**: the source dictionary that contains the code, encoded code or path to code to be executed by mlrun. See section below

Optionally, you can specify the following parameters:

- **`uuid`**: the uuid of the function (this is automatically generated if not provided). **Must** be a valid uuid v4.
- **`description`**: the description of the function
- **`labels`**: the labels of the function
- **`git_source`**: the remote source of the function (git repository)
- **`embedded`**: whether the function is embedded or not. If `True`, the function is embedded (all the details are expressed) in the project. If `False`, the function is not embedded in the project.

#### Source

The **`source`** parameter must be a dictionary containing reference to the sql query to be executed. The parameter is structured as a dictionary with the following keys:

- **`source`**: the source URI to the code. It accepts the following values:
  - **git+https://repo-host/repo-owner/repo.git#indication-where-to-checkout**: the code is fetched from a git repository. The link points to the root of the repository, the fragment is as simple indication of the branch, tag or commit to checkout. The runtime will clone the repository and checkout the indicated branch, tag or commit.
  - **zip+s3://path-to-some-code.zip**: the code is fetched from a zip file in the *minio* digitalhub instance. The link points to the path to the zip file. The runtime will download the zip file and extract it. It fails if the zip file is not valid.
- **`code`**: the python string code
- **`base64`**: the base64 encoded code
- **`lang`**: the language of the code use in the console higlihter

Example:

```python
import digitalhub as dh

project = dh.get_or_create_project('my_project')

path = 'path-to-some-code.py'
dataitem = project.new_dataitem("my_dataitem", kind="table", path="path-to-some-data")

function = dh.new_function(
    kind='mlrun',
    name='my_function',
    source={"source": path}
)
```

## Task

The mlrun runtime introduces a task of kind `job` that allows you to execute a mlrun function.

### Job task parameters

When you want to execute a task of kind `job`, you need to pass the following mandatory parameters to the function method `run()`:

- **`action`**: the action to perform. This must be `job`.

The following parameters are optional, but usually you need to pass them:

- **`inputs`**: the list of referenced items used in the mlrun function.
- **`outputs`**: a list referenced items produced by the mlrun function.
- **`parameters`**: a dictionary of parameters to pass to the mlrun function `mlrun.run_function()`
- **`values`**: a list of output values that are not `artifacts`, `dataitems` or `models`

As optional, you can pass the following task parameters specific for remote execution:

- **`node_selector`**: a list of node selectors. The runtime will select the nodes to which the task will be scheduled.
- **`volumes`**: a list of volumes
- **`resources`**: a map of resources (CPU, memory, GPU)
- **`affinity`**: node affinity
- **`tolerations`**: tolerations
- **`env`**: environment variables to inject in the container
- **`secrets`**: list of secrets to inject in the container
- **`backoff_limit`**: the number of retries when a job fails.
- **`schedule`**: the schedule of the job as a cron expression
- **`replicas`**: the number of replicas of the deployment

Example:

```python
run = function.run(
    action='job',
    inputs=[{"mlrun-input-param-name": my_dataitem.key}],
    outputs=[{"mlrun-input-param-name": "my-output-name"}],
    parameters={"inputs": {"key": "value"}},
    values=["simple-mlrun-output-value-name"]
)
```

## Runtime workflow

The mlrun runtime execution workflow is the following:

1. The runtime fetches the input dataitems by downloading them locally.
2. It creates mlrun project and function.
3. It passes the local fetched data path to the mlrun function referenced by the input key as parameter and the content of `parameters`.
4. It executes the mlrun function and parses the results. It maps the outputs with the name passed in the `outputs` parameter. If the outputs are not `artifacts`, `dataitems` or `models`, the output is mapped with the `values`.
5. You can retrieve the outputs with the `run.outputs()` method.

## Snippet example

```python
import digitalhub as dh

# Get or create project
project = dh.get_or_create_project("project-mlrun")

# Create new input dataitem
url = "https://gist.githubusercontent.com/kevin336/acbb2271e66c10a5b73aacf82ca82784/raw/e38afe62e088394d61ed30884dd50a6826eee0a8/employees.csv"

# Create new dataitem
dataitem = project.new_dataitem(name="url-dataitem",
                                kind="table",
                                path=url)

# Create new function
downloader_function = project.new_function(name="mlrun-downloader",
                                           kind="mlrun",
                                           source={"source":"pipeline.py"},
                                           handler="downloader",
                                           image="mlrun/mlrun")

# Run function
downloader_run = downloader_function.run("job",
                                         inputs=[{"url": dataitem.key}],
                                         outputs=[{"dataset": "dataset"}])

# Run refresh
downloader_run.refresh()
```

pipeline.py file:

```python
import mlrun
import pandas as pd

@mlrun.handler(outputs=["dataset"])
def downloader(context, url: mlrun.DataItem):
    # read and rewrite to normalize and export as data
    df = url.as_df(format='parquet')
    return df
```
