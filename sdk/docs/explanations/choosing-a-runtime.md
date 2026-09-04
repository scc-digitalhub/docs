# Choosing a runtime

Choose a runtime based on your workload, execution model, and dependency requirements. DigitalHub provides specialized runtimes for Python jobs, containers, model serving, workflow orchestration, data transformation, federated learning, and service pipelines.

<div class="runtime-cards" markdown>

- [**Python Runtime**](../reference/runtimes/python/python/overview.md){ .runtime-card-link }

	Execute user-defined Python handlers for jobs, model training, and services.

	**Use cases**{ .runtime-card-label }

	Batch jobs; request/response handlers with `guardrail`; inference endpoints with `openinference`.

- [**Container Runtime**](../reference/runtimes/container/overview.md){ .runtime-card-link }

	Run existing containerized applications with custom dependencies.

	**Use cases**{ .runtime-card-label }

	Existing containerized applications; workloads with custom system dependencies; remote jobs and services on Kubernetes.

- [**ModelServe Runtime**](../reference/runtimes/modelserve/overview.md){ .runtime-card-link }

	Deploy supported machine learning models as scalable inference services.

	**Use cases**{ .runtime-card-label }

	REST inference endpoints; scikit-learn, MLflow, and Hugging Face models; vLLM text and speech serving.

- [**Hera Runtime**](../reference/runtimes/hera/overview.md){ .runtime-card-link }

	Build and execute multi-step workflows with Hera.

	**Use cases**{ .runtime-card-label }

	DAG and Steps pipelines; conditional or parallel workflow execution; workflow definitions compiled for remote runs.

- [**Flower Runtime**](../reference/runtimes/flower/overview.md){ .runtime-card-link }

	Build privacy-preserving federated-learning workloads.

	**Use cases**{ .runtime-card-label }

	Federated learning simulations; Flower clients and servers; training across distributed datasets.

- [**DBT Runtime**](../reference/runtimes/dbt/overview.md){ .runtime-card-link }

	Transform tabular data with SQL-based workflows.

	**Use cases**{ .runtime-card-label }

	SQL transformations on tabular data; local or remote DBT runs; PostgreSQL-backed data workflows.

- [**ServiceGraph Runtime**](../reference/runtimes/servicegraph/overview.md){ .runtime-card-link }

	Deploy synchronous or asynchronous pipelines that orchestrate services and streaming data.

	**Use cases**{ .runtime-card-label }

	Synchronous or asynchronous service pipelines; AI service processing chains; streaming inputs and outputs.

- **TVM Runtime**

	Runtime documentation will be added here.

	**Use cases**{ .runtime-card-label }

	To be defined.

</div>

## Next steps

Once you've selected a runtime, follow these steps:

1. **Read the overview** for your chosen runtime
2. **Check the examples** to see common usage patterns
3. **Review the execution guide** for detailed parameter information
4. **Explore the entity documentation** for complete API reference

!!! tip "Still unsure?"

	Start with the Python Runtime for general-purpose workloads. Choose the Container Runtime for complex dependencies, Hera for coordinated steps, ModelServe for model inference, DBT for SQL transformations, or Flower for federated learning.
