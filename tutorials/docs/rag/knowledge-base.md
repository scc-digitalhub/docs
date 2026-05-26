# Building the knowledge base

We now define the process to extract text content from the PDF file and generate embeddings from it.

## Text extraction

### Deploy a text extraction service

We will use [Apache Tika](https://tika.apache.org/), a tool for extracting text from a variety of formats. Create the function, run it and obtain the URL of the service:

```python
tika_function = project.new_function("tika", kind="container", image="apache/tika:latest-full")
```

```python
tika_run = tika_function.run("serve", service_ports = [{"port": 9998, "target_port": 9998}], wait=True)
```

```python
service = tika_run.refresh().status.service
print("Service status:", service)
```

```python
TIKA_URL = tika_run.status.to_dict()["service"]["url"]
print(TIKA_URL)
```

### Extract the text

We create a python function which will read an artifact from the platform's repository and leverage the Tika service to extract the textual content and write it to a HTML file.

```python
extract_function = project.new_function(
    name="extract",
    kind="python",
    python_version="PYTHON3_10",
    code_src="src/extract.py",
    handler="extract_text"
)
```

We store the PDF file as artifact and download it. You are free to change the address to whichever PDF file you would like.

```python
pdf = project.new_artifact("document.pdf",kind="artifact", path="https://raw.githubusercontent.com/scc-digitalhub/digitalhub-tutorials/master/s7-rag/resources/document.pdf")
pdf.download("document.pdf")
```

Then, we run the function by passing it the artifact and the URL to Tika:

```python
extract_run = extract_function.run("job", inputs={"artifact": pdf.key}, parameters={"tika_url": TIKA_URL}, wait=True)
```

Let's read the file and check the content is correct:

```python
html_artifact = project.get_artifact("document.pdf_output.html")
html_artifact.download()
with open('./artifact/output.html', 'r') as file:
    file_content = file.read()
    print(file_content)
```

## Embeddings

Embeddings are vectors of floating-point numbers that represent words and indicate how strong the connection between certain words is.

We need to deploy a suitable model to generate embeddings from the extracted text.

```python
embed_function = project.new_function(
    "embed",
    kind="kubeai-text",
    model_name="embmodel",
    features=["TextEmbedding"],
    engine="VLLM",
    url="hf://thenlper/gte-base",
)
```

```python
embed_run = embed_function.run("serve", wait=True)
```

```python
status = embed_run.refresh().status
print("Service status:", status.state)
```

```python
EMBED_URL = status.to_dict()["service"]["url"]
EMBED_MODEL = status.to_dict()["openai"]["model"]
print(f"service {EMBED_URL} with model {EMBED_MODEL}")
```

Let's check that the model is ready. We need the OpenAI client installed:

```
%pip install -qU openai
```

```python
from openai import OpenAI

client = OpenAI(api_key="ignored", base_url=f"{EMBED_URL}/v1")
response = client.embeddings.create(
    input="Your text goes here.",
    model=EMBED_MODEL
)
```

```python
response
```

### Embedding generation
We define a function to read the text from the repository and push the data into the vector store.

```python
embedder_function = project.new_function(
    name="embedder",
    kind="python",
    python_version="PYTHON3_10",
    requirements=[
        "transformers==4.50.3",
        "psycopg_binary",
        "openai",
        "langchain-text-splitters",
        "langchain-community",
        "langgraph",
        "langchain-core",
        "langchain-huggingface",
        "langchain_postgres",
        "langchain[openai]",
        "beautifulsoup4",
    ],
    code_src="src/embedder.py",
    handler="process",
)
```

Parameters are as follows:

- Embed model is served at `EMBED_URL` with `EMBED_MODEL`.
- Input artifact (HTML) is `html_artifact`.

```python
embedder_run = embedder_function.run(
    "job",
    inputs={"input": html_artifact.key},
    envs=[
        {
            "name": "EMBEDDING_SERVICE_URL",
            "value": EMBED_URL
        },
        {    "name": "EMBEDDING_MODEL_NAME",
            "value": EMBED_MODEL,
        }
    ],
    wait=True,
)
```

Check that the run has completed:

```python
embedder_run.status.state
```
