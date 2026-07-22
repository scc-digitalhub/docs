# Container Runtime

The Container runtime enables launching pods, jobs and services on Kubernetes. It registers Function kind `container` and supports various actions for containerized workloads including jobs, services and builds.

- **`container`**: Execute containerized workloads on Kubernetes

## Prerequisites

**Supported Python versions:**

- Python ≥ 3.10, < 3.15

**Required packages:**

- `digitalhub-runtime-container`

Install from PyPI:

```bash
pip install digitalhub-runtime-container
```

## Usage overview

To execute container workloads on the platform:

1. Prepare your container image or build instructions.
2. Create a `Function` resource that references your container configuration.
3. Call `function.run()` to execute the container workload.

See [how to](how-to.md) for detailed instructions on which actions you can execute and how to configure your container workloads.
See [Examples](examples.md) for code samples.
