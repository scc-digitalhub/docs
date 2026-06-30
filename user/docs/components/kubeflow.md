# KubeFlow Pipelines

[Kubeflow Pipelines](https://www.kubeflow.org/docs/components/pipelines) makes part of the Kubeflow platform and allows for organizing workflows out of single tasks performed as Kubernetes Jobs via Argo Workflows. Kubeflow Pipelines comes with its own DSL specification on top of Python, which is compiled into a workflow definition ready for execution in Kubernetes. In this way, each task, its resources, dependencies, etc may be configured indipendently; management and tracking are performed by the Kubeflow Pipelines component, also equipped with the Web-based UI for monitoring.  

The platform uses Kubeflow Pipelines to implement the composite pipelines through its Core orchestrator component and UI.

Currently, version v1 of Kubeflow Pipelines is used for compatibility purposes. The definition of the KFP workflows is provided in the corresponding [KFP Runtime](../runtimes/kfp_pipelines.md) section.

!!! info "How to access"

    Kubeflow Pipelines UI may be accessed from the [dashboard](dashboard.md). From its interface, you will be able to monitor the deployed workflows and their executions.

## Resources

- [Official documentation](https://www.kubeflow.org/docs/components/pipelines)
