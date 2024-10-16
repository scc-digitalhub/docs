# MLFLow ML scenario introduction

This scenario provides a quick overview of developing and deploying a machine learning application based on model tracked with MLFlow framework using the functionalities of the platform.

The resulting edited notebook, as well as a file for the function we will create, are available in the `documentation/examples/mlmlflow` path within the repository of this documentation.

We will prepare data, train a generic model and expose it as a service. Access Jupyter from your Coder instance and create a new notebook.

## Set-up

Install the necessary libraries:

``` python
%pip install mlflow scikit-learn==1.5.0
```

Then, import necessary libraries and create a project to host the functions and executions

```python
import digitalhub as dh

project = dh.get_or_create_project("demo-ml")
```

## Generate data

For the sake of simplicity, we use the predefined IRIS dataset.

## Training the model

Let us define the training function.

``` python
%%writefile train-model.py

from digitalhub_runtime_python import handler

from digitalhub_ml import from_mlflow_run
import mlflow

from sklearn import datasets, svm
from sklearn.model_selection import GridSearchCV

@handler()
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

    project.log_model(
        name="model-mlflow",
        kind="mlflow",
        **model_params
)
```

The function creates an SVC model with the scikit-learn framework. Note that here
we use the autologging functionality of MLFlow and then construct the necessary model metadata out of the tracked MLFlow model.
Specifically, MLFlow creates a series of artifacts that describe the model and the corresponding model files, as well as additional files representing the model properties and metrics.

We then log the model of ``mlflow`` kind using the extract metadata as kwargs.

Let us register it:

``` python
train_fn = project.new_function(name="train",
                                kind="python",
                                python_version="PYTHON3_9",
                                code_src="train-model.py",
                                handler="train",
                                requirements=["scikit-learn==1.5.0", "mlflow==2.15.1"])
```

and run it locally:

``` python
train_run = train_fn.run(action="job", local_execution=True)
```

As a result, a new model is registered in the Core and may be used by different inference operations:

```python
model = project.get_model("model-mlflow")
model.spec.path
```

Lastly, we'll deploy and test the model.
