# Execution Overview

This section explains how to execute ServiceGraph serving tasks in the ServiceGraph runtime.
First, we list the function types and actions, then we examine the usage pattern.
Finally, we provide links to detailed documentation for each parameter category.

## Function types and Actions
The function kind in the ServiceGraph runtime is `servicegraph` supporing the `serve` action.


## Usage Pattern

To execute a graph serving task, follow this pattern:

1. Use `dh.new_function()` or `project.new_function()` to create the function, passing **function parameters**.
2. Call `function.run()` with the desired action, passing **task parameters** and **run parameters**.

```python
# Create function with function parameters
function = dh.new_function(
    name="my-graph",
    kind="servicegraph",
    code_src="src/flow.yaml"
)

# Execute with task and run parameters
run = function.run(
    action="serve",  # Task parameter
    parameters={
        "input.url": "http://videosource:1984"
    }
)
```

ServiceGraph functions are executed remotely on Kubernetes clusters managed by the platform.

## Parameter Documentation

Here are links to the detailed documentation for the serving actions in the ServiceGraph runtime:

- [servicegraph serve](../../reference/runtimes/servicegraph/actions/servicegraph-serve.md)
