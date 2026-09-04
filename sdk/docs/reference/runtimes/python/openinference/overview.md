# OpenInference runtime

The OpenInference runtime enables you to execute user-defined Python handlers for inference-oriented services with explicit tensor schemas.

## Prerequisites

| Requirement | Details |
| --- | --- |
| Package Python requirement | >= 3.10, < 3.15 |
| Execution Python versions | `PYTHON3_10`, `PYTHON3_11`, `PYTHON3_12`, `PYTHON3_13` |
| Package | `digitalhub-runtime-python` |

## Usage pattern

To execute an OpenInference function, follow this pattern:

1. Implement the handler as described in [handler definition](../define-function.md).
2. Use `dh.new_function()` or `project.new_function()` to create the function, passing function parameters.
3. Call `function.run()` with the desired action, passing task parameters and run parameters.

??? example "Create and serve an OpenInference function"

	```python
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

The `inputs` and `outputs` parameters declare the tensor names, shapes and data types exposed by the inference service.

## Action documentation

Review the detailed parameters for each OpenInference action:

<div class="list-cards" markdown>

- [**Serve**](actions/openinference-serve.md){ .list-card-link }

	Deploy an OpenInference function as an inference endpoint.

- [**Build**](actions/openinference-build.md){ .list-card-link }

	Build a container image for an OpenInference function.

</div>

## Examples

<div class="list-cards" markdown>

- [**OpenInference examples**](examples.md){ .list-card-link }

	Explore complete examples for OpenInference inference services.

</div>
