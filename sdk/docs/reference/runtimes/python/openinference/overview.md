# OpenInference Runtime

The OpenInference runtime enables you to execute user-defined Python handlers for inference-oriented services with explicit tensor schemas

## Supported kinds and actions

| Function Kind | Purpose | Supported Actions |
| --- | --- | --- |
| `openinference` | Inference services with declared model/tensor metadata | `serve`, `build` |

The shared actions behave as follows:

- **`serve`**: Deploy a handler as a long-lived service
- **`build`**: Create a Docker image with the required dependencies

## Prerequisites

**Package Python requirement:**

- Python >= 3.10, < 3.15

**Execution Python versions:**

- `PYTHON3_10`
- `PYTHON3_11`
- `PYTHON3_12`
- `PYTHON3_13`

**Required packages:**

- `digitalhub-runtime-python`

Install from PyPI:

```bash
pip install digitalhub-runtime-python
```

## Usage overview

To execute a Python-based handler on the platform:

1. Implement the handler as described in [handler definition](define-function.md).
2. Create a `Function` resource with kind `openinference`.
3. Call `function.run()` to execute the handler.

See [how to](how-to.md) for detailed instructions on which actions you can execute and how to configure each function kind.
See [Examples](examples.md) for code samples.
