# Custom Resource Manager

**Custom Resource Manager** (CRM) is an application to manage several types of Kubernetes resources:

- Custom resources
- Services
- Deployments
- Volumes
- Jobs

It consists in a back-end, written in *Java*, which connects to the Kubernetes API to perform actions on resources, and a front-end, written in *React* and based on [React-admin](https://marmelab.com/react-admin/).

Instructions on how to install and start an instance can be found on the [repository](https://github.com/scc-digitalhub/custom-resource-manager).

## Services, Deployments

You can list services or deployments by clicking the corresponding button in the left menu, and view the details of one item by clicking its *Show* button. 

## Custom resources

Custom resources can be viewed, created, edited and deleted through the use of the interface. 

If you don't see a specific kind of custom resource listed to the left, it means neither Kubernetes nor KRM contain a schema for it. A schema is required so that the application may understand and describe the related resources.

Creating a schema is fairly simple. Access the **Settings** section from the left menu and click *Create*.

The **CRD** drop-down menu will list all *Custom Resource Definitions* available on the Kubernetes instance; when you pick one, the **Version** field will automatically be filled with the version of the currently active schema.

Providing the **Schema** may seem daunting, but you can simply leave it empty and click *Save*, and it will automatically be built from the currently active schema.

!!! warning "Automatic schema specification"

    When the schema is built automatically, you will need to *Edit* it afterwards, to add the `"$schema":"https://json-schema.org/draft/2020-12/schema"` property at root level, like this:

    ``` json
    {"$schema":"https://json-schema.org/draft/2020-12/schema",...}
    ```

    This property is required by the *OpenAPI* specification, yet is missing from the properties present in Kubernetes. Until a solution to make it compliant is implemented, it will have to be manually added after automatic creation.

If some resources already exist, they will be immediately be visible.
