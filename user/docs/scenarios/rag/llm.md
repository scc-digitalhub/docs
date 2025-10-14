# LLM

The first step is to deploy and serve a pre-trained Large Language Model. We'll work with the [Llama model](https://ollama.com/library/llama3.2:1b) for text generation.

## Project initialization

Initialize a project on the platform:

```python
import digitalhub as dh
import getpass as gt

USERNAME = gt.getuser()

project = dh.get_or_create_project(f"{USERNAME}-tutorial-project")
print(project.name)
```

## Model configuration

We'll create a function to serve the LLama3.2 model directly. The model path may use different protocols, such as `ollama://` or `hf://`, to directly reference models from the corresponding hub, without manual downloading.

```python
llm_function = project.new_function(
    name="llama32-1b",
    kind="kubeai-text",
    model_name=f"{USERNAME}-model",
    url="ollama://llama3.2:1b",
    engine='OLlama',
    features=['TextGeneration']
)
```

## Model serving

To deploy the model, we use a GPU profile (`1xa100`) to accelerate the generation.

```python
llm_run = llm_function.run("serve", profile="1xa100", wait=True)
```

Let's check that our service is running and ready to accept requests:

```python
service = llm_run.refresh().status.service
print("Service status:", service)
```

When the service is ready, we need to wait for the model to be downloaded and deployed.

```python
status = llm_run.refresh().status.k8s.get("Model")['status']
print("Model status:", status)
```

Once ready, we save the URL and model:

```python
CHAT_URL = llm_run.status.to_dict()["service"]["url"]
CHAT_MODEL = llm_run.status.to_dict()["openai"]["model"]
print(f"service {CHAT_URL} with model {CHAT_MODEL}")
```

## Test the LLM API

Let's test our deployed model with a prompt:

```python
model_name =llm_run.refresh().status.k8s.get("Model").get("metadata").get("name")
json_payload = {'model': model_name, 'prompt': 'Describe MLOps'}
```

```python
import pprint
pp = pprint.PrettyPrinter(indent=2)
result = llm_run.invoke(model_name=model_name, json=json_payload, url=service['url']+'/v1/completions').json()
print("Response:")
pp.pprint(result)
```

The response contains the answer, as well as some usage parameters.
