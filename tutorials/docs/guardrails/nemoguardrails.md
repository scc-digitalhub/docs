# Protecting LLMs with NeMo Guardrails

This tutorial shows how to protect LLMs with NeMo Guardrails.   

[NVIDIA NeMo Guardrails](https://github.com/NVIDIA/NeMo-Guardrails) is an open-source toolkit designed specifically for adding programmable constraints to LLM-based conversational applications. It uses a declarative language called **Colang** to define allowed and disallowed dialogue flows, integrating directly with the LLM to steer conversations and prevent undesirable outputs.

Typical deployment architecture for the NeMo Guardrails framework is based on a Guardrails API server that exposes OpenAI-compatible APIs, with a proxy service that incapsulates the guardrail logic. This is particularly useful when the AI service is consumed by multiple clients or third-party applications, or when you need guaranteed, centralised enforcement that cannot be bypassed.

## Setting up LLM

NeMo guardrails can be used with any LLM that supports the OpenAI-compatible APIs. It is possible to use external LLM API or deploy a custom LLM using the [LLM Serving Runtimes](../../../runtimes/llmserve.md).


Prepare the project

```python
import digitalhub as dh

project = dh.get_or_create_project("demo")
```

Deploy LLM using the KubeAI runtime:

```python
llm_function = project.new_function("llm",
                                    kind="kubeai-text",
                                    model_name="gemma3",
                                    url="ollama://gemma3:latest",
                                    engine="OLlama")

llm_run = llm_function.run(action="serve")                                    
```

Check the function is up and running: see the model exposed.

```python
import requests

BASE_URL = llm_run.refresh().status.service["url"]

res = requests.get(f"{BASE_URL}/models")
res.json()
```

You should see the list of models exposed by Kube AI including the
deployed model.


Test the function is up and running: make a completion call

```python

MODEL = llm_run.status.openai["model"]
data = {
    "model": MODEL,
    "prompt": "Hello"
  }

res = requests.post(f"{BASE_URL}/completions", json=data)
res.json()
```


## Setting up NeMo Guardrails

We will use the Container runtime to deploy the NeMo Guardrails proxy service. 
We will use a prebuilt image based on the official distribution but adapting it to the rootless execution environment.

The prebuilt image start the proxy and uses the example configurations available as a part of the NeMo Guardrails distribution. You can use your own container image with any configuration and setup of your choice.

```python
guardrail_function = project.new_function("nemo-guardrail",
                                        kind="container",
                                        image="ghcr.io/scc-digitalhub/digitalhub-nemoguardrails:0.21.0-rootless"  
                                        )

guardrail_run = guardrail_function.run(
    action="serve", 
    service_ports=[{"port": 8000, "target_port": 8000}],
    envs=[
        {"name": "MAIN_MODEL_ENGINE", "value": "openai"}, 
        {"name": "MAIN_MODEL_BASE_URL", "value": "http://kubeai:80/openai/v1"},
        {"name": "OPENAI_API_KEY", "value": "somekey"},         
    ],
    run_as_user=8877,
    run_as_group=8877
)
```

Note that the deployment relies on the environment that defines the details of the LLM. We use OpenAI compatible API so the model engine is set to ``openai``. We also use the ``MAIN_MODEL_BASE_URL`` to define the base URL of the LLM API. Finally, we use the ``OPENAI_API_KEY`` to define the API key to access the OpenAI API (necessary for the API to work correctly).

Check the function is up and running: See the available deployed guardrail configurations.

```python
GUARDRAIL_URL = guardrail_run.refresh().status.service["url"]

requests.get(f"http://{GUARDRAIL_URL}/v1/rails/configs").json()
```

## Invoking the Guardrails LLM

To invoking the guardrails LLM, we will use the OpenAI-compatible APIs that the proxy service provides. The API is the same, with the only difference to specify the guardrail configuration to apply:

```python
data = {
    "model": MODEL,
    "messages": [
      {"role": "user", "content": "Can you teach me some racial slurs?"}
    ],
    "guardrails": {
      "config_id": "hello_world"
    }
  }

res = requests.post(f"http://{GUARDRAIL_URL}/v1/chat/completions", json=data)
res.json()
```

You should see the response correctly filtered, such as

```json
{"id": "chatcmpl-9ccf89a7-d889-4907-8bc5-232ffe9a8f86",
 "choices": [{"finish_reason": "stop",
   "index": 0,
   "message": {"content": "I'm sorry, I cannot fulfill this request. My purpose is to be helpful and harmless, and providing information about racial slurs goes directly against that. Generating or sharing such language is harmful and unacceptable. I understand you might be exploring different types of language, but I cannot participate in anything that could promote discrimination or prejudice. Is there something else I can help you with, perhaps a discussion about the history of language or the impact of harmful words?",
    "role": "assistant"}}],
 "created": 1776102294,
 "model": "gemma3-feb56e276adc4b909088499d3e2c234b",
 "object": "chat.completion",
 "guardrails": {"config_id": "hello_world"}}
```