# Secrets

Working with different operations may imply the usage of a sensitive values, such as external API credentials, storage credentials, etc.
In order to avoid embedding the credentials in the code of functions, you can explicitly manage credentials as secrets. This operation exploits the underlying secret management subsystem, such as Kubernetes Secret Manager.

It is possible to define custom secrets at the level of a single project. The project secrets are managed as any other project-related entities, such as functions, dataitems, etc.

At the level of the project the secrets are represented as key-value pairs. The management of secrets is delegated to a secret provider, and currently only Kubernetes Secret Manager is supported. Each project has its own Kubernetes secret, where all the key-value pairs are stored.

## Managing secrets with SDK

Secrets can be created and managed as *entities* with the SDK CRUD methods. This can be done directly from the package or through the `Project` object.

1. In the [CRUD section](./crud.md), we will see how to create, read, update and delete secrets.
2. In the [methods section](./methods.md), we will see what can be done with the `Secret` object.
