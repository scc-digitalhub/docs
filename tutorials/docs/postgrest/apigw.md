# Expose service externally

Finally, we make the PostgREST service available externally. 

Go to the Kubernetes Resource Manager component (available from dashboard) and go to the HTTP Route section. To expose a service it is necessary to define 
a set of properties. See the [HTTP Route](../../admin/charts/krm/resources/#exposing-services-externally) instructions for details.


![Create APIGW](./images/krm_httproute.jpg)

Save and the API gateway will be created. You can try a simple query like the following, even in your browser, to view its results (remember to change domain according to your case):
```
https://pgrest.services.example.com/readings?limit=3
```
