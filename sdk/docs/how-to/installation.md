---
render_macros: true
---

# Installation

Install the SDK first, then install the runtime required by your workload. Packages are available on [PyPI](https://pypi.org/project/digitalhub/) and can be installed with `uv`, `pip`, or another Python package manager.

## SDK

For a complete first installation, install the SDK with all its optional feature dependencies:

=== "uv"

	```bash
	uv pip install "digitalhub[full]"
	```

=== "pip"

	```bash
	python -m pip install "digitalhub[full]"
	```

This is the recommended SDK installation. It includes the dependencies used by the SDK's data and model features.

??? note "Install individual SDK extras"

	The `full` extra already includes these dependencies. Install an individual extra only when you intentionally want a smaller installation.

	=== "uv"

		```bash
		uv pip install "digitalhub[pandas]"
		uv pip install "digitalhub[polars]"
		uv pip install "digitalhub[mlcroissant]"
		uv pip install "digitalhub[huggingface]"
		```

	=== "pip"

		```bash
		python -m pip install "digitalhub[pandas]"
		python -m pip install "digitalhub[polars]"
		python -m pip install "digitalhub[mlcroissant]"
		python -m pip install "digitalhub[huggingface]"
		```

## Runtimes

Install the runtime required by your workload. The Python, Container, ModelServe, and Hera runtimes cover the most common workloads; the remaining runtimes support more specialized use cases.

{{ runtime_installation("digitalhub-runtime-python", div="python") }}

{{ runtime_installation("digitalhub-runtime-container", div="container") }}

{{ runtime_installation("digitalhub-runtime-modelserve", div="modelserve") }}

{{ runtime_installation("digitalhub-runtime-hera", local_description="The `[local]` extra enables local execution of build actions.", div="hera") }}

{{ runtime_installation("digitalhub-runtime-dbt", local_description="The `[local]` extra enables local execution.", div="dbt") }}

{{ runtime_installation("digitalhub-runtime-flower", local_description="The `[local]` extra enables local simulation.", div="flower") }}

{{ runtime_installation("digitalhub-runtime-servicegraph", div="servicegraph") }}

{{ runtime_installation("digitalhub-runtime-tvm", div="tvm") }}

{{ runtime_installation("digitalhub-runtime-hydra", div="hydra") }}

{{ runtime_installation("digitalhub-runtime-ray", div="ray") }}

For runtime actions, parameters, and usage details, see the [Runtime reference](../reference/runtimes/index.md).
