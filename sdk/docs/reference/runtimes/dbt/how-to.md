# Execution Overview

This section explains how to execute dbt transformations in the DBT runtime.
First, we list the function types and actions, then we examine the usage pattern, including local vs remote execution.
Finally, we provide links to detailed documentation for each parameter category.

## Function types and Actions

There is one function kind in the DBT runtime:

- `dbt`: Execute dbt transformations

The kind supports specific actions.

| Function Kind | Supported Actions |
| --- | --- |
| `dbt` | `transform` |

## Usage Pattern

To execute a dbt transformation, follow this pattern:

1. Use `dh.new_function()` or `project.new_function()` to create the function, passing **function parameters**.
2. Call `function.run()` with the desired action, passing **task parameters** and **run parameters**.

```python
# Create function with function parameters
function = dh.new_function(
    name="my-function",
    kind="dbt",
    code="SELECT * FROM {{ ref('my_table_ref') }}"
)

# Execute with task and run parameters
run = function.run(
    action="transform",  # Task parameter
    inputs={"my_table_ref": dataitem.key},  # Run parameter
    outputs={"output_table": "mapped-name"}  # Run parameter
)
```

You can control whether the execution happens locally on your machine or remotely on the platform by setting the `local_execution` parameter (see [Local vs Remote Execution](#local-vs-remote-execution) for details).

### Local vs Remote Execution

When executing a function, you can choose between **local execution** and **remote execution** by setting the `local_execution` parameter in the run parameters.

- **Local Execution** (`local_execution=True`): The function runs directly on your local machine. You need to have the required dependencies of your function installed locally.

- **Remote Execution** (`local_execution=False`, default): The function is executed on a remote server or cluster managed by the platform.

## Parameter Documentation

Here are links to the detailed documentation for each parameter category:

- [DBT Transform](actions/dbt-transform.md) — Complete reference for the transform action including function, task, and run parameters.
