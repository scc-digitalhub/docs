# Visualize data with Streamlit

We can take this one step further and visualize our data in a graph. We will make use of [Streamlit](https://streamlit.io/), a library to create web apps and visualize data by writing simple scripts.

## Setup

From the Jupyter notebook you've been using, write the result of the API call to a file:

``` python
with open("result.json", "w") as file:
    file.write(res['data'])
```

Create the script that Streamlit will run:

``` python
%%writefile 'streamlit-app.py'

import pandas as pd
import streamlit as st

rdf = pd.read_json('result.json', orient='records')

st.write("""My data""")
st.line_chart(rdf, x='codice spira', y='12:00-13:00')
```

## Launch app

Now, open a local shell and login to your Coder instance as follows. A tab will open on your browser, containing a token you must copy and paste to the shell (it may ask your credentials, if your browser isn't already logged in).
``` shell
coder login https://coder.my-digitalhub-instance.it
```

Connect to the workspace, port-forwarding via ssh:
``` shell
ssh -L 8501:localhost:8501 coder.my-jupyter-workspace
```

Install streamlit:
``` shell
pip install streamlit
```

Run streamlit:
``` shell
streamlit run streamlit-app.py --browser.gatherUsageStats false
```

Access `localhost:8501` on your browser to view the data!

![Streamlit image](../../../images/streamlit.png)

The graph we displayed is very simple, but you are welcome to experiment with more Streamlit features.

## As Docker container

Streamlit apps can be run as Docker containers. For this section, we will run the same application locally as a container, so you will need either Podman or Docker installed on your machine. Instructions refer to Podman, but if you prefer to use Docker, the commands are equivalent: simply replace instances of `podman` with `docker`.

Download the `result.json` file obtained previously on your machine, as we will need its data for the app. Also download the `streamlit-app.py` file.

Create a file named `Dockerfile` and paste the following contents in it:
``` Dockerfile
FROM python:3.9-slim

WORKDIR /app

RUN apt-get update && apt-get install -y \
    build-essential \
    curl \
    software-properties-common \
    git \
    && rm -rf /var/lib/apt/lists/*

COPY streamlit-app.py streamlit-app.py
COPY result.json result.json

RUN pip3 install altair pandas streamlit

EXPOSE 8501

HEALTHCHECK CMD curl --fail http://localhost:8501/_stcore/health

ENTRYPOINT ["streamlit", "run", "streamlit-app.py", "--browser.gatherUsageStats=false"]
```

The Dockerfile describes how the image for the container will be built. In short, it installs the required libraries, copies the files you downloaded, then launches the Streamlit script.

Make sure the three files are in the same directory, then open a shell in it and run the following, which builds the Docker image:
``` shell
podman build -t streamlit .
```

Once it's finished, you can verify the image exists with:
``` shell
podman images
```

Now, run a container:
``` shell
podman run -p 8501:8501 --name streamlit-app streamlit
```

!!! Port already in use

    If you run into an error, it's likely that you didn't quit the remote session you opened while following the previous section, meaning port 8501 is already in use.

Open your browser and visit `localhost:8501` to view the data!

To stop the container, simply press *Ctrl+C*, then run the following to remove the container:
``` shell
podman rm -f streamlit-app
```