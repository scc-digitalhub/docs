# Expose datasets as API

We define an exposing function to make the data reachable via REST API:

```python
%%writefile 'src/api.py'

def init_context(context, dataitem):
    di = context.project.get_dataitem(dataitem)
    df = di.as_df()
    setattr(context, "df", df)

def serve(context, event):
    df = context.df

    if df is None:
        return ""

    # mock REST api
    fields = event.fields

    # pagination
    page = 0
    pageSize = 50

    if "page" in fields:
        page = int(fields["page"])

    if "size" in fields:
        pageSize = int(fields["size"])

    if page < 0:
        page = 0

    if pageSize < 1:
        pageSize = 1

    if pageSize > 100:
        pageSize = 100

    start = page * pageSize
    end = start + pageSize
    total = len(df)

    if end > total:
        end = total

    ds = df.iloc[start:end]
    json = ds.to_json(orient="records")

    return {"data": json, "page": page, "size": pageSize, "total": total}
```

Register the function:

```python
api_func = project.new_function(name="api",
                                kind="python",
                                python_version="PYTHON3_10",
                                code_src="src/api.py",
                                handler="serve",
                                init_function="init_context")
```

Please note that other than defining the handler method, it is possible to define the ``init_function`` to define the preparatory steps.

Deploy the function (perform ``serve`` action):

```python
run_serve_model = api_func.run("serve", wait=True)
```

Wait till the deployment is complete and the necessary pods and services are up and running.

```python
run_serve_model.refresh()
```

When done, the status of the run contains the ``service`` element with the internal service URL to be used.

```python
svc_url = f"http://{run_serve_model.status.service['url']}/?page=5&size=10"
```

Invoke the API and print its results:

```python
res = run_serve_model.invoke(url=svc_url).json()
print(res)
```

You can also use *pandas* to load the result in a data frame:

```python
rdf = pd.read_json(res['data'], orient='records')
rdf.head()
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
