# Collect the data

Create a new folder to store the function's code in:

```python
from pathlib import Path
Path("src").mkdir(exist_ok=True)
```

Define a function for downloading data as-is and persisting it in the data-lake:

```python
%%writefile "src/download-data.py"

from digitalhub_runtime_python import handler

@handler(outputs=["dataset"])
def downloader(url):
    return url.as_df(file_format='csv',sep=";")
```

Register the function in Core:

```python
func = project.new_function(name="download-data",
                            kind="python",
                            python_version="PYTHON3_10",
                            code_src="src/download-data.py",
                            handler="downloader")
```

This code creates a new function definition that uses Python runtime (versione 3.10) pointing to the created file and the handler method that should be called.

For the function to be executed, we need to pass it a reference to the data item. Let us create and register the corresponding data item:

```python
URL = "https://opendata.comune.bologna.it/api/explore/v2.1/catalog/datasets/rilevazione-flusso-veicoli-tramite-spire-anno-2023/exports/csv?limit=50000&lang=it&timezone=Europe%2FRome&use_labels=true&delimiter=%3B"
di = project.new_dataitem(name="url_data_item",
                          kind="table",
                          path=URL)
```

It is also possible to see the data item directly in the Core UI.

Then, execute the function (locally) as a single job. Note that it may take a few minutes.

```python
run = func.run("job",
               inputs={'url': di.key},
               wait=True)
```

Note that the ``inputs`` map should contain the references to the project entities (e.g., artifacts, dataitems, etc), while in order to pass literal values to the function execution it is necessary to use ``parameters`` map.

The result will be saved as an artifact in the data store, versioned and addressable with a unique key. The name of the artifact will be defined according to the mapping specified in ``@handler`` annotation.
To get the value of the artifact we can refer to it by the output name:

```python
dataset_di = project.get_dataitem('dataset')
```

Load the data item and then into a data frame:

```python
dataset_df = dataset_di.as_df()
```

Run `dataset_df.head()` and, if it prints a few records, you can confirm that the data was properly stored. It's time to process this data.
