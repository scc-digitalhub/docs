# Flower Runtime

The Flower runtime enables you to execute federated learning tasks using the [Flower](https://flower.dev/) framework. It registers Function kinds `flower-app`, `flower-client`, and `flower-server` and supports various actions for federated learning workflows including training, building, and deploying federated applications.

- **`flower-app`**: Execute Flower simulations
- **`flower-client`**: Define a Flower client for federated learning participation
- **`flower-server`**: Define a Flower server to coordinate federated learning

## Prerequisites

**Supported Python versions:**

- Python ≥ 3.10, < 3.15

**Required packages:**

- `digitalhub-runtime-flower`

Install from PyPI:

```bash
pip install digitalhub-runtime-flower
```

For local execution (simulation mode):

```bash
pip install digitalhub-runtime-flower[local]
```

## Usage overview

To execute federated learning tasks on the platform:

1. Implement your Flower application (client and server).
2. Create a `Function` resource that references your Flower code.
3. Call `function.run()` to execute the federated learning task.

See [how to](how-to.md) for detailed instructions on which kind of applications you can execute and how to implement and deploy your Flower application.
See [Examples](examples.md) for code samples.
