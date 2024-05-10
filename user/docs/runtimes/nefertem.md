# Nefertem runtime

The Nefertem runtime allows you to run [Nefertem](https://github.com/scc-digitalhub/nefertem/tree/main) validation, profiling or inference on your data. It is a wrapper around the Nefertem library.
The runtime introduces a function of kind `neferetm` and four task of kind `validate`, `profile`, `infer` and `metric`.

## Prerequisites

Python libraries:

- python >= 3.9
- digitalhub
- digitalhub-data-nefertem
- Nefertem plugins available in the [Nefertem repository](https://github.com/scc-digitalhub/nefertem/tree/main/plugins)

If you want to execute Nefertem tasks locally, you need to install digitalhub-core-nefertem package with `local` flag:

```bash
git clone https://github.com/scc-digitalhub/digitalhub-sdk.git
cd digitalhub-sdk
pip install core/ data/ ./
pip install data/modules/nefertem[local]
```

## Function

The Nefertem runtime introduces a function of kind `neferetm` that allows you to execute various tasks on your data.

### Nefertem function parameters

When you create a function of kind `neferetm`, you need to specify the following mandatory parameters:

- **`project`**: the project name with which the function is associated. **Only** if you do not use the project context to create the function, e.g. `project.new_function()`.
- **`name`**: the name of the function
- **`kind`**: the kind of the function, **must** be `neferetm`

Optionally, you can specify the following parameters:

- **`uuid`**: the uuid of the function (this is automatically generated if not provided). **Must** be a valid uuid v4.
- **`description`**: the description of the function
- **`labels`**: the labels of the function
- **`git_source`**: the remote source of the function (git repository)
- **`source_code`**: pointer to the source code of the function
- **`constraints`**: the constraints of the function to be applied on the data. Valid only for `validate` tasks
- **`error_report`**: the error report output format. Valid only for `validate` tasks
- **`embedded`**: whether the function is embedded or not. If `True`, the function is embedded (all the details are expressed) in the project. If `False`, the function is not embedded in the project.

For example:

```python
import digitalhub_core as dh

constraint = {
  'constraint': 'type',
  'field': 'field-name',
  'field_type': 'string',
  'name': 'check_country_string',
  'resources': ['ref-source'],
  'title': '',
  'type': 'const-type',
  'value': 'string',
  'weight': 5
}
function = dh.new_function(name="nefertem-function",
                           kind="nefertem",
                           constraints=[constraint])
```

## Task

The Nefertem runtime introduces three tasks of kind `validate`, `profile` and `infer` that allows you to run a Nefertem validation, profiling or inference on your data.

### Validate task parameters

When you want to execute a task of kind `validate`, you need to pass the following mandatory parameters to the function method `run()`:

- **`action`**: the action to perform. This must be `validate`.
- **`framework`**: the Nefertem framework to be used.
- **`inputs`**: the list of nefertem resources referenced in the constraint mapped to some dataitem keys. The corresponding dataitem objects must be present in the backend, whether it's local or Core backend.

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

For example:

```python
run = function.run("validate",
                   framework="frictionless",
                   inputs={"employees": di.key})
```

### Profile task parameters

When you want to execute a task of kind `profile`, you need to pass the following mandatory parameters to the function method `run()`:

- **`action`**: the action to perform. This must be `profile`.
- **`framework`**: the Nefertem framework to be used.
- **`inputs`**: the list of nefertem resources referenced mapped to some dataitem keys. The corresponding dataitem objects must be present in the backend, whether it's local or Core backend.

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

For example:

```python
run = function.run("profile",
                   framework="frictionless",
                   inputs={"employees": di.key})
```

### Infer task parameters

When you want to execute a task of kind `infer`, you need to pass the following mandatory parameters to the function method `run()`:

- **`action`**: the action to perform. This must be `infer`.
- **`framework`**: the Nefertem framework to be used.
- **`inputs`**: the list of nefertem resources referenced mapped to some dataitem keys. The corresponding dataitem objects must be present in the backend, whether it's local or Core backend.

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

For example:

```python
run = function.run("infer",
                   framework="frictionless",
                   inputs={"employees": di.key})
```

## Runtime workflow

The Nefertem runtime execution workflow is the following:

1. The runtime fetches the input dataitems by downloading them locally. The runtime tries to get the file from the `path` attribute. At the moment, we support the following path types:
     - `http(s)://<url>`
     - `s3://<bucket>/<path>`
     - `sql://<database>(/<schema-optional>)/<table>`
     - `<local-path>`
2. The runtime creates a Nefertem `DataResource` from the input dataitem. The `DataResource` is a Nefertem object that represents the data to be validated, profiled, inferred or measured.
3. The runtime then create a Nefertem `run` and execute it. The Nefertem `run` executes three methods based on the *task*, and produces a `run_metadata` report file:
   1. If the task is `validate`:
      - `run.validate()`
      - `run.log_report()` -> produces a `NefertemReport`
      - `run.persist_report()` -> produces one or more validation framework reports
   2. If the task is `profile`:
      - `run.profile()`
      - `run.log_profile()` -> produces a `NefertemProfile`
      - `run.persist_profile()` -> produces one or more profiling framework reports
   3. If the task is `infer`:
      - `run.infer()`
      - `run.log_schema()` -> produces a `NefertemSchema`
      - `run.persist_schema()` -> produces one or more inference framework reports
4. The runtime then creates an `Artifact` object for each file produced by Nefertem and saves it into the *Core backend*. It then uploads all the files to the default *s3* storage provided. You can collect the artifacts with the `run.outputs()` method. In general, the saving path is `s3://<bucket-from-env>/<project-name>/artifacts/ntruns/<nefertem-run-uuid>/<file>`.

## Snippet example

```python
import digitalhub as dh

# Get or create project
project = dh.get_or_create_project("project-nefertem")

# Create dataitem
url = "https://gist.githubusercontent.com/kevin336/acbb2271e66c10a5b73aacf82ca82784/raw/e38afe62e088394d61ed30884dd50a6826eee0a8/employees.csv"
di = project.new_dataitem(name="employees",
                          kind="table",
                          path=url)

# Create function
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
function = project.new_function(name="function-nefertem",
                                kind="nefertem",
                                constraints=[constraint])

# Run validate task
run = function.run("validate",
                   framework="frictionless",
                   inputs={"employees": di.key})

# Refresh run
run.refresh()
```
