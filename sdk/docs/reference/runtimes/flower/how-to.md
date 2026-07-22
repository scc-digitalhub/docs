# Execution Overview

This section explains how to execute federated learning tasks in the Flower runtime.
First, we list the function types and actions, then we examine the usage pattern, including local vs remote execution.
Finally, we provide links to detailed documentation for each function and action.

## Function types and Actions

There are three function kinds in the Flower runtime:

- `flower-app`: Complete Flower application with client and server components
- `flower-client`: Flower client for federated learning participation
- `flower-server`: Flower server for managing federated learning tasks

Each kind supports specific actions.

| Function Kind | Supported Actions |
| --- | --- |
| `flower-app` | `train` |
| `flower-client` | `build`, `deploy` |
| `flower-server` | `build`, `deploy` |

## Usage Pattern

To execute a federated learning task, follow this pattern:

1. Use `dh.new_function()` or `project.new_function()` to create the function, passing **function parameters**.
2. Call `function.run()` with the desired action, passing **task parameters** and **run parameters**.

```python
# Create Flower function that references a Flower app source
# in a git repository
function = dh.new_function(
    name="my-flower-app",
    kind="flower-app",
    source="git+https://github.com/your-org/your-repo"
)

# Execute with task and run parameters
run = function.run(
    action="train",  # Task parameter
    federation="my-federation",  # Run parameter
    superlink="superlink-service",  # Run parameter
    parameters={"num_rounds": 10}  # Run parameter
)
```

### Local vs Remote Execution

When executing a **flower-app** function (and only that) with `train` action, you can choose between **local execution** and **remote execution** by setting the `local_execution` parameter in the run parameters.

- **Local Execution** (`local_execution=True`): The function runs directly on your local machine using Flower's simulation mode. You need to have Flower and required dependencies installed locally.

- **Remote Execution** (`local_execution=False`, default): The function is executed on a remote server or cluster managed by the platform.

## Function and Action Documentation

Here are links to the detailed documentation for each function and action:

- Function `flower-app` action `train` [docs](actions/flower-app-train.md).
- Function `flower-client` action `build` [docs](actions/flower-client-build.md).
- Function `flower-client` action `deploy` [docs](actions/flower-client-deploy.md).
- Function `flower-server` action `build` [docs](actions/flower-server-build.md).
- Function `flower-server` action `deploy` [docs](actions/flower-server-deploy.md).
