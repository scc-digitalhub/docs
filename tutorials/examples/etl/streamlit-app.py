import pandas as pd
import streamlit as st

rdf = pd.read_json("result.json", orient="records")

# Replace colons in column names as they can cause issues with Streamlit
rdf.columns = rdf.columns.str.replace(":", "")

st.write("""My data""")
st.line_chart(rdf, x="codice spira", y="1200-1300")