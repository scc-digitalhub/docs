# Managing LLM Models with KubeAI Runtime

To support the set of LLM scenarios within the platform it is possible to use the KubeAI runtime when the [KubeAI](https://www.kubeai.org/) operator is
enabled. 

For what concerns LLM tasks, currently KubeAI runtime allows for deploying the models for the following tasks:

- ``TextGeneration``: text generation tasks with  the OpenAI-compatible API
- ``TextEmbedding``: creating embeddings from the text following the OpenAI-compatible API

To accomplish this, it is possible to use one of the KubeAI-supported runtimes, namely [vLLM](https://docs.vllm.ai/), [OLlama](https://ollama.com/), and [Infinity](https://michaelfeil.eu/infinity). in case of vLLM also adapters are supported.

For details about the specification, see the corresponding section of [Modelserve](../../runtimes/modelserve.md) reference.

## Exposing Text Generation Models

To expose the text generation model, it is possible to use Core UI or Python SDK. To define the corresponding function, the following parameters should be specified:

- model name
- inference engine (one of ``VLLM``, ``OLlama``, ``Infinity``) to use
- model URL. Currently the model can be loaded either from HuggingFace (``hf://`` prefix), from S3 storage of the platform (``s3://``), or OLlama compatible model (``ollama://`` prefix in case of OLlama engine).
- feature should be set to ``TextGeneration``.
- in case of vLLM engine it is also possible to add list of adapters for the main model. Each adapter is specified with its own name and URL of the corresponding adapter.

To serve the text generation model, the function should be run with the ``serve`` action, specifying additional parameters. In particular, it may be necessary to specify the HW profile to use with number of processors (since GPU may be required) or resource specification, and further parameters and arguments accepted by the KubeAI model specification:

- ``args``: command-line arguments to pass to the engine
- ``env``: custom environment values (key-value pair)
- ``secrets``: project secrets to pass the values. For example, in case HuggingFace token is needed, create ``HF_TOKEN`` secret at the project with the token value to use. 
- ``files``: extra file specifications for the deployment
- ``scaling``: scaling specification as of KubeAI documentation
- ``caching_profile``: cache profile as of KubeAI documentation.

For example to deploy a model with an adapter from HuggingFace, the following procedure may be used:

```python
llm_function = project.new_function("llm",
                                    kind="kubeai-text",
                                    model_name="tinyllama-chat",
                                    url="hf://TinyLlama/TinyLlama-1.1B-Chat-v0.3",
                                    engine="VLLM",
                                    features=["TextGeneration"],
                                    adapters=[{"name": "colorist", "url": "hf://jashing/tinyllama-colorist-lora"}])


llm_run = llm_function.run(action="serve",
                           profile="1xa100",
                           args=["--enable-prefix-caching", "--max-model-len=8192"])                                    
```

Once deployed, the model is available and it is possible to call the OpenAI-compatible API from within the platform.
The run status (see ``openai`` and ``service`` section) contains the information about the name of the model and the endpoints
of the KubeAI API exposed 

```python
import requests 

model_name = f"tinyllama-chat-123xyz_colorist"

input = {"prompt": "Hi", "model": model_name}

res = requests.post(f"http://{KUBEAI_ENDPOINT}/openai/v1/completions", json=input)
print(res.json())
```

By default, the ``KUBEAI_ENDPOINT`` is ``kubeai:80``.

!!! note "Model name"

    Please note how the model name is defined: it is composed of the name of the model as specified in the function and the random value. In case of adapter the name of adapter should be added: ``<model_name>-<random>_<adapter-name>``.

It is also possible to use OpenAI client for interacting with the model. 

## Exposing Text Embedding Models

To expose the text embedding model, it is possible to use Core UI or Python SDK. To define the corresponding function, the following parameters should be specified:

- model name
- inference engine (one of ``VLLM``, or ``Infinity``) to use
- model URL. Currently the model can be loaded either from HuggingFace (``hf://`` prefix), from S3 storage of the platform (``s3://``).
- feature should be set to ``TextEmbedding``.

To serve the text emvedding model, the function should be run with the ``serve`` action, specifying additional parameters. 
Normally embedding models do not require extra resources. However,  further parameters and arguments accepted by the KubeAI model specification may be added:

- ``args``: command-line arguments to pass to the engine
- ``env``: custom environment values (key-value pair)
- ``secrets``: project secrets to pass the values 
- ``files``: extra file specifications for the deployment
- ``scaling``: scaling specification as of KubeAI documentation
- ``caching_profile``: cache profile as of KubeAI documentation.

For example to deploy a model from HuggingFace, the following procedure may be used:

```python
llm_function = project.new_function("llm",
                                    kind="kubeai-text",
                                    model_name="embedding",
                                    url="hf://BAAI/bge-small-en-v1.5",
                                    engine="Infinity",
                                    features=["TextEmbedding"])


llm_run = llm_function.run(action="serve")                                    
```

Once deployed, the model is available and it is possible to call the OpenAI-compatible API from within the platform or OpenAI client:

```python
from openai import OpenAI

model_name = f"embedding-123qwe"

client = OpenAI(api_key="ignored", base_url=f"http://{KUBEAI_ENDPOINT}/openai/v1")
response = client.embeddings.create(
    input="Your text goes here.",
    model=model_name
)
```

By default, the ``KUBEAI_ENDPOINT`` is ``kubeai:80``.
