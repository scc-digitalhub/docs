# Deploy and expose the model

Deploying a model is as easy as defining a serverless function: we should define the inference operation and the initialization
operation where the model is loaded.

Create a model serving function and provide the model:

```python
%%writefile "src/serve_darts_model.py"
import json
from zipfile import ZipFile

import pandas as pd
from darts import TimeSeries
from darts.datasets import AirPassengersDataset
from darts.metrics import mae, mape, smape
from darts.models import NBEATSModel
from digitalhub_runtime_python import handler

def init_context(context, model_key):
    """
    Initialize serving context by loading the trained model
    """
    model = context.project.get_model(model_key)
    path = model.download()
    local_path_model = "extracted_model/"

    # Extract model from zip file
    with ZipFile(path, "r") as zip_ref:
        zip_ref.extractall(local_path_model)

    # Load the NBEATS model
    input_chunk_length = 24
    output_chunk_length = 12
    name_model_local = local_path_model + "predictor_model.pt"
    mm = NBEATSModel(input_chunk_length, output_chunk_length).load(name_model_local)

    setattr(context, "model", mm)


def serve_predictions(context, event):
    """
    Serve time series predictions via REST API
    """
    if isinstance(event.body, bytes):
        body = json.loads(event.body)
    else:
        body = event.body

    context.logger.info(f"Received event: {body}")
    inference_input = body["inference_input"]

    # Convert input to Darts TimeSeries format
    pdf = pd.DataFrame(inference_input)
    pdf["date"] = pd.to_datetime(pdf["date"], unit="ms")

    ts = TimeSeries.from_dataframe(pdf, time_col="date", value_cols="value")

    # Make predictions
    output_chunk_length = 12
    result = context.model.predict(n=output_chunk_length * 2, series=ts)

    # Convert result to JSON format
    jsonstr = result.pd_dataframe().reset_index().to_json(orient="records")
    return json.loads(jsonstr)
```

Register it:

```python
func = project.new_function(name="serve_darts_model",
                            kind="python",
                            python_version="PYTHON3_10",
                            code_src="src/serve_darts_model.py",
                            handler="serve",
                            init_function="init")
```

Given the dependencies, it is better to have the image ready, using ``build`` action of the function:

```python
run_build_model_serve = func.run("build",
                                 instructions=["pip3 install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cpu","pip3 install darts patsy scikit-learn"],
                                 wait=True)
```

Now we can deploy the function:

```python
serve_run = serve_func.run("serve", init_parameters={"model_key": model.key}, labels=["time-series-service"], wait=True)
```

Install locally the dependencies:

```python
# Install darts locally for testing (if not already installed)
%pip install darts==0.30.0 --quiet
```

Create a test input:

```python
import json
from datetime import datetime
from darts.datasets import AirPassengersDataset

# Load test data
series = AirPassengersDataset().load()
val = series[-24:]  # Last 24 points for prediction
json_value = json.loads(val.to_json())

# Prepare input data in the expected format
data = map(
    lambda x, y: {"value": x[0], "date": datetime.timestamp(datetime.strptime(y, "%Y-%m-%dT%H:%M:%S.%f")) * 1000},
    json_value["data"],
    json_value["index"],
)
inputs = {"inference_input": list(data)}
```

And finally test the endpoint:

```python
serve_run.invoke(json=inputs).json()
```

## Create an API gateway

Right now, the API is only accessible from within the environment. To make it accessible from outside, we'll need to create an API gateway.

Go to the Kubernetes Resource Manager component (available from dashboard) and go to the API Gateways section. To expose a service it is necessary to define

- name of the gateway
- the service to expose
- the endpoint where to publish
- and the authentication method (right now only no authentication or basic authentication are available). in case of basic authentication it is necessary to specify  *Username* and *Password*.

The platform by default support exposing the methods at the subdomains of ``services.<platform-domain>``, where platform-domain is the domain of the platform instance.

![KRM APIGW image](../../images/scenario-etl/apigw-krm.png)

*Save* and, after a few moments, you will be able to call the API at the address you defined! If you set *Authentication* to *Basic*, don't forget that you have to provide the credentials.
