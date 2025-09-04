# Scikit-learn ML scenario introduction

This scenario provides a quick overview of developing and deploying a scikit-learn machine learning application using the functionalities of the platform.

We will prepare data, train a generic model and expose it as a service. Access Jupyter from your Coder instance and create a new notebook. Alternatively, you can find the final notebook file for this scenario in the [tutorial repository](https://github.com/scc-digitalhub/digitalhub-tutorials/tree/main/s3-scikit-learn).

## Set-up

First, import necessary libraries and create a project to host the functions and executions

```python
import digitalhub as dh

project = dh.get_or_create_project("project-ml-ci")
```

Create folder for source code:

```python
from pathlib import Path
Path("src").mkdir(exist_ok=True)
```

## Generate data

Define the following function, which generates the dataset as required by the model:

```python
%%writefile "src/data-prep.py"

import pandas as pd
from sklearn.datasets import load_breast_cancer

from digitalhub_runtime_python import handler

@handler(outputs=["dataset"])
def data_generator():
    """
    A function which generates the breast cancer dataset from scikit-learn
    """
    breast_cancer = load_breast_cancer()
    breast_cancer_dataset = pd.DataFrame(data=breast_cancer.data, columns=breast_cancer.feature_names)
    breast_cancer_labels = pd.DataFrame(data=breast_cancer.target, columns=["target"])
    breast_cancer_dataset = pd.concat([breast_cancer_dataset, breast_cancer_labels], axis=1)
    return breast_cancer_dataset
```

Register it:

```python
data_gen_fn = project.new_function(name="data-prep",
                                   kind="python",
                                   python_version="PYTHON3_10",
                                   code_src="src/data-prep.py",
                                   handler="data_generator")
```

Run it:

```python
gen_data_run = data_gen_fn.run("job",wait=True)
```

You can view the state of the execution with `gen_data_run.status` or its output with `gen_data_run.outputs()`. You can see a few records from the output artifact:

```python
gen_data_run.output("dataset").as_df().head()
```

We will now proceed to training a model.
