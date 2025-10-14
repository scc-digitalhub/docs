# Retrieval-Augmented Generation

In this scenario, we create a *Retrieval-Augmented Generation* (RAG) application, a chatbot able to take new documents, learn from their contents and answer questions related to them.

When a LLM model is asked a question concerning information not found in the data it has been trained on, it is unable to provide a correct response and will provide a (perhaps even somewhat convincing) wrong answer or, at best, admit it doesn't know.

Rather than re-train the model on a larger dataset, the idea is to provide a document - such as a file or a link - to be analyzed and used as context for the response.

## Scenario

In this scenario, we will face a common situation, where the question we wish to ask is related to the information contained within a *PDF* file. As the subject is so precise, existing LLM models likely will not be able to give a good answer right away, but by providing such document and letting the application study it, it will become able to answer questions related to the document's contents.

The steps will be as follows:

- Prepare a LLM model
- Extract text from the PDF file and generate embeddings
- Prepare the RAG application
- Create a UI for the application

## Code for the functions

Three functions will be used during this tutorial. To prepare them in advance, run the following code cells on your Jupyter notebook.

Create the directory for the code:

```python
from pathlib import Path
Path("src").mkdir(exist_ok=True)
```

Function for text extraction:

```python
%%writefile "src/extract.py"
import requests

def extract_text(tika_url, artifact, project):
    print(f"Downloading artifact {artifact.name}...")
    fp = artifact.as_file()
    if not (tika_url)[:4] == "http": 
        tika_url = "http://"+tika_url
    print(f"Sending {fp} to {tika_url}...")    
    response = requests.put(tika_url+"/tika",headers={"Accept":"text/html"}, data=open(fp,'rb').read())
    if response.status_code == 200:
        print("Extracted text with success")
        res = "/tmp/output.html"
        with open(res, "w") as tf:
            tf.write(response.text)
        project.log_artifact(kind="artifact", name=artifact.name+"_output.html", source=res)
        return res
    else:
        print(f"Received error: {response.status_code}")
        raise Exception("Error")

```

Function for embedding generation:

```python
%%writefile "src/embedder.py"
import bs4
from langchain_community.document_loaders import WebBaseLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_postgres import PGVector
import os
import requests
from langchain_openai import OpenAIEmbeddings
from openai import OpenAI


PG_USER = os.environ["DB_USERNAME"]
PG_PASS = os.environ["DB_PASSWORD"]
PG_HOST = os.environ["DB_HOST"]
PG_PORT = os.environ["DB_PORT"]
DB_NAME = os.environ["DB_DATABASE"]
ACCESS_TOKEN = os.environ["DHCORE_ACCESS_TOKEN"]


def process(input):
    print(f"process input {input.id}...")
    url = (
        os.environ["DHCORE_ENDPOINT"]
        + "/api/v1/-/"
        + input.project
        + "/"
        + input.kind
        + "s/"
        + input.id
        + "/files/download"
    )
    print(f"request download link for input {input.id} from {url}")
    res = requests.get(url, headers={"Authorization": f"Bearer {ACCESS_TOKEN}"})
    print(f"Download url status {res.status_code}")
    if res.status_code == 200:
        j = res.json()
        print(f"{j}")
        #if "url" in j:
            #return embed(j["url"])

    print("End.")


def embed(url):
    PG_CONN_URL = (
        f"postgresql+psycopg://{PG_USER}:{PG_PASS}@{PG_HOST}:{PG_PORT}/{DB_NAME}"
    )
    print(f"process url {url}...")
    embedding_service_url = os.environ["EMBEDDING_SERVICE_URL"]
    embedding_model_name = os.environ["EMBEDDING_MODEL_NAME"]
    
    class CEmbeddings(OpenAIEmbeddings):
        def embed_documents(self, docs):
            client = OpenAI(api_key="ignored", base_url=f"{embedding_service_url}/v1")
            emb_arr = []
            for doc in docs:
                #sanitize string: replace NUL with spaces
                d=doc.replace("\x00", "-")
                embs = client.embeddings.create(
                    input=d,
                    model=embedding_model_name
                )
                emb_arr.append(embs.data[0].embedding)
            return emb_arr

    custom_embeddings = CEmbeddings(api_key="ignore")

    vector_store = PGVector(
        embeddings=custom_embeddings,
        collection_name=f"{embedding_model_name}_docs",
        connection=PG_CONN_URL,
    )

    loader = WebBaseLoader(
        web_paths=(url,),
        bs_kwargs=dict(
            parse_only=bs4.SoupStrainer(
                class_=("post-content")
            )
        ),
    )    
    docs = loader.load()
    print(f"document loaded, generate embeddings...")

    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
    all_splits = text_splitter.split_documents(docs)
    print(f"store documents in vector db...")

    vector_store.add_documents(documents=all_splits)
    print("Done.")

```

Function to serve the RAG application:

```python
%%writefile "src/serve.py"
import bs4
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_postgres import PGVector
import os
from langchain_openai import OpenAIEmbeddings
from openai import OpenAI

from langchain import hub
from langchain_core.documents import Document
from typing_extensions import List, TypedDict

from langgraph.graph import START, StateGraph
from langchain.chat_models import init_chat_model

PG_USER = os.environ["DB_USERNAME"]
PG_PASS = os.environ["DB_PASSWORD"]
PG_HOST = os.environ["DB_HOST"]
PG_PORT = os.environ["DB_PORT"]
DB_NAME = os.environ["DB_DATABASE"]
ACCESS_TOKEN = os.environ["DHCORE_ACCESS_TOKEN"]

class State(TypedDict):
    question: str
    context: List[Document]
    answer: str


def init(context):
    chat_model_name = os.environ["CHAT_MODEL_NAME"]
    chat_service_url = os.environ["CHAT_SERVICE_URL"]
    embedding_model_name = os.environ["EMBEDDING_MODEL_NAME"]
    embedding_service_url = os.environ["EMBEDDING_SERVICE_URL"]

    class CEmbeddings(OpenAIEmbeddings):
        def embed_documents(self, docs):
            client = OpenAI(api_key="ignored", base_url=f"{embedding_service_url}/v1")
            emb_arr = []
            for doc in docs:
                embs = client.embeddings.create(
                    input=doc,
                    model=embedding_model_name
                )
                emb_arr.append(embs.data[0].embedding)
            return emb_arr

    custom_embeddings = CEmbeddings(api_key="ignored")
    PG_CONN_URL = (
        f"postgresql+psycopg://{PG_USER}:{PG_PASS}@{PG_HOST}:{PG_PORT}/{DB_NAME}"
    )
    vector_store = PGVector(
        embeddings=custom_embeddings,
        collection_name=f"{embedding_model_name}_docs",
        connection=PG_CONN_URL,
    )
    
    os.environ["OPENAI_API_KEY"] = "ignore"

    llm = init_chat_model(chat_model_name, model_provider="openai", base_url=f"{chat_service_url}/v1/")
    prompt = hub.pull("rlm/rag-prompt")

    def retrieve(state: State):
        retrieved_docs = vector_store.similarity_search(state["question"])
        return {"context": retrieved_docs}
    
    def generate(state: State):
        docs_content = "\n\n".join(doc.page_content for doc in state["context"])
        messages = prompt.invoke({"question": state["question"], "context": docs_content})
        response = llm.invoke(messages)
        return {"answer": response.content}

    graph_builder = StateGraph(State).add_sequence([retrieve, generate])
    graph_builder.add_edge(START, "retrieve")
    graph = graph_builder.compile()

    setattr(context, "graph", graph)

def serve(context, event):
    graph = context.graph
    context.logger.info(f"Received event: {event}")
    
    if isinstance(event.body, bytes):
        body = json.loads(event.body)
    else:
        body = event.body
        
    question = body["question"]
    response = graph.invoke({"question": question})
    return {"answer": response["answer"]}

```