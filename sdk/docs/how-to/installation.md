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

??? note "Python"

	**Use it for:** Create and execute Python functions.

	The Python runtime also provides the `guardrail` and `openinference` function kinds. They do not require separate runtime packages.

	=== "uv"

		```bash
		uv pip install digitalhub-runtime-python
		```

	=== "pip"

		```bash
		python -m pip install digitalhub-runtime-python
		```

??? note "Container"

	**Use it for:** Run containerized applications.

	See the [Container runtime reference](../reference/runtimes/container/overview.md) for supported actions and configuration.

	=== "uv"

		```bash
		uv pip install digitalhub-runtime-container
		```

	=== "pip"

		```bash
		python -m pip install digitalhub-runtime-container
		```

??? note "ModelServe"

	**Use it for:** Serve machine learning models.

	See the [ModelServe runtime reference](../reference/runtimes/modelserve/overview.md) for supported model types and actions.

	=== "uv"

		```bash
		uv pip install digitalhub-runtime-modelserve
		```

	=== "pip"

		```bash
		python -m pip install digitalhub-runtime-modelserve
		```

??? note "Hera"

	**Use it for:** Build and run workflows.

	See the [Hera runtime reference](../reference/runtimes/hera/overview.md) for pipeline definition and execution.

	=== "uv"

		```bash
		uv pip install digitalhub-runtime-hera
		```

	=== "pip"

		```bash
		python -m pip install digitalhub-runtime-hera
		```

??? note "DBT"

	**Use it for:** Run DBT transformations.

	Add `[local]` to the package name for local execution. See the [DBT runtime reference](../reference/runtimes/dbt/overview.md) for details.

	=== "uv"

		```bash
		uv pip install digitalhub-runtime-dbt
		```

	=== "pip"

		```bash
		python -m pip install digitalhub-runtime-dbt
		```

??? note "Flower"

	**Use it for:** Run federated learning workloads.

	Add `[local]` to the package name for local simulation. See the [Flower runtime reference](../reference/runtimes/flower/overview.md) for details.

	=== "uv"

		```bash
		uv pip install digitalhub-runtime-flower
		```

	=== "pip"

		```bash
		python -m pip install digitalhub-runtime-flower
		```

??? note "ServiceGraph"

	**Use it for:** Deploy service pipelines.

	See the [ServiceGraph runtime reference](../reference/runtimes/servicegraph/overview.md) for details.

	=== "uv"

		```bash
		uv pip install digitalhub-runtime-servicegraph
		```

	=== "pip"

		```bash
		python -m pip install digitalhub-runtime-servicegraph
		```

??? note "TVM"

	**Use it for:** TVM model support.

	An SDK runtime guide is not available yet.

	=== "uv"

		```bash
		uv pip install digitalhub-runtime-tvm
		```

	=== "pip"

		```bash
		python -m pip install digitalhub-runtime-tvm
		```

For runtime actions, parameters, and usage details, see the [Runtime reference](../reference/runtimes/index.md).
