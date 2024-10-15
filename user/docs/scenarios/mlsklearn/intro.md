# Scikit-learn ML scenario introduction

This scenario provides a quick overview of developing and deploying a scikit-learn machine learning application using the functionalities of the platform.

We will prepare data, train a generic model and expose it as a service. Access Jupyter from your Coder instance and create a new notebook. Alternatively, you can find the final notebook file for this scenario in the `user/examples/mlsklearn` path within the repository of this documentation, together with any additional related files.

## Set-up

First, import necessary libraries and create a project to host the functions and executions

```python
import digitalhub as dh

project = dh.get_or_create_project("demo-ml")
```

## Generate data

Define the following function, which generates the dataset as required by the model:

``` python
%%writefile data-prep.py

import pandas as pd
from sklearn.datasets import load_breast_cancer

from digitalhub_runtime_python import handler

@handler(outputs=["dataset"])
def breast_cancer_generator():
    """
    A function which generates the breast cancer dataset
    """
    breast_cancer = load_breast_cancer()
    breast_cancer_dataset = pd.DataFrame(
        data=breast_cancer.data, columns=breast_cancer.feature_names
    )
    breast_cancer_labels = pd.DataFrame(data=breast_cancer.target, columns=["target"])
    breast_cancer_dataset = pd.concat(
        [breast_cancer_dataset, breast_cancer_labels], axis=1
    )

    return breast_cancer_dataset
```

Register it:

``` python
data_gen_fn = project.new_function(name="data-prep",
                                   kind="python",
                                   python_version="PYTHON3_10",
                                   code_src="data-prep.py",
                                   handler="breast_cancer_generator")
```

Run it locally:

``` python
gen_data_run = data_gen_fn.run(action="job", outputs={"dataset": "dataset"}, local_execution=True)
```

You can view the state of the execution with `gen_data_run.status` or its output with `gen_data_run.outputs()`. You can see a few records from the output artifact:

``` python
gen_data_run.output("dataset").as_df().head()
```

We will now proceed to training a model.
