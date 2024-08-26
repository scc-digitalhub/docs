# Deploy and expose the model

Deploying a model is as easy as defining a serverless function: we should define the inference operation and the initialization
operation where the model is loaded.

Create a model serving function and provide the model:
``` python
%%writefile "serve_model.py"

from pickle import load
import pandas as pd
import json

def init(context):
    # Qua ti setti il nome del modello che vuoi caricare
    model_name = "cancer_classifier"

    # prendi l'entity model sulla base del nome
    model = context.project.get_model(model_name)
    path = model.download()
    with open(path, "rb") as f:
        svc_model = load(f)
    
    # settare model nel context di nuclio (non su project che è il context nostro)
    setattr(context, "model", svc_model)

def serve(context, event):

    # Sostanzialmente invochiamo la funzione con una chiamata REST
    # Nel body della richiesta mandi l'inference input
    
    if isinstance(event.body, bytes):
        body = json.loads(event.body)
    else:
        body = event.body
    context.logger.info(f"Received event: {body}")
    inference_input = body["inference_input"]
    
    data = json.loads(inference_input)
    pdf = pd.json_normalize(data)

    result = context.model.predict(pdf)

    # Convert the result to a pandas DataFrame, reset the index, and convert to a list
    jsonstr = str(result.tolist())
    return json.loads(jsonstr)
```

Register it and deploy:
``` python
func = project.new_function(name="serve_model",
                            kind="python",
                            python_version="PYTHON3_9",
                            base_image = "python:3.9",
                            source={
                                 "source": "serve_model.py",
                                 "handler": "serve",
                                 "init_function": "init"},
                            requirements=["scikit-learn==1.2.2"])

serve_run = func.run(action="serve")
```

You can now test the endpoint (using e.g., X_test):
``` python
import requests

SERVICE_URL = serve_run.refresh().status.to_dict()["service"]["url"]

with requests.post(f'http://{SERVICE_URL}', json={"inference_input":X_test.to_json(orient='records')}) as r:
    res = r.json()
print(res)
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