# Visualize data with Streamlit

We can take this one step further and visualize our data in a graph. We will make use of [Streamlit](https://streamlit.io/), a library to create web apps and visualize data by writing simple scripts.

From the Jupyter notebook you've been using, write the result of the API call to a file:

``` python
with open("result.json", "w") as file:
    file.write(res['data'])
```

Create the script that Streamlit will run:

``` python
%%writefile 'streamlit-data.py'

import pandas as pd
import streamlit as st

rdf = pd.read_json('result.json', orient='records')

st.write("""My data""")
st.line_chart(rdf, x='codice spira', y='12:00-13:00')
```

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
streamlit run streamlit-data.py --browser.gatherUsageStats false
```

Access `localhost:8501` on your browser to view the data!

![Streamlit image](../../../images/streamlit.png)

The graph we displayed is very simple, but you are welcome to experiment with more Streamlit features.