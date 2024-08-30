# Using Kubernetes Resources for Runs

## Managing Kubernetes Resources with SDK

When it come to execution of AI tasks, either batch jobs or model serving, it is important to be able to
allocate an appropriate set of resources, such as memory, GPU, node types, etc.

For this purpose the platform relies on the standard Kubernetes functionality and resource definitions. More specifically,
the run configuration may have a specific requirements for

- node selection
- volumes (Persistent Volume Claims and Config Maps)
- HW resources in terms of CPU and memory requests and limits, numbers of GPUs
- Kubernetes affinity definition and/or toleration properties
- Additional secrets and environment variables to be associated with the execution

In the platform, these requirements may be defined in two ways.

First, it is possible to configure them explictly when defining the function run, either via Core UI or via SDK. Please note that it is possible to describe only some of these properties, leaving the rest blank without constraints. All the defaults are managed by the underlying Kubernetes deployment.

Second, it is possible to rely on a set of preconfigured HW profiles defined by the platform deployment. The mechanism of profiles is described in the administration section of the documentation and is managed by the platform admins. The profile allow for abstracting the platform users from the underlying complexity. Each profile corresponds to a specific resource configuration that defines a combination of requirements. For example, the profile may define a specific type of GPU, memory, and CPUs to be used. In this case it is sufficient to specify the corresponding profile name in the run execution configuration to allocate the corresponding resources.

Please note that the requirements defined in the template have priority over those defined by the user and are not overwritten.

With SDK you can manage Kubernetes resources for your tasks. When you run a function, you can require some Kubernetes resources for the task. Resources and data are specified in the `function.run()` method.

Please see the [Kubernetes Resources](https://scc-digitalhub.github.io/sdk-docs/runtimes/kubernetes-resources/) section of the documentation for more information.
