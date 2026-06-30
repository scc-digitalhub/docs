# Speech to Text Serving Runtime

The **Speech to Text serving runtime** (kubeai-speech) supports exposing automated speech-recognition functionality as an OpenAI-compatible transcriptions API.
 
For this purpose, the runtime relies on [KubeAI](https://www.kubeai.org/) operator to expose models using the FasterWhisper engine. Serving is performed by KubeAI, similarly to the KubeAI Text runtime. 

The specification of the KubeAI speech runtime amounts to defining:

- model URL (from S3 storage or from HuggingFace catalog, e.g., ``hf://Systran/faster-whisper-medium.en``)
- name of the model to expose
- optional base image for serving

The ``serve`` action allows for deploying the model, and a set of extra properties may be configured, including:

- inference server-specific arguments
- load balancing strategy and properties
- scaling configuration (min/max/default replicas, scale delays and request targets)
- Resource confguration (e.g., run profile), environments and secrets (e.g., reference to ``HF_TOKEN`` if needed for accessing Huggingface resources)

## Management with SDK

Check the [SDK runtime documentation](https://scc-digitalhub.github.io/sdk-docs/reference/runtimes/modelserve/overview/) for more information.
