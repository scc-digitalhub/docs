# Training the model

Let us define the training function.

```python
%%writefile "src/train-model.py"
import os
import pandas as pd
import numpy as np
from pickle import dump
import sklearn.metrics
from digitalhub_runtime_python import handler
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC

@handler(outputs=["model"])
def train_model(project, di):
    """
    Train an SVM classifier on the breast cancer dataset and log metrics
    """
    df_cancer = di.as_df()
    X = df_cancer.drop(["target"], axis=1)
    y = df_cancer["target"]
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20, random_state=5)
    svc_model = SVC()
    svc_model.fit(X_train, y_train)
    y_predict = svc_model.predict(X_test)

    if not os.path.exists("model"):
        os.makedirs("model")

    with open("model/breast_cancer_classifier.pkl", "wb") as f:
        dump(svc_model, f, protocol=5)

    metrics = {
        "f1_score": sklearn.metrics.f1_score(y_test, y_predict),
        "accuracy": sklearn.metrics.accuracy_score(y_test, y_predict),
        "precision": sklearn.metrics.precision_score(y_test, y_predict),
        "recall": sklearn.metrics.recall_score(y_test, y_predict),
    }
    model = project.log_model(name="breast_cancer_classifier", kind="sklearn", source="./model/")
    model.log_metrics(metrics)
    return model
```

The function takes the analysis dataset as input, creates an SVC model with the scikit-learn framework and logs the model with its metrics.

Let us register it:

```python
train_fn = project.new_function(
    name="train-classifier",
    kind="python",
    python_version="PYTHON3_10",
    code_src="src/train-model.py",
    handler="train_model",
    requirements=["numpy<2"],
)
```

and run it:

```python
dataset = gen_data_run.output("dataset")
train_run = train_fn.run(action="job", inputs={"di": dataset.key}, wait=True)
```

As a result, a new model is registered in the Core and may be used by different inference operations:

```python
model = train_run.output("model")
```

Lastly, we'll deploy and test the model.
