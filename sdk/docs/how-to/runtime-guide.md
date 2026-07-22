# Runtime Guide

This guide helps you choose the right runtime for your use case. The Digitalhub platform provides several specialized runtimes, each designed for different types of workloads and execution patterns.

## Quick Runtime Selection

| If you need to... | Use this runtime | Best for |
| --- | --- | --- |
| Execute Python code | [Python Runtime](../reference/runtimes/python/python/overview.md) | General-purpose Python execution, guardrails, and OpenInference services |
| Run containerized applications | [Container Runtime](../reference/runtimes/container/overview.md) | Custom containers, complex dependencies |
| Orchestrate multiple steps | [Hera Runtime](../reference/runtimes/hera/overview.md) | Workflow orchestration, DAGs |
| Serve ML models | [ModelServe Runtime](../reference/runtimes/modelserve/overview.md) | Model inference, API serving |
| Transform tabular data | [DBT Runtime](../reference/runtimes/dbt/overview.md) | Data transformation, SQL workflows |
| Run federated learning | [Flower Runtime](../reference/runtimes/flower/overview.md) | Federated learning, privacy-preserving ML |

## Runtime Capabilities Matrix

| Runtime | Local Execution | Remote Execution | Multi-step Workflows | Model Serving | Data Processing | Federated Learning |
| --- | --- | --- | --- | --- | --- | --- |
| **Python** | ✅ | ✅ | ❌ | ✅ | ✅ | ❌ |
| **Container** | ❌ | ✅ | ❌ | ❌ | ✅ | ❌ |
| **Hera** | ❌ | ✅ | ✅ | ❌ | ✅ | ❌ |
| **ModelServe** | ❌ | ✅ | ❌ | ✅ | ❌ | ❌ |
| **DBT** | ✅ | ✅ | ❌ | ❌ | ✅ | ❌ |
| **Flower** | ✅ | ✅ | ❌ | ❌ | ❌ | ✅ |

## Detailed Selection Guide

### Python Runtime

**Choose when:**

- You have Python code that needs to run
- You want simple job execution or model training
- You need request/response processing through `guardrail`
- You need inference endpoints with declared tensor schemas through `openinference`
- Your workload fits within Python's ecosystem

### Container Runtime

**Choose when:**

- Your application requires complex dependencies
- You want to run existing containerized applications
- Python runtime isn't sufficient for your environment needs

### Hera Runtime

**Choose when:**

- You have multiple steps to execute in sequence
- You want to build DAGs (Directed Acyclic Graphs)
- You need conditional execution or parallel processing

### ModelServe Runtime

**Choose when:**

- You need to serve machine learning models
- You want to expose models as REST APIs
- You need scalable model inference
- You work with various ML frameworks (scikit-learn, MLflow, HuggingFace, etc.)

### DBT Runtime

**Choose when:**

- You work with tabular data
- You need SQL-based data transformations

### Flower Runtime

**Choose when:**

- You want to implement federated learning
- You need privacy-preserving machine learning
- You work with distributed datasets across multiple parties
- You want to use the Flower framework for FL

## Getting Started with Your Chosen Runtime

Once you've selected a runtime, follow these steps:

1. **Read the overview** for your chosen runtime
2. **Check the examples** to see common usage patterns
3. **Review the execution guide** for detailed parameter information
4. **Explore the entity documentation** for complete API reference

## Need Help Choosing?

If you're still unsure which runtime to use, consider:

- **Start with Python Runtime** if you're new to the platform
- **Use Container Runtime** if you have complex dependencies
- **Use Hera Runtime** if you have multiple coordinated steps
- **Use ModelServe Runtime** if you need to serve ML models
- **Use DBT Runtime** if you work primarily with SQL and tabular data
- **Use Flower Runtime** if you need federated learning capabilities
