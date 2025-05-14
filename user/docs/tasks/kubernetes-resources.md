# Using Kubernetes Resources for Runs

When it come to execution of AI tasks, either batch jobs or model serving, it is important to be able to
allocate an appropriate set of resources, such as memory, GPU, node types, etc.

For this purpose the platform relies on Kubernetes functionalities and resource definitions. More specifically,
the run configuration may have a specific requirements for

- node selection
- volumes (Persistent Volume Claims and Config Maps)
- HW resources in terms of CPU and memory requests and limits, numbers of GPUs
- Kubernetes affinity definition and/or toleration properties
- Additional secrets and environment variables to be associated with the execution




## How to define resource requirements
In the platform, kubernetes resource requirements may be defined in two ways: 
* by users at run time, by requesting resources to be allocated for a given run,
* by administrators at deployment time, by configuring defaults and limits along with pre-configured templates and profiles


### Request resources at runtime
The platform lets users require additional k8s resource to be allocated to a given function's run, either via Core UI or via SDK. Please note that it is possible to describe only some properties, leaving the rest blank without constraints. All the defaults are managed by the platform in accordance with the underlying Kubernetes deployment.

To define requirements for single runs, developers need to include in the run specification the resource definition, in accordance with the schema.

For example, to request for a certain amount of compute resources, the spec must contain the detailed definition as follows:

```yaml
resources:
  cpu:
    requests: 8
  mem:
    requests: 32Gi
  gpu:
    limits: "1"
```

In order to provide such definitions, users can leverage the SDK or the Core UI to programmatically or interactively define their request.
Please see the [Kubernetes Resources](https://scc-digitalhub.github.io/sdk-docs/runtimes/kubernetes-resources/) section of the documentation for more information.


### Resource templates and profiles

It is possible to rely on a set of preconfigured HW profiles defined during the platform deployment. 
The profile allow for abstracting the platform users from the underlying complexity. Each profile corresponds to a specific resource configuration that defines a combination of requirements. For example, the profile may define a specific type of GPU, memory, and CPUs to be used. In this case it is sufficient to specify the corresponding profile name in the run execution configuration to allocate the corresponding resources.

The mechanism of profiles is described in the administration section of the documentation and is managed by the platform admins. Please see [Resource templates](https://scc-digitalhub.github.io/docs/admin/) section of the documentation for more information.

Please note that the requirements defined in the template have priority over those defined by the user and are not overwritten.


