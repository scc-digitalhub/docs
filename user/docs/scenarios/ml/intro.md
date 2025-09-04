# Custom ML scenario introduction

This scenario provides a quick overview of developing and deploying generic machine learning applications using the functionalities of the platform. For this purpose, we use ML algorithms for the time series management provided by the [Darts](https://unit8co.github.io/darts/) framework.

We will train a generic model and expose it as a service. Access Jupyter from your Coder instance and create a new notebook. Alternatively, you can find the final notebook file for this scenario in the [tutorial repository](https://github.com/scc-digitalhub/digitalhub-tutorials/tree/main/s6-custom-ml-model).

## Set-up

First, import necessary libraries and create a project to host the functions and executions

```python
import digitalhub as dh

project = dh.get_or_create_project("project-cml-darts-ci")
```

## Create dir for the code

Create a directory for the code:

```python
from pathlib import Path
Path("src").mkdir(exist_ok=True)
```

## Training the model

Let us define the training function. For the sake of simplicity, we use predefined "Air Passengers" dataset of Darts.

```python
%%writefile "src/train-model.py"
import json
from zipfile import ZipFile

import pandas as pd
from darts import TimeSeries
from darts.datasets import AirPassengersDataset
from darts.metrics import mae, mape, smape
from darts.models import NBEATSModel
from digitalhub_runtime_python import handler


@handler(outputs=["model"])
def train_model(project):
    """
    Train a NBEATS model on the Air Passengers dataset
    """
    # Load Air Passengers dataset
    series = AirPassengersDataset().load()
    train, test = series[:-36], series[-36:]

    # Configure and train NBEATS model
    model = NBEATSModel(input_chunk_length=24, output_chunk_length=12, n_epochs=200, random_state=0)
    model.fit(train)

    # Make predictions for evaluation
    pred = model.predict(n=36)

    # Save model artifacts
    model.save("predictor_model.pt")
    with ZipFile("predictor_model.pt.zip", "w") as z:
        z.write("predictor_model.pt")
        z.write("predictor_model.pt.ckpt")

    # Calculate metrics
    metrics = {"mape": mape(test, pred), "smape": smape(test, pred), "mae": mae(test, pred)}

    # Register model in DigitalHub
    model_artifact = project.log_model(
        name="air-passengers-forecaster",
        kind="model",
        source="predictor_model.pt.zip",
        algorithm="darts.models.NBEATSModel",
        framework="darts",
    )
    model_artifact.log_metrics(metrics)
    return model_artifact
```

In this code we create a NBEATS DL model, store it locally zipping the content, extract some metrics, and log the model to the platform
with a generic ``model`` kind.

Let us register it:

```python
train_fn = project.new_function(
    name="train-time-series-model",
    kind="python",
    python_version="PYTHON3_10",
    code_src="src/functions.py",
    handler="train_model",
)
```

and run it with build instruction:

```python
train_build = train_fn.run("build",
                           instructions=["pip3 install torch'<2.6.0' darts==0.30.0 patsy"],
                           wait=True)
```

Once the build is completed, launch the training.

```python
train_run = train_fn.run("job", wait=True)
```

As a result of train execution, a new model is registered in the Core and may be used by different inference operations.

Lastly, we'll deploy and test the model.
