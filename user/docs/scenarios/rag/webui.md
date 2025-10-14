# Agent Web UI

Finally, we build a web interface to test the agent. The interface will be available via browser by proxying the port through the workspace.

## Deploy the UI

We use [Streamlit](https://docs.streamlit.io/) to serve a simple webpage with an input field connected to the agent API.

Streamlit is a Python framework to create browser applications with little code.

```
%pip install -qU streamlit langgraph langchain-core langchain-postgres "langchain[openai]" psycopg_binary
```

Add the models' names and service URLs to the environment file:

```python
with open("./streamlit.env", "w") as env_file:
    env_file.write(f"CHAT_MODEL_NAME={CHAT_MODEL}\n")
    env_file.write(f"CHAT_SERVICE_URL={CHAT_URL}\n")
    env_file.write(f"EMBEDDING_MODEL_NAME={EMBED_MODEL}\n")
    env_file.write(f"EMBEDDING_SERVICE_URL={EMBED_URL}\n")
```

Write the function implementing the RAG UI to file:

```python
%%writefile 'rag-streamlit-app.py'
import os
import bs4
import streamlit as st
from dotenv import load_dotenv
from langchain import hub
from langchain.chat_models import init_chat_model
from langchain_core.documents import Document
from langchain_openai import OpenAIEmbeddings
from langchain_postgres import PGVector
from langgraph.graph import START, StateGraph
from openai import OpenAI
from pathlib import Path
from typing_extensions import List, TypedDict

# Read environment variables
add_env_path = Path('.') / 'streamlit.env'
load_dotenv(dotenv_path=add_env_path, override=True)

PG_USER = os.environ["DB_USERNAME"]
PG_PASS = os.environ["DB_PASSWORD"]
PG_HOST = os.environ["DB_HOST"]
PG_PORT = os.environ["DB_PORT"]
DB_NAME = os.environ["DB_DATABASE"]
ACCESS_TOKEN = os.environ["DHCORE_ACCESS_TOKEN"]

chat_model_name = os.environ["CHAT_MODEL_NAME"]
chat_service_url = os.environ["CHAT_SERVICE_URL"]
embedding_model_name = os.environ["EMBEDDING_MODEL_NAME"]
embedding_service_url = os.environ["EMBEDDING_SERVICE_URL"]
PG_CONN_URL = (
    f"postgresql+psycopg://{PG_USER}:{PG_PASS}@{PG_HOST}:{PG_PORT}/{DB_NAME}"
)

# Embedding model
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

custom_embeddings = CEmbeddings(api_key="ignored")

# Vector store
vector_store = PGVector(
    embeddings=custom_embeddings,
    collection_name=f"{embedding_model_name}_docs",
    connection=PG_CONN_URL,
)

# Chat model
os.environ["OPENAI_API_KEY"] = "ignore"
llm = init_chat_model(chat_model_name, model_provider="openai", base_url=f"{chat_service_url}/v1/")

# Define prompt and operations
prompt = hub.pull("rlm/rag-prompt")

class State(TypedDict):
    question: str
    context: List[Document]
    answer: str

def retrieve(state: State):
    retrieved_docs = vector_store.similarity_search(state["question"])
    return {"context": retrieved_docs}

def generate(state: State):
    docs_content = "\n\n".join(doc.page_content for doc in state["context"])
    messages = prompt.invoke({"question": state["question"], "context": docs_content})
    response = llm.invoke(messages)
    return {"answer": response.content}

# Define graph of operations
graph_builder = StateGraph(State).add_sequence([retrieve, generate])
graph_builder.add_edge(START, "retrieve")
graph = graph_builder.compile()

# Streamlit setup
st.title("RAG App")
st.write("Welcome to the RAG (Retrieval-Augmented Generation) app.")
if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

qa = st.container()

with st.form("rag_form", clear_on_submit=True):
    question = st.text_input("Question", "")
    submit = st.form_submit_button("Submit")
    
if submit:
    # Load and chunk contents
    if question:
        st.session_state.messages.append({"role": "user", "content": question})
        with qa.chat_message("user"):
            st.write(question)
    
        response = graph.invoke({"question": question})
        st.session_state.messages.append({"role": "assistant", "content": response["answer"]})
        with qa.chat_message("assistant"):
            st.write(response["answer"])
    else:
        with qa.chat_message("assistant"):
            st.write("You didn't provide a question!")
```

## Launch and test the Streamlit app

This command launches the Streamlit app, based on the file written by the previous cell. To access the app, you will need to forward port 8501 in Coder. 

Try asking the app a question.

```
!streamlit run rag-streamlit-app.py --browser.gatherUsageStats false
```
