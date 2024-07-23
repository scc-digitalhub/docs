# KubeFlow Pipelines

[Kubeflow Pipelines](https://www.kubeflow.org/docs/components/pipelines) makes part of the Kubeflow platform and allows for organizing workflows out of single tasks performed as Kubernetes Jobs via Argo Workflows. Kubeflow Pipelines comes with its own DSL specification on top of Python, which is compiled into a workflow definition ready for execution in Kubernetes. In this way wach task, its resources, dependencies, etc may be configured indipendently; the management and tracking is performed by the Kubeflow Pipelines component, equipped also with the Web-based UI for monitoring.  

The platform used Kubeflow pipelines to

- implement the composite pipelines through its Core orchestrator component and UI
- support MLRun pipelines. 

Currently, version v1 of the Kubeflow Pipelines is used for the compatibility purposes. The definition of the KFP workflows is provided in the corresponding [KFP Runtime](../runtimes/kfp_pipelines.md) section.

!!! info "How to access"

    Kubeflow Pipelines UI may be accessed from the [dashboard](dashboard.md). From its interface, you will be able to monitor the deployed workflows and their executions.

## Resources

- [Official documentation](https://www.kubeflow.org/docs/components/pipelines)
- 