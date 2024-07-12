# Collect the data

Create a new folder to store the function's code in:
``` python
new_folder = 'src'
if not os.path.exists(new_folder):
    os.makedirs(new_folder)
```

Define a function for downloading data as-is and persisting it in the data-lake:
``` python
%%writefile "src/download-data.py"

from digitalhub_runtime_python import handler
import pandas as pd
import requests

@handler(outputs=["dataset"])
def downloader(project, url):
    # read and rewrite to normalize and export as data
    df = url.as_df(file_format='csv',sep=";")
    return df
```

Register the function in Core:
``` python
func = project.new_function(
                         name="download-data",
                         kind="python",
                         python_version="PYTHON3_9",
                         source={"source": "src/download-data.py", "handler": "downloader"})
```

This code creates a new function definition that uses Python runtime (versione 3.9) pointing to the create file and the handler method that should be called.

For the function to be executed, we need to pass it a reference to the data item. Let us create and register the corresponding data item:
``` python
URL = "https://opendata.comune.bologna.it/api/explore/v2.1/catalog/datasets/rilevazione-flusso-veicoli-tramite-spire-anno-2023/exports/csv?lang=it&timezone=Europe%2FRome&use_labels=true&delimiter=%3B"
di= project.new_dataitem(name="url_data_item",kind="table",path=URL)
```

It is also possible to see the data item directly in the Core UI. 


Then, execute the function (locally) as a single job. Note that it may take a few minutes.
``` python
run = func.run(action="job", inputs={'url':di.key}, outputs={"dataset": "dataset"}, local_execution=True)
```

Note that the ``inputs`` map should contain the references to the project entities (e.g., artifacts, dataitems, etc), while in order to pass literal values to the function execution it is necessary to use ``parameters`` map.

The result will be saved as an artifact in the data store, versioned and addressable with a unique key. The name of the artifact will be defined according to the mapping specified in ``outputs`` map: it maps the handler outputs (see the ``@handler`` annotation and its output definition) to the expected name.

To get the value of the artifact we can refer to it by the output name:
``` python
dataset_di = project.get_dataitem(entity_name='dataset')
```

Load the data item and then into a data frame:
``` python
dataset_df = dataset_di.as_df()
```

Run `dataset_df.head()` and, if it prints a few records, you can confirm that the data was properly stored. It's time to process this data.