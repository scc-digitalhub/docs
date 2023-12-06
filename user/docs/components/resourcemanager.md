# Kubernetes Resource Manager

**Kubernetes Resource Manager** (KRM) is an application to manage several types of Kubernetes resources:

- Custom resources
- Services
- Deployments
- Volumes
- Jobs

It consists in a back-end, written in *Java*, which connects to the Kubernetes API to perform actions on resources, and a front-end, written in *React* and based on [React-admin](https://marmelab.com/react-admin/).

Instructions on how to install and start an instance can be found on the [repository](https://github.com/scc-digitalhub/custom-resource-manager).

## Standard Kubernetes Resources

With KRM you can control the main Kubernetes resources (e.g., services, deployments), manage Persistent Volume Claims, and access the secrets.Click the corresponding button in the left menu, and view the details of one item by clicking its *Show* button. 

## Custom resources

Custom resources can be viewed, created, edited and deleted through the use of the interface. 

If you don't see a specific kind of custom resource listed to the left, it means neither Kubernetes nor KRM contain a schema for it. A schema is required so that the application may understand and describe the related resources.

If some resources already exist, they will be immediately be visible.
