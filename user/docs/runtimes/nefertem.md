# Nefertem runtime

The Nefertem runtime allows you to run [Nefertem](https://github.com/scc-digitalhub/nefertem/tree/main) validation, profiling or inference on your data. It is a wrapper around the Nefertem library.
The runtime introduces a function of kind `neferetm` and four task of kind `validate`, `profile`, `infer` and `metric`.

## Prerequisites

Python libraries:

- python >= 3.9
- digitalhub-core[base_yaml]
- digitalhub-core-nefertem
- Nefertem plugins available in the [Nefertem repository](https://github.com/scc-digitalhub/nefertem/tree/main/plugins)

If you want to execute Nefertem tasks locally, you need to install digitalhub-core-nefertem package with `local` flag:

```bash
pip install digitalhub-core-nefertem[local]
```

Otherwise, only remote execution with Core backed available is possible.

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
- **`source_remote`**: the remote source of the function (git repository)
- **`source_code`**: pointer to the source code of the function
- **`constraints`**: the constraints of the function to be applied on the data. Valid only for `validate` tasks
- **`error_report`**: the error report output format. Valid only for `validate` tasks
- **`metrics`**: the metrics of the function to be applied on the data. Valid only for `metric` tasks
- **`embedded`**: whether the function is embedded or not. If `True`, the function is embedded (all the details are expressed) in the project. If `False`, the function is not embedded in the project.

For example:

```python
import digitalhub_core as dhcore

constraint = {
  'constraint': 'type',
  'field': 'Country',
  'field_type': 'string',
  'name': 'check_country_string',
  'resources': ['organizations'],
  'title': '',
  'type': 'frictionless',
  'value': 'string',
  'weight': 5
}
function = dhcore.new_function(name="nefertem-function",
                               kind="nefertem",
                               constraints=[constraint])
```

## Task

The Nefertem runtime introduces four tasks of kind `validate`, `profile`, `infer` and `metric` that allows you to run a Nefertem validation, profiling, inference or metric on your data.

### Validate task parameters

When you want to execute a task of kind `validate`, you need to pass the following mandatory parameters to the function method `run()`:

- **`action`**: the action to perform. This must be `validate`.
- **`inputs`**: the list of **dataitem names** to be validated. The corresponding dataitem objects must be present in the backend, whether it's local or Core backend.
- **`run_config`**: Nefretm run configuration.

For example:

```python
nefertem_run_config = {
        "operation": "validation",
        "exec_config": [{"framework": "frictionless"}]
}
run = function.run("validate",
                   run_config=nefertem_run_config,
                   inputs={"dataitems": ["organizations"]})
```

### Profile task parameters

When you want to execute a task of kind `profile`, you need to pass the following mandatory parameters to the function method `run()`:

- **`action`**: the action to perform. This must be `profile`.
- **`inputs`**: the list of **dataitem names** to be profiled. The corresponding dataitem objects must be present in the backend, whether it's local or Core backend.
- **`run_config`**: Nefretm run configuration.

For example:

```python
nefertem_run_config = {
        "operation": "profiling",
        "exec_config": [{"framework": "frictionless"}]
}
run = function.run("profile",
                   run_config=nefertem_run_config,
                   inputs={"dataitems": ["organizations"]})
```

### Infer task parameters

When you want to execute a task of kind `infer`, you need to pass the following mandatory parameters to the function method `run()`:

- **`action`**: the action to perform. This must be `infer`.
- **`inputs`**: the list of **dataitem names** to be inferred. The corresponding dataitem objects must be present in the backend, whether it's local or Core backend.
- **`run_config`**: Nefretm run configuration.

For example:

```python
nefertem_run_config = {
        "operation": "inference",
        "exec_config": [{"framework": "frictionless"}]
}
run = function.run("infer",
                   run_config=nefertem_run_config,
                   inputs={"dataitems": ["organizations"]})
```

### Metric task parameters

When you want to execute a task of kind `metric`, you need to pass the following mandatory parameters to the function method `run()`:

- **`action`**: the action to perform. This must be `metric`.
- **`inputs`**: the list of **dataitem names** to be measured. The corresponding dataitem objects must be present in the backend, whether it's local or Core backend.
- **`run_config`**: Nefretm run configuration.

For example:

```python
nefertem_run_config = {
        "operation": "measure",
        "exec_config": [{"framework": "frictionless"}]
}
run = function.run("metric",
                   run_config=nefertem_run_config,
                   inputs={"dataitems": ["organizations"]})
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
   4. If the task is `metric`:
      - `run.metric()`
      - `run.log_metric()` -> produces a `NefertemMetricReport`
      - `run.persist_metric()` -> produces one or more metric framework reports
4. The runtime then creates an `Artifact` object for each file produced by Nefertem and saves it into the *Core backend*. It then uploads all the files to the default *s3* storage provided. You can extract the path where the files are uploaded with the `run.get_artifacts()` method. In general, the path is `s3://<bucket-from-env>/<project-name>/artifacts/ntruns/<nefertem-run-uuid>/<file>`.

## Snippet example

```python
import digitalhub_core as dhcore

# Get or create project
project = dhcore.get_or_create_project("project-nefertem")

# Create dataitem
url = "https://media.githubusercontent.com/media/datablist/sample-csv-files/main/files/organizations/organizations-1000.csv"
di = project.new_dataitem(name="organizations",
                          kind="dataitem",
                          path=url)

# Create function
constraint = {
  'constraint': 'type',
  'field': 'Country',
  'field_type': 'string',
  'name': 'check_country_string',
  'resources': ['organizations'],
  'title': '',
  'type': 'frictionless',
  'value': 'string',
  'weight': 5
}
function = project.new_function(name="function-nefertem",
                                kind="nefertem",
                                constraints=[constraint])

# Run validate task
nefertem_run_config = {
        "operation": "validation",
        "exec_config": [{"framework": "frictionless"}]
}
run = function.run("validate",
                   run_config=nefertem_run_config,
                   inputs={"dataitems": ["organizations"]})
```
