# Examples

## MLflow Model Example

```python
import digitalhub as dh

project = dh.get_or_create_project("my_project")

function = project.new_function(name="mlflow-serve-function",
                                kind="mlflowserve",
                                path=model.key)

run = function.run(action="serve")
```

## MLflow Build Example

```python
import digitalhub as dh

project = dh.get_or_create_project("my_project")

function = project.new_function(name="mlflow-build-function",
                                kind="mlflowserve",
                                path=model.key)

build_run = function.run(
    action="build",
    instructions=["pip install -r requirements.txt"]
)
```

## Scikit-Learn Model Example

```python
function = project.new_function(name="sklearn-serve-function",
                                kind="sklearnserve",
                                path=model.key)

run = function.run(action="serve")
```

## KubeAI Text Model Example

```python
function = project.new_function(
    name="kubeai-text-function",
    kind="kubeai-text",
    url="hf://mistralai/Mistral-7B-v0.1",
    features=["TextGeneration"],
    engine="VLLM"
)

run = function.run(action="serve")
```

## KubeAI Speech Model Example

```python
function = project.new_function(
    name="kubeai-speech-function",
    kind="kubeai-speech",
    url="hf://openai/whisper-large-v3",
    features=["SpeechToText"],
    engine="FasterWhisper"
)

run = function.run(action="serve")
```

## vLLM Text Model Example

```python
function = project.new_function(
    name="vllm-text-function",
    kind="vllmserve-text",
    url="hf://meta-llama/Meta-Llama-3-8B-Instruct",
)

run = function.run(action="serve")
```

## Service Invocation

```python
# Prepare input data
input_data = {"inputs": "Your input text here"}

# Invoke the service
response = run.invoke(json=input_data)

# Run invoke method accept requests.request parameters.
# It accepts also url parameter. The url MUST start
# with a valid HTTP scheme (http:// or https://) and should
# include the service url. To check the service url:
run.status.service['url']
```

## Tutorials

Find additional examples in the [tutorial repository](https://github.com/scc-digitalhub/digitalhub-tutorials) of the DSLab GitHub organization.
