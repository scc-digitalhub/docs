# Execution Overview

This section explains how to execute a function in the Guardrail runtime.
First, we list the function types and actions, then we examine the usage pattern, including local vs remote execution.
Finally, we provide links to detailed documentation for each parameter category.

## Function types and Actions

The Guardrail runtime package exposes `guardrail` kind that execute Python handlers to process incoming and/or outgoing requests.

| Function Kind | Supported Actions |
| --- | --- |
| `guardrail` | `serve`, `build` |

## Usage Pattern

To execute a function, follow this pattern:

1. Implement a Python function (see [Function definition](define-function.md) for detailed instructions on creating guardrail handlers).
2. Use `dh.new_function()` or `project.new_function()` to create the function, passing **function parameters**.
3. Call `function.run()` with the desired action, passing **task parameters** and **run parameters**.

```python
# Create function with function parameters
function = dh.new_function(
    name="my-function",
    kind="guardrail",
    processing_mode="preprocessor",
    code_src="handler.py",
    handler="main",
    init_function="init",
    python_version="PYTHON3_10"
)

# Execute with task and run parameters
run = function.run(
    action="serve"  # Task parameter
)
```
## Parameter Documentation

Here are links to the detailed documentation for each Python action:

- [Guardrail Serve](guardrail-serve.md) — Deploy a `guardrail` function as a request/response processor
- [Guardrail Build](guardrail-build.md) — Build a container image for a `guardrail` function
