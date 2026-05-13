# Invoke, Use, and Expose Services

When executing _runs_, tasks of type _service_ will result in a deployment with an HTTP service published inside the platform.

Those runs will receive a unique, addressable identifier along with an IP address and an internal service URL. The detailed information are stored in the run _status_ field, under the `service` keyword. Together with the base service url, all well known urls will be registered and exposed to users.

```yaml
service:
  name: s-containerserve-9271ab33c0364d549c89f8b2834ae141
  type: ClusterIP
  clusterIP: 172.16.143.129
  ports:
    - name: port5678
      port: 5678
      protocol: TCP
      targetPort: 5678
  url: s-containerserve-9271ab33c0364d549c89f8b2834ae141:5678
```

By calling the URL, users are thus able to invoke their function interactively.

The service view will present at any given time the status of active _services_, i.e. runs with a service exposed. Users can get a quick glimpse of the health of their deployments, with quick actions available.

![Services list](../images/console/services-list.png)

As we can see from the screenshot, the current _status_ is highlighted, and any contextual message is directly reported.

**Important!**

Do note that service URLs are not exposed outside the perimeter of the platform. Only clients from inside the platform, such as workspaces, other functions and the core console are able to access. In order to expose the service _externally_ an api gateway is required.

## Service invocation

Services which are in an healthy state can be invoked from inside the platform, either manually (by custom code or standard HTTP clients) or via the python SDK `invoke` method on runs.

```python

run = function.run(...)
# invoke the service only when ready!

result = run.invoke(...)

```

See the [SDK Reference documentation](https://scc-digitalhub.github.io/sdk-docs) for details.

## HTTP client

The user console implements a basic HTTP client, able to perform operations on textual content (e.g. text/plain, application/json etc).

By selecting a valid service run and clicking the _CLIENT_ button, the console will open a simplified dialog as depicted in following figure.

![HTTP Client](../images/console/http-client.png)

From the client, users will be able to perform basic operations and visualize the results.

#### Features

- Supports GET/POST/PUT/DELETE operations
- Can invoke internal urls leveraging core as gateway
- Supports custom HTTP headers
- Full request/response history
- Basic _raw_ text support
- Interactive preview for JSON and YAML

#### Notes

The service is not exposed to the user's browser: access is mediated by the console through the core backend. As such, only a limited set of content is allowed: **text-based** requests and responses with a reasonable size limit.

### Specialized clients

In addition to the standard HTTP client, the console provides specialized clients for specific model-serving scenarios. The appropriate client is automatically selected based on the service type:

- **[Chat Client](../runtimes/chat-client.md)** — An interactive chat interface for LLM models served with OpenAI-compatible APIs. Used with HuggingFace Serve and KubeAI Text runtimes.
- **[InferenceV2 Client](../runtimes/inference-v2-client.md)** — A dedicated client for models served using the Open Inference Protocol (V2), with built-in health monitoring and pre-configured endpoints. Used with MLflow Serve and Scikit-learn Serve runtimes.

## Exposing services externally

Various APIs and services (e.g., PostgREST or Dremio data services, serverless functions, ML services) may be exposed externally, outside of the platform, on a public domain of the platform. Using KRM, the operation amounts to defining a new gateway (HTTPRoute resource) that will be transformed into the corresponding ingress routing specification.

![KRM HTTP Route create image](../../images/krm/krm_httproute.jpg)

To create a new gateway, provide the following:

- **Name** of the gateway. This is merely an identifier for Kubernetes.
- Kubernetes **backend service** to be exposed (select it from the dropdown list and **port** will automatically be provided).
- **Hostname** defines the full domain name under which the service will be exposed. By default, it refers to the `services` subdomain. If your instance of the platform is found in the `example.com` domain, this field's value could be `myservice.services.example.com`.
- Relative **path prefix** to expose the service on.
- **Rewrite path prefix** to rewrite the path of the request.
-
- **Authentication** information. Currently, services may be
  - unprotected (`None`) or
  - protected with `Basic` authentication, specifying the secret with the httpwd credentials.
  - protected with `ApiKey` authentication, specifying the secret with the token name / token value pairs and the header name.
  - protected with `JWT` configuration, specifying the information about JWKS, issuer, optional audiences to check and claim mapping.
