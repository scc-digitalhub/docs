# Execution Overview

This section explains how to execute model serving tasks in the ModelServe runtime.
First, we list the function types and actions, then we examine the usage pattern.
Finally, we provide links to detailed documentation for each parameter category.

## Function types and Actions

There are multiple function kinds in the ModelServe runtime:

- `sklearnserve`: Serve scikit-learn models
- `mlflowserve`: Serve MLflow models
- `huggingfaceserve`: Serve HuggingFace models
- `kubeai-text`: Serve text generation models via KubeAI
- `kubeai-speech`: Serve speech processing models via KubeAI
- `vllmserve-text`: Serve vLLM text generation models
- `vllmserve-speech`: Serve vLLM speech models
- `vllmserve-pooling`: Serve vLLM models with pooling support

Each kind supports specific actions.

| Function Kind | Supported Actions |
| --- | --- |
| `sklearnserve` | `serve` |
| `mlflowserve` | `build`, `serve` |
| `huggingfaceserve` | `serve` |
| `kubeai-text` | `serve` |
| `kubeai-speech` | `serve` |
| `vllmserve-text` | `serve` |
| `vllmserve-speech` | `serve` |
| `vllmserve-pooling` | `serve` |

## Usage Pattern

To execute a model serving task, follow this pattern:

1. Use `dh.new_function()` or `project.new_function()` to create the function, passing **function parameters**.
2. Call `function.run()` with the desired action, passing **task parameters** and **run parameters**.

```python
# Create function with function parameters
function = dh.new_function(
    name="my-model-function",
    kind="mlflowserve",
    path="s3://my-bucket/path-to-model"
)

# Execute with task and run parameters
run = function.run(
    action="serve",  # Task parameter
    replicas=1  # Task parameter
)
```

ModelServe functions are executed remotely on Kubernetes clusters managed by the platform.

## Parameter Documentation

Here are links to the detailed documentation for each ModelServe action:

- [sklearnserve serve](actions/sklearnserve-serve.md) — Deploy scikit-learn models as services
- [mlflowserve build](actions/mlflowserve-build.md) — Build MLflow model-serving images
- [mlflowserve serve](actions/mlflowserve-serve.md) — Deploy MLflow models as services
- [huggingfaceserve serve](actions/huggingfaceserve-serve.md) — Deploy HuggingFace models as services
- [kubeai-text serve](actions/kubeai-text-serve.md) — Deploy text processing models via KubeAI
- [kubeai-speech serve](actions/kubeai-speech-serve.md) — Deploy speech processing models via KubeAI
- [vllmserve-text serve](actions/vllmserve-text-serve.md) — Deploy vLLM text generation models
- [vllmserve-speech serve](actions/vllmserve-speech-serve.md) — Deploy vLLM speech models
- [vllmserve-pooling serve](actions/vllmserve-pooling-serve.md) — Deploy vLLM models with pooling support
