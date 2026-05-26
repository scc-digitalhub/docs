# Protecting Services with Guardrails

!!! note IMPORTANT

    In this scenario we expect the platform is equipped with the **Envoy Gateway** infrastructure configured for guardrails management. 


This tutorial shows how to protect services with Guardrails.

We will use a simple API to be protected by guardrails. The api makes devision operation given the input data.

## Setting up the Service

We will use a simple Python Serverless function created with the Python runtime.

```python
import nuclio_sdk
import os
import json

def handler_serve(context: nuclio_sdk.Context, event: nuclio_sdk.Event):
    if isinstance(event.body, bytes):
        body = json.loads(event.body)
    else:
        body = event.body
    
    divident = body['divident']
    divisor = body['divisor']

    return {"result": divident/divisor}
```

Register the function in platform:

```python
func = project.new_function(name="divisor",
                            kind="python",
                            python_version="PYTHON3_10",
                            code_src="src/divisor.py",
                            handler="handler_serve"
                           )
```

Run and test the unprotected function:

```python
run = func.run(action="serve", wait=True)

# Test the function
import requests

data = {
    'divident': 42,
    'divisor': 6
}
res = requests.post(f"http://{run.refresh().status.service['url']}", json=data)
res.json()
``` 

## Setting up the Guardrail

We will use a simple Guardrail to protect the API implemented with Guardrail runtime. The function controls the input data to avoid devision by zero.

```python 
import nuclio_sdk
import os
import json

def handler_serve(context: nuclio_sdk.Context, event: nuclio_sdk.Event):
    if isinstance(event.body, bytes):
        body = json.loads(event.body)
    else:
        body = event.body
    
    divident = body['divident'] if 'divident' in body else 0 
    divisor = body['divisor'] if 'divisor' in body else 0

    if divident and divisor and divisor > 0:
        return event.body

    return context.Response(body="Invalid input data",
                headers={},
                content_type='text/plain',
                status_code=400)
```

Register the function in platform and run it:

```python
guardrail_func = project.new_function(name="divisor-guardrail",
                                        kind="guardrail",
                                        python_version="PYTHON3_10",
                                        code_src="src/divisor_guardrail_service.py",
                                        handler="handler_serve",
                                        processing_mode="preprocessor"
                                       )
                                    
run = guardrail_func.run(action="serve")
```

## Use the Guardrail to Protect the API

To protect the service instance with guardrails, we rely on the corresponding gateway and use Envoy Gateway extension for the runs. Specifically, when the service enable the extension, we obtain:

- the service exposed also behind the preconfigured service Envoy gateway (see the gatewayInfo in service status);
- if the guardrails are configured, the gateway controls the traffic using the ExtProc extension that interacts with the guardrails to implement pre/post processing logic. 

```python
guardrail_url = guardrail_run.refresh().status.service['url']

run = func.run(action="serve", extensions=[{
    "kind": "envoygw",
    "name": "gw",
    "spec": {
        "guardrails": [guardrail_url]
    }
}])
```

The protected endpoint of service gateway may be obtained as follows:

```python
PROTECTED_ENDPOINT = f"http://{run.status.gatewayInfo['gatewayEndpoint']}/{run.id}"
```

Test the protected service:

```python
import requests

data = {
    'divident': 42,
    'divisor': 0
}
res = requests.post(PROTECTED_ENDPOINT, json=data)
res.text
```