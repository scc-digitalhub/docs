# Guardrail runtime

The Guardrail runtime enables user-defined Python handlers for request/response processing using [EnvoyProxy ExtProc](https://www.envoyproxy.io/docs/envoy/latest/api-v3/extensions/filters/http/ext_proc/v3/ext_proc.proto) specifications. It is provided by the `digitalhub-runtime-python` package.

## Prerequisites

| Requirement | Details |
| --- | --- |
| Package Python requirement | >= 3.10, < 3.15 |
| Execution Python versions | `PYTHON3_10`, `PYTHON3_11`, `PYTHON3_12`, `PYTHON3_13` |
| Package | `digitalhub-runtime-python` |

## Usage pattern

To execute a Guardrail function, follow this pattern:

1. Implement the handler as described in [handler definition](../define-function.md).
2. Use `dh.new_function()` or `project.new_function()` to create the function, passing function parameters.
3. Call `function.run()` with the desired action, passing task parameters and run parameters.

??? example "Create and serve a Guardrail function"

	```python
	function = dh.new_function(
		name="my-function",
		kind="guardrail",
		processing_mode="preprocessor",
		code_src="handler.py",
		handler="main",
		init_function="init",
		python_version="PYTHON3_10"
	)

	run = function.run(
		action="serve"
	)
	```

`processing_mode` selects how the guardrail handles request or response messages. Use `init_function` when the handler needs initialization before processing requests.

## Action documentation

Review the detailed parameters for each Guardrail action:

<div class="list-cards" markdown>

- [**Serve**](actions/guardrail-serve.md){ .list-card-link }

	Deploy a Guardrail function as a request/response processor.

- [**Build**](actions/guardrail-build.md){ .list-card-link }

	Build a container image for a Guardrail function.

</div>

## Examples

<div class="list-cards" markdown>

- [**Guardrail examples**](examples.md){ .list-card-link }

	Explore complete examples for Guardrail request/response processing.

</div>
