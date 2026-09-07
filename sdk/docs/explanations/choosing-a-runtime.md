---
render_macros: true
---

# Execution frameworks

Choose an execution framework based on what you need to run, how it should run, and which dependencies it requires. DigitalHub provides execution frameworks for Python jobs, containers, model serving, workflow orchestration, data transformation, federated learning, and service pipelines.

{{ framework_card(
	title="Python",
	link="../reference/runtimes/python/python/overview.md",
	description="Execute user-defined Python handlers for jobs, model training, and services.",
	use_cases=[
		"Batch jobs and model training.",
		"Services and APIs.",
	]
) }}

{{ framework_card(
	title="Container",
	link="../reference/runtimes/container/overview.md",
	description="Run existing containerized applications with custom dependencies.",
	use_cases=[
		"Existing containerized applications.",
		"Workloads with custom system dependencies.",
		"Remote jobs and services on Kubernetes.",
	]
) }}

{{ framework_card(
	title="ModelServe",
	link="../reference/runtimes/modelserve/overview.md",
	description="Deploy supported machine learning models as scalable inference services.",
	use_cases=[
		"REST inference endpoints.",
		"scikit-learn, MLflow, and Hugging Face models.",
		"vLLM text and speech serving.",
	]
) }}

{{ framework_card(
	title="Hera",
	link="../reference/runtimes/hera/overview.md",
	description="Build and execute multi-step workflows with Hera.",
	use_cases=[
		"DAG and Steps pipelines.",
		"Conditional or parallel workflow execution.",
		"Workflow definitions compiled for remote runs.",
	]
) }}

{{ framework_card(
	title="Flower",
	link="../reference/runtimes/flower/overview.md",
	description="Build privacy-preserving federated-learning workloads.",
	use_cases=[
		"Federated learning simulations.",
		"Flower clients and servers.",
		"Training across distributed datasets.",
	]
) }}

{{ framework_card(
	title="DBT",
	link="../reference/runtimes/dbt/overview.md",
	description="Transform tabular data with SQL-based workflows.",
	use_cases=[
		"SQL transformations on tabular data.",
		"Local or remote DBT runs.",
		"PostgreSQL-backed data workflows.",
	]
) }}

{{ framework_card(
	title="ServiceGraph",
	link="../reference/runtimes/servicegraph/overview.md",
	description="Deploy synchronous or asynchronous pipelines that orchestrate services and streaming data.",
	use_cases=[
		"Synchronous or asynchronous service pipelines.",
		"AI service processing chains.",
		"Streaming inputs and outputs.",
	]
) }}

{{ framework_card(
	title="Guardrail",
	link="../reference/runtimes/python/guardrail/overview.md",
	description="Execute Python handlers for request/response processing using EnvoyProxy ExtProc specifications.",
	use_cases=[
		"Request and response processing.",
		"Preprocessing and postprocessing traffic.",
		"Guardrails around service requests and responses.",
	]
) }}

{{ framework_card(
	title="Openinference",
	link="../reference/runtimes/python/openinference/overview.md",
	description="Execute Python handlers for inference-oriented services with explicit tensor schemas.",
	use_cases=[
		"Inference endpoints.",
		"Explicit input and output tensor schemas.",
		"Model inference services.",
	]
) }}

## Next steps

Once you've selected an execution framework, follow these steps:

1. **Read the overview** for your chosen execution framework
2. **Check the examples** to see common usage patterns
3. **Review the execution guide** for detailed parameter information
4. **Explore the entity documentation** for complete API reference

!!! tip "Still unsure?"

	Start with Python for general-purpose workloads. Choose Container for complex dependencies, Hera for coordinated steps, ModelServe for model inference, DBT for SQL transformations, or Flower for federated learning.
