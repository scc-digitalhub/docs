# Deploy and expose the model

Deploying a MLFLow model is easy: ``mlflowserve`` runtime supports this functionality out of the box. It is sufficient to specify the path to the model artifact and optionally the name of the model to expose.

It is important to note that the path should point to the folder, where the MLFlow ``MLModel`` artifact is placed. If the model 
is created from MLFlow run artifact path, besides the ``model`` folder it may contain additional artifacts.

Register it and deploy:
``` python
func = project.new_function(name="serve_mlflowmodel",
                            kind="mlflowserve",
                            model_name="testmodel",
                            path=model.spec.path + 'model')

serve_run = func.run(action="serve")
```

You can now test the endpoint (using e.g., the subset of data):
``` python
import requests
from sklearn import datasets

SERVICE_URL = serve_run.refresh().status.to_dict()["service"]["url"]
MODEL_NAME = "testmodel"

iris = datasets.load_iris()
test_input = iris.data[0:2].tolist()

with requests.post(f'http://{SERVICE_URL}/v2/models/{MODEL_NAME}/infer', json={
    "inputs": [
        {
        "name": "input-0",
        "shape": [2, 4],
        "datatype": "FP64",
        "data": test_input
        }
    ]
}) as r:
    res = r.json()
print(res)
```

Please note that the MLFLow model serving exposes also the Open API specification under ``/v2/docs`` path.

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