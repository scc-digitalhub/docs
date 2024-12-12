# Insert data into the database

Access Jupyter from your Coder instance and create a new notebook. If a Jupyter workspace isn't already available, create one from its template.

Open a new notebook using the **`Python 3 (ipykernel)`** kernel.

We will now insert some data into the database we created earlier. Copy the snippets of code from here and paste them in your notebook, then execute them with *Shift+Enter*. After running, Jupyter will create a new code cell.

The notebook file is available in the `documentation/examples/postgrest` path within the repository of this documentation.

Import required libraries:

```python
import os
from sqlalchemy import create_engine
import pandas as pd
import requests
```

Connect to the database. You will need the value of **POSTGRES_URL** you got from the owner's secret in the first stage of the scenario.

```python
engine = create_engine('postgresql://owner-UrN9ct:88aX8tLFJ95qYU7@database-postgres-cluster/mydb')
```

Download a CSV file and parse it (may take a few minutes):

```python
URL = "https://opendata.comune.bologna.it/api/explore/v2.1/catalog/datasets/rilevazione-flusso-veicoli-tramite-spire-anno-2023/exports/csv?lang=it&timezone=Europe%2FRome&use_labels=true&delimiter=%3B"
filename = "rilevazione-flusso-veicoli-tramite-spire-anno-2023.csv"

with requests.get(URL) as r:
    with open(filename, "wb") as f:
        f.write(r.content)

df = pd.read_csv(filename, sep=";")
```

The following will create a table and insert the dataframe into it. If it fails, resources allocated to the Jupyter workspace may be insufficient. The table will be created automatically, or replaced if it already exists.
```python
df.to_sql("readings", engine, if_exists="replace")
```

Run a test select query to check data has been successfully inserted:
```python
select = "SELECT * FROM readings LIMIT 3"
select_df = pd.read_sql(select,con=engine)
select_df.head()
```

If everything went right, a few rows are returned. We will now create a PostgREST service to expose this data via a REST API.
