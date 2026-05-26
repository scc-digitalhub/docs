# Protecting LLMs with Guardrails

!!! note IMPORTANT

    In this scenario we expect the platform is equipped with the **Envoy Gateway** infrastructure configured for guardrails management. 


This tutorial shows how to protect LLMs with Guardrails.

We will use a generic LLM to be protected by guardrails, specifically the OpenAI `/v1/completions` API calls.

## Setting up the Service

To test the scenario, we use a generic LLM model, such as `gemma3` and usr the KubeAI runtime for deploying the model in the platform. 

```python
llm_function = project.new_function("llm",
                                    kind="kubeai-text",
                                    model_name="gemma3",
                                    url="ollama://gemma3:latest",
                                    engine="OLlama")

```

Run and test the unprotected function:

```python
llm_run = llm_function.run(action="serve")

# Test the function
import requests

BASE_URL = llm_run.refresh().status.service['url']
MODEL = llm_run.status.openai["model"]
data = {
    "model": MODEL,
    "prompt": "Hello!"
  }

res = requests.post(f"{BASE_URL}/completions", json=data)
res.json()
``` 

## Setting up the Guardrail

We will use a Guardrail implementation based on [GuardrailsAI](https://guardrailsai.com/guardrails/docs) framework. The framework targets LLM applications and provides a collection of predefined validators that can be used to enforce constraints on the output of the LLM.

Specifically, the function uses Toxic Language validator and blocks the inappropriate requests.

```python 
import nuclio_sdk
import os
import json
from guardrails import Guard, OnFailAction

def init_context(context: nuclio_sdk.Context):
    context.logger.info("Initializing guardrails...")
    from guardrails.hub import ToxicLanguage
    guard = Guard().use(
        ToxicLanguage, threshold=0.5, validation_method="sentence", on_fail="exception"
    )
    setattr(context, "guard", guard)

def handler_serve(context: nuclio_sdk.Context, event: nuclio_sdk.Event):
    if isinstance(event.body, bytes):
        body = json.loads(event.body)
    else:
        body = event.body
        
    prompt = body['prompt'] if 'prompt' in body else None

    if prompt:
        try:
            guard.validate(prompt) 
        except Exception as e:
            return context.Response(body="Toxic language used",
                            headers={},
                            content_type='text/plain',
                            status_code=400)

    return event.body
```

Register the function in platform and run it:

```python
guardrail_func = project.new_function(
                            name="toxic-guardrail",
                            kind="guardrail",
                            python_version="PYTHON3_10",
                            code_src="src/guardrail_service.py",
                            handler="handler_serve",
                            init_function="init_context",
                            processing_mode="preprocessor",
                            requirements=["guardrails-ai==0.5.0", "transformers==4.42.0"]
                           )
                                    
```

## Build the function image

The GuardrailsAI library is based on predefined or custom guardrail validators. Predefined validators may be obtained from the Guardrails AI hub, downloaded and deployed. In this scenario, we will use predefined guardrails that should be integrated in the service. To make it efficient, the guardrails should be integrated in the underlying container image and we will build it for this function.

First, we need an API KEY from Guardrails AI to access the hub. We will add to the project as a secret.

```python
secret = project.new_secret(name="GUARDRAILS_API_KEY",
                            secret_value="value")
```

To build the image for the function we will need to add some instructions to use Git, to authenticate to the hub, and to install the specific validator (toxic_language).

```python
build_run = guardrail_func.run(
                     action="build", 
                     secrets=["GUARDRAILS_API_KEY"],
                     instructions=[
                         "/opt/nuclio/uv/uv pip install --system  typer==0.9.0 click==8.1.7 guardrails-ai==0.5.0",
                         "apt-get update && apt-get install -y git",
                         "--mount=type=secret,id=GUARDRAILS_API_KEY,env=GUARDRAILS_API_KEY guardrails configure --enable-metrics --enable-remote-inferencing --token $GUARDRAILS_API_KEY",
                         "guardrails hub install hub://guardrails/toxic_language"
                     ]
                    )
```

We need to deploy the guard and protect LLM with it.

```python
guardrail_run = build_run.refresh().run(action="serve")
```

## Use the Guardrail to Protect the API

To protect the service instance with guardrails, we rely on the corresponding gateway and use Envoy Gateway extension for the runs. Specifically, when the service enable the extension, we obtain:

- the service exposed also behind the preconfigured service Envoy gateway (see the gatewayInfo in service status);
- if the guardrails are configured, the gateway controls the traffic using the ExtProc extension that interacts with the guardrails to implement pre/post processing logic. 

```python
llm_run = llm_function.run(action="serve", extensions=[{
    "kind": "envoygw",
    "name": "gw",
    "spec": {
        "guardrails": [guardrail_run.refresh().status.service['url']]
    }
}])
```

The protected endpoint of model gateway may be obtained as follows:

```python
PROTECTED_ENDPOINT = f"http://{run.status.gatewayInfo['gatewayEndpoint']}/v1"
```

Test the protected service:

```python
import requests

MODEL = llm_run.status.openai["model"]
data = {
    "model": MODEL,
    "prompt": "My landlord is an asshole!"
  }

res = requests.post(f"http://{PROTECTED_ENDPOINT}/completions", json=data)
res.text
```