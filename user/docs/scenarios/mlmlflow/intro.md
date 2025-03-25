# MLFLow ML scenario introduction

This scenario provides a quick overview of developing and deploying a machine learning application based on model tracked with MLFlow framework using the functionalities of the platform.

We will prepare data, train a generic model and expose it as a service. Access Jupyter from your Coder instance and create a new notebook. Alternatively, you can find the final notebook file for this scenario in the [tutorial repository](https://github.com/scc-digitalhub/digitalhub-tutorials/tree/main/s4-mlflow).

## Set-up

Create folder for source code:

```python
from pathlib import Path
Path("src").mkdir(exist_ok=True)
```

Then, import necessary libraries and create a project to host the functions and executions

```python
import digitalhub as dh

project = dh.get_or_create_project("project-mlflow-model-ci")
```

## Generate data

For the sake of simplicity, we use the predefined IRIS dataset.

## Training the model

Let us define the training function.

```python
%%writefile "src/train-model.py"

from digitalhub_runtime_python import handler
from digitalhub import from_mlflow_run, get_mlflow_model_metrics
import mlflow

from sklearn import datasets, svm
from sklearn.model_selection import GridSearchCV

@handler(outputs=["model"])
def train(project):
    mlflow.sklearn.autolog(log_datasets=True)

    iris = datasets.load_iris()
    parameters = {"kernel": ("linear", "rbf"), "C": [1, 10]}
    svc = svm.SVC()
    clf = GridSearchCV(svc, parameters)

    clf.fit(iris.data, iris.target)
    run_id = mlflow.last_active_run().info.run_id

    # utility to map mlflow run artifacts to model metadata
    model_params = from_mlflow_run(run_id)
    metrics = get_mlflow_model_metrics(run_id)

    model = project.log_model(
        name="model-mlflow",
        kind="mlflow",
        **model_params
    )
    for metric in metrics:
        model.log_metric(metric, metrics[metric], single_value=True)
    return model
```

The function creates an SVC model with the scikit-learn framework. Note that here
we use the autologging functionality of MLFlow and then construct the necessary model metadata out of the tracked MLFlow model.
Specifically, MLFlow creates a series of artifacts that describe the model and the corresponding model files, as well as additional files representing the model properties and metrics.

We then log the model of ``mlflow`` kind using the extract metadata as kwargs.

Let us register it:

```python
train_fn = project.new_function(name="train",
                                kind="python",
                                python_version="PYTHON3_10",
                                code_src="src/train-model.py",
                                handler="train",
                                requirements=["scikit-learn", "mlflow"])
```

and run it locally:

```python
train_model_run = train_fn.run(action="job", wait=True)
```

As a result, a new model is registered in the Core and may be used by different inference operations:

```python
model = train_model_run.output("model-mlflow")
model.spec.path
```

Lastly, we'll deploy and test the model.
