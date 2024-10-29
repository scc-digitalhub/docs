# Custom ML scenario introduction

This scenario provides a quick overview of developing and deploying generic machine learning applications using the functionalities of the platform. For this purpose, we use ML algorithms for the time series management provided by the [Darts](https://unit8co.github.io/darts/) framework.

We will train a generic model and expose it as a service. Access Jupyter from your Coder instance and create a new notebook. Alternatively, you can find the final notebook file for this scenario in the [tutorial repository](https://github.com/scc-digitalhub/digitalhub-tutorials/tree/main/s6-custom-ml-model).

## Set-up

First, import necessary libraries and create a project to host the functions and executions

```python
import digitalhub as dh

project = dh.get_or_create_project("demo-ml")
```

## Training the model

Let us define the training function. For the sake of simplicity, we use predefined "Air Passengers" dataset of Darts.

``` python
%%writefile "train-model.py"


from digitalhub_runtime_python import handler

import pandas as pd
import numpy as np

from darts import TimeSeries
from darts.datasets import AirPassengersDataset
from darts.models import NBEATSModel
from darts.metrics import mape, smape, mae

from zipfile import ZipFile

@handler()
def train_model(project):
    series = AirPassengersDataset().load()
    train, val = series[:-36], series[-36:]

    model = NBEATSModel(
        input_chunk_length=24,
        output_chunk_length=12,
        n_epochs=200,
        random_state=0
    )
    model.fit(train)
    pred = model.predict(n=36)

    model.save("predictor_model.pt")
    with ZipFile("predictor_model.pt.zip", "w") as z:
        z.write("predictor_model.pt")
        z.write("predictor_model.pt.ckpt")
    metrics = {
        "mape": mape(series, pred),
        "smape": smape(series, pred),
        "mae": mae(series, pred)
    }

    project.log_model(
        name="darts_model",
        kind="model",
        source="predictor_model.pt.zip",
        algorithm="darts.models.NBEATSModel",
        framework="darts",
        metrics=metrics
    )
```

In this code we create a NBEATS DL model, store it locally zipping the content, extract some metrics, and log the model to the platform
with a generic ``model`` kind.

Let us register it:

``` python
train_fn = project.new_function(name="train-darts",
                                kind="python",
                                python_version="PYTHON3_10",
                                code_src="train-model.py",
                                handler="train_model",
                                requirements=["darts==0.30.0"])
```

and run it:

``` python
train_run = train_fn.run(action="job")
```

As a result of train execution, a new model is registered in the Core and may be used by different inference operations.

Lastly, we'll deploy and test the model.
