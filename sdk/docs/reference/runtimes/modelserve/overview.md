---
render_macros: true
---

# ModelServe runtime

ModelServe deploys machine-learning models as services on Kubernetes using serving kinds for scikit-learn, MLflow, KubeAI and vLLM.

{{ runtime_prerequisites("digitalhub-runtime-modelserve") }}

{{ runtime_actions([
    ("scikit-learn serve", "sklearnserve-serve/action.md", "Serve a scikit-learn model saved in pickle format."),
    ("MLflow build", "mlflowserve-build/action.md", "Build a serving image for an MLflow model."),
    ("MLflow serve", "mlflowserve-serve/action.md", "Deploy an MLflow model as a service."),
    ("KubeAI text serve", "kubeai-text-serve/action.md", "Deploy a text model through KubeAI."),
    ("KubeAI speech serve", "kubeai-speech-serve/action.md", "Deploy a speech model through KubeAI."),
    ("vLLM text serve", "vllmserve-text-serve/action.md", "Deploy a vLLM text-generation model."),
    ("vLLM speech serve", "vllmserve-speech-serve/action.md", "Deploy a vLLM speech model."),
    ("vLLM pooling serve", "vllmserve-pooling-serve/action.md", "Deploy a vLLM model with pooling support."),
]) }}

{{ runtime_examples("Explore complete examples for supported model-serving kinds.") }}
