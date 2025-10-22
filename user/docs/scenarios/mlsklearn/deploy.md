# Deploy and expose the model

Deploying a scikit-learn model is easy: ``sklearnserve`` runtime supports this functionality out of the box. It is sufficient to specify the path to the model artifact and optionally the name of the model to expose.

Register it and deploy:

```python
serve_func = project.new_function(
    name="serve-classifier",
    kind="sklearnserve",
    path=model.key,
)
serve_run = serve_func.run("serve", wait=True)
```

You can now create a dataset for testing the endpoint:

```python
import numpy as np

# Generate sample data for prediction
data = np.random.rand(2, 30).tolist()
json_payload = {"inputs": [{"name": "input-0", "shape": [2, 30], "datatype": "FP32", "data": data}]}
```

Finally, you can test the endpoint. To do so, you need to refresh the serve run. This is needed because the backend monitors the deployment every minute and the model status, where the endpoint is exposed, is updated after a minute.
When the model is ready, invoke the endpoint:

```python
result = serve_run.refresh().invoke(json=json_payload).json()
print("Prediction result:")
print(result)
```

Please note that the scikit-learn model serving exposes also the Open API specification under ``/docs`` path.

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
