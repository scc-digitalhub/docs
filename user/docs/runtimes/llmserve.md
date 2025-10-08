# LLM Model Serving Runtime

**LLM Model serving runtime** aims at supporing the possibility to expose the LLM models as OpenAI-compatible APIs. For this purpose several different runtimes are available. Depending on the specific scenario requirements, the user may choose one or another approach.

- **HuggingFace Serving** (``huggingfaceserve``) runtime exposes standalone LLM models using KServe-based implementation. In a nutshell, this runtime allows for exposing LLMs using the [vLLM](https://docs.vllm.ai/) engine. The engine supports, in particular, completions and chat completions APIs compatible with the OpenAI protocol, embedding, and a series of other functions (like embeddings, fill mask, classification) using Open Inference Protocol. See corresponding [kserve](https://kserve.github.io/archive/0.14/modelserving/v1beta1/llm/huggingface/) documentation for the details. 
- **KubeAI-Text Serving** (``kubeai-text``) runtime that relies on [KubeAI](https://www.kubeai.org/) operator to expose model. Differently to the previous one, KubeAI serving deploys model while their serving is performed by KubeAI through a single channel. Also, this runtime relies on different engine, including vLLM, OLLama, and Infinity for different tasks. KubeAI supports also serving multiple LoRA adapters, autoscaling, and many other useful options for production-ready environments. 

## Huggingface Serve runtime

The specification of the HuggingfaceServe runtime functions consists of the following elements:

- ``path`` defining the URL of the model, either from the platform storage or from HuggingFace catalog (e.g., 'huggingface://Qwen/Qwen2.5-0.5B')
- ``model`` defining the name of the exposed model 
- and optional base image to use for serving the model if different from the one used by the platform by default

The runtime supports the ``serve`` action that may specify further deployment details including

- backend engine type (vLLM or custom Kserve implementation called "huggingface")
- inference task (e.g., ``sequence_classification``, ``fill_mask``, ``text_generation``, ``text_embedding``, etc)
- Specific parameters refering to the context length, data types, logging properties, tokenizer revision, engine args, etc.
- Resource confguration (e.g., run profile), environments and secrets (e.g., reference to ``HF_TOKEN`` if needed for accessing Huggingface resources)

Once deployed, a model is exposed with the corresponding Kubernetes service. The sevice endpoint is avaialble as a part of the ``status/service`` data of the run.

## KubeAI Text runtime

KubeAI Text runtime relies on KubeAI platform for model serving. In this case, for each serve action performed with this runtime a corresponding deployment is created, while no dedicated service is exposed - the models are service by KubeAI service directly.

There are different advantages of using KubeAI deployment, which include

- possibility to use multiple backend engines optimized for different goals. For example OLLama is best suited for testing models without GPU, while vLLM suites better for GPU-based environments.
- possibility to serve multiple models simultaneously through LoRA adapters. In this case one single base model + a list of different fine-tuned adapters are served on the same resources, while being made available indipendently.
- possibility to configure more efficient resource management with autoscaling and scale profiles.
- use of configurable prefix caching.
- Full OpenAI compatibility (completions, chat completions, embeddings)

The specification of the KubeAI text runtime amounts to defining

- base model URL (from S3 storage or from HuggingFace catalog)
- list of adapters (from S3 storage or from HuggingFace catalog)
- name of the model to expose
- Model task or feature: text generation (default) or embedding
- Backend engine: vLLM, OLLama, or Infinity (for embeddings only)
- optional base image for serving

The ``serve`` action allows for deploying the model and adapters, and a set of extra properties may be configured, including

- inference server-specific arguments
- load balancing strategy and properties
- prefix cache length
- scaling configuration (min/max/default replicas, scale delays and request targets)
- Resource confguration (e.g., run profile), environments and secrets (e.g., reference to ``HF_TOKEN`` if needed for accessing Huggingface resources)

!!! note "Using GPU for model seving"

    Please note that in case of large models for text generation task the usage of the corresponding GPU-based profiles may be required.


When deployed, the corresponding ``serve`` run specification contains extra information for using the LLM model. This includes

- the base URL of the kube AI environment to use by the clients
- the name of the deployed model and adapters to be used in the OpenAI requests
- LLM metadata - feature information, engine, base model, etc

## Management with SDK

Check the [SDK runtime documentation](https://scc-digitalhub.github.io/sdk-docs/reference/runtimes/modelserve/overview/) for more information.
