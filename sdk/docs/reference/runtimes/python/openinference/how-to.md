# Execution Overview

This section explains how to execute a function in the OpenInference runtime.
First, we list the function types and actions, then we examine the usage pattern.
Finally, we provide links to detailed documentation for each parameter category.

## Function types and Actions

The OpenInference runtime package exposes  `openinference` kind that executes Python handlers yo expose inference-style tensor schemas

| Function Kind | Supported Actions |
| --- | --- |
| `openinference` | `serve`, `build` |

## Usage Pattern

To execute a function, follow this pattern:

1. Implement a Python function (see [Function definition](define-function.md) for detailed instructions on creating Python, guardrail, and openinference handlers).
2. Use `dh.new_function()` or `project.new_function()` to create the function, passing **function parameters**.
3. Call `function.run()` with the desired action, passing **task parameters** and **run parameters**.

```python
# Create function with function parameters
function = dh.new_function(
    name="my-openinference-function",
    kind="openinference",
    code_src="inference.py",
    handler="predict",
    python_version="PYTHON3_10",
    model_name="text-classifier",
    inputs=[{"name": "input-0", "shape": [-1, -1], "datatype": "BYTES"}],
    outputs=[{"name": "output-0", "shape": [-1, -1], "datatype": "FP32"}]
)

run = function.run(
    action="serve",
    replicas=1,
)
```

## Parameter Documentation

Here are links to the detailed documentation for each action:

- [OpenInference Serve](openinference-serve.md) — Deploy an `openinference` function as an inference endpoint
- [OpenInference Build](openinference-build.md) — Build a container image for an `openinference` function
