# Speech to Text Serving Runtime

**Speech to Text serving runtime** (kubeai-speech) aims at supporing the possibility to expose the automated speech recognition functionality as OpenAI-compatible transcriptions API. 
 
For this purpose the runtime that relies on [KubeAI](https://www.kubeai.org/) operator to expose model using the FasterWhisper engine. The serving is performed by KubeAI as in case of KubeAI Text runtime. 

The specification of the KubeAI speech runtime amounts to defining

   model URL (from S3 storage or from HuggingFace catalog, e.g., ``hf://Systran/faster-whisper-medium.en``)
- name of the model to expose
- optional base image for serving

The ``serve`` action allows for deploying the model, and a set of extra properties may be configured, including

- inference server-specific arguments
- load balancing strategy and properties
- scaling configuration (min/max/default replicas, scale delays and request targets)
- Resource confguration (e.g., run profile), environments and secrets (e.g., reference to ``HF_TOKEN`` if needed for accessing Huggingface resources)

## Management with SDK

Check the [SDK runtime documentation](https://scc-digitalhub.github.io/sdk-docs/reference/runtimes/modelserve/overview/) for more information.
