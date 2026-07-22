# Execution Overview

This section explains how to execute container workloads in the Container runtime.
First, we list the function types and actions, then we examine the usage pattern.
Finally, we provide links to detailed documentation for each parameter category.

## Function types and Actions

There is one function kind in the Container runtime:

- `container`: Execute containerized workloads on Kubernetes

The kind supports specific actions.

| Function Kind | Supported Actions |
| --- | --- |
| `container` | `job`, `serve`, `build` |

## Usage Pattern

To execute a container workload, follow this pattern:

1. Use `dh.new_function()` or `project.new_function()` to create the function, passing **function parameters**.
2. Call `function.run()` with the desired action, passing **task parameters** and **run parameters**.

```python
# Create function with function parameters
function = dh.new_function(
    name="my-function",
    kind="container",
    image="my-image:latest",
    command="my-command"
)

# Execute with task and run parameters
run = function.run(
    action="job",  # Task parameter
    args=["arg1", "arg2"]  # Run parameter
)
```

Container functions are executed remotely on Kubernetes clusters managed by the platform.

## Parameter Documentation

Here are links to the detailed documentation for each container action:

- [Container Job](actions/container-job.md) — Execute a container as a one-off job
- [Container Serve](actions/container-serve.md) — Deploy a container as a long-lived service
- [Container Build](actions/container-build.md) — Create a Docker image with custom instructions
