# Deploy and expose the model

Deploying a MLFLow model is easy: ``mlflowserve`` runtime supports this functionality out of the box. It is sufficient to specify the path to the model artifact and optionally the name of the model to expose.

It is important to note that the path should point to the folder, where the MLFlow ``MLModel`` artifact is placed. If the model
is created from MLFlow run artifact path, besides the ``model`` folder it may contain additional artifacts.

Register it and deploy:

```python
serve_func = project.new_function(
    name="serve-mlflow-model",
    kind="mlflowserve",
    model_name=model.name,
    path=model.spec.path + "model/",
)

serve_run = func.run("serve", wait=True)
```

You can now create a dataset for testing the endpoint:

```python
from sklearn import datasets

iris = datasets.load_iris()
data = iris.data[0:2].tolist()
json={
    "inputs": [
        {
        "name": "input-0",
        "shape": [-1, 4],
        "datatype": "FP64",
        "data": data
        }
    ]
}
```

Finally, you can test the endpoint. When the model is ready to be used, invoke the endpoint:

```python
serve_run.invoke(model_name=model.name, json=json).json()
```

If it does not work, wait for sometimes, because it takes a while to load the model.

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
