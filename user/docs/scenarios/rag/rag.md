# RAG application with LangChain

This step will define the agent which connects the embedding model, the chat model and the vector store to fullfill the RAG scenario.

You should have the URLs and models for the latest `RUNNING` runs of the two functions from the previous steps of the scenario:

```python
print(f"Service {EMBED_URL} with model {EMBED_MODEL}")
print(f"Service {CHAT_URL} with model {CHAT_MODEL}")
```

## Create the agent

We will register a python function implementing the RAG agent with [LangChain](https://python.langchain.com/docs/introduction/):

```python
serve_func = project.new_function(
    name="rag-service", 
    kind="python", 
    python_version="PYTHON3_10",
    code_src="src/serve.py",     
    handler="serve",
    init_function="init",
    requirements=["transformers==4.50.3", "psycopg_binary", "openai", "langchain-text-splitters", "langchain-community", "langgraph", "langchain-core", "langchain-huggingface", "langchain_postgres", "langchain[openai]"]
)
```

Then, we can run an instance connecting the model services together. It may take a while for this run to finish initialization. If the execution fails, it is probably due to the large number of dependencies required.

```python
serve_run = serve_func.run(
    action="serve",
    resources={
        "cpu": {"limits": "8", "requests": "4"},
        "mem": {"limits": "8Gi", "requests": "4Gi"},
    },
    envs=[
            {"name": "CHAT_MODEL_NAME", "value": CHAT_MODEL},
            {"name": "CHAT_SERVICE_URL", "value": CHAT_URL},
            {"name": "EMBEDDING_MODEL_NAME", "value": EMBED_MODEL},
            {"name": "EMBEDDING_SERVICE_URL", "value": EMBED_URL}
         ],
    wait=True
)
```

```python
AGENT_URL = serve_run.status.to_dict()["service"]["url"]
print(AGENT_URL)
```

To test our API, we make a call to the service endpoint, providing JSON text with an example question.

```python
import requests

res = requests.post(f"http://{AGENT_URL}",json={"question": "What is the idea behind SVMs?"})
print(res.json())
```
