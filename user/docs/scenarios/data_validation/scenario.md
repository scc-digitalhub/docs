# Data validation 

This scenario implements a simple data validation function, which evaluates the correctness of a CSV table by leveraging an open source library, [Frictionless](https://github.com/frictionlessdata/frictionless-py).

The function will read a CSV file and then produce a *report*, along with a LABEL marking the dataset as `VALID` or `INVALID`.


## Set-up

First, we initialize our environment and create a project.

Import required libraries:

```python
import digitalhub as dh
import pandas as pd
import requests
import os
```

Create a project:

```python
PROJECT = "validation"
project = dh.get_or_create_project(PROJECT)
```


## Function definition

Define the validation function by writing the source code and registering it via sdk.

```python
%%writefile "validate.py"


import digitalhub as dh
from digitalhub_runtime_python import handler
from frictionless import Checklist, validate
import os

@handler(outputs=["report"])
def main(project, di):
    # download as local file
    path = di.download(destination=di.name, overwrite=True)
    # validate
    report = validate(path)
    # update artifact with label    
    label = "VALID" if report.valid else "INVALID"
    di.metadata.labels = di.metadata.labels.append(label) if di.metadata.labels else [label]
    di.save(update=True)    
    #cleanup
    os.remove(path) 

    with open("report.json", "w") as f:
      f.write(report.to_json())

    project.log_artifact(kind="artifact", name=f"{di.name}_validation-report.json", source="report.json")
        
    # persist report
    return report.to_json()
```

And then

```python
func = project.new_function(name="validate-csv",
                            kind="python",
                            python_version="PYTHON3_10",
                            requirements=["frictionless"],
                            code_src="validate.py",
                            handler="main")
```


The function can be tested by passing a DataItem as input. For example, we can register an URL and use it as source for a quick run.


```python
URL = "https://raw.githubusercontent.com/scc-digitalhub/digitalhub-tutorials/refs/heads/main/s10-data-validation/data-invalid.csv"
di = project.new_dataitem(name="data-invalid.csv",
                          kind="table",
                          path=URL)
```

And then execute the function:

```python
run = func.run("job",
               inputs={'di': di.key},
               wait=True)
```

The result will be the execution of the function as a batch job, producing a report in JSON format stored as artifact in the repository. Additionally, the function will append an `INVALID` label to the data item.

## Trigger

We set up a trigger to automatically run the validate function when a CSV file is uploaded as a data item.

Create the trigger:

```python
func.trigger(action="job",
             kind="lifecycle",
             name="csv-trigger",
             states=["READY"],
             key=f"store://{PROJECT}/dataitem/table/*",
             template={"inputs": {"di": "{{input.key}}"}})
```

If you go to the console and create a data item by selecting `table` as *kind* and uploading any CSV file, once the data item is *READY*, the function will be run and the report artifact will be generated.

We can also create a data item here:

```python
URL = "https://raw.githubusercontent.com/scc-digitalhub/digitalhub-tutorials/refs/heads/main/s10-data-validation/data-valid.csv"
di = project.new_dataitem(name="data-valid.csv",
                          kind="table",
                          path=URL)
project.log_dataitem(name="data-valid.csv", kind="table", source=di.as_file())
```
