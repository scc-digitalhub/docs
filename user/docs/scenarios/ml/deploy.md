# Deploy and expose the model

Deploying a model is as easy as defining a serverless function: we should define the inference operation and the initialization
operation where the model is loaded.

Create a model serving function and provide the model:

``` python
%%writefile "serve_darts_model.py"

from darts.models import NBEATSModel
from zipfile import ZipFile
from darts import TimeSeries
import json
import pandas as pd

def init(context):
    model_name = "darts_model"

    model = context.project.get_model(model_name)
    path = model.download()
    local_path_model = "extracted_model/"

    with ZipFile(path, 'r') as zip_ref:
        zip_ref.extractall(local_path_model)

    input_chunk_length = 24
    output_chunk_length = 12
    name_model_local = local_path_model +"predictor_model.pt"
    mm = NBEATSModel(
            input_chunk_length,
            output_chunk_length
    ).load(name_model_local)

    setattr(context, "model", mm)

def serve(context, event):

    if isinstance(event.body, bytes):
        body = json.loads(event.body)
    else:
        body = event.body
    context.logger.info(f"Received event: {body}")
    inference_input = body["inference_input"]

    pdf = pd.DataFrame(inference_input)
    pdf['date'] = pd.to_datetime(pdf['date'], unit='ms')

    ts = TimeSeries.from_dataframe(
        pdf,
        time_col="date",
        value_cols="value"
    )

    output_chunk_length = 12
    result = context.model.predict(n=output_chunk_length*2, series=ts)
    # Convert the result to a pandas DataFrame, reset the index, and convert to a list
    jsonstr = result.pd_dataframe().reset_index().to_json(orient='records')
    return json.loads(jsonstr)
```

Register it:

``` python
func = project.new_function(name="serve_darts_model",
                            kind="python",
                            python_version="PYTHON3_10",
                            code_src="serve_darts_model.py",
                            handler="serve",
                            init_function="init",
                            requirements=["darts==0.30.0"])
```

Given the dependencies, it is better to have the image ready, using ``build`` action of the function:

``` python
run_build_model_serve = func.run(action="build", instructions=["pip3 install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cpu","pip3 install darts==0.30.0"])
```

Now we can deploy the function:

``` python
run_serve = func.run(action="serve")
```

Install locally the dependencies:

``` python
%pip install darts==0.30.0
```

Create a test input:

``` python
import json
from datetime import datetime
from darts.datasets import AirPassengersDataset

series = AirPassengersDataset().load()
val = series[-24:]
json_value = json.loads(val.to_json())

data = map(lambda x, y: {"value": x[0], "date": datetime.timestamp(datetime.strptime(y, "%Y-%m-%dT%H:%M:%S.%f"))*1000}, json_value["data"], json_value["index"])
inference_input = list(data)
json = {"inference_input": inference_input}
```

Refresh the run until `service` attribute is available in `status`:

``` python
run_serve.refresh().status
```

And finally test the endpoint:

``` python
run_serve.invoke(method="POST", json=json).json()
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
