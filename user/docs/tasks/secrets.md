# Secret Management

Working with different operations may implu the usage of a sensitive values, such as external API credentials,
storage credentials, etc.

In order to avoid embedding the credentials in the code of functions, the platform supports an explicit management
of credentials as secrets. This operation exploits the underlying secret management subsystem, such as Kubernetes Secret Manager.

Besides the secrets managed natively by the platform to integrate e.g., default storage credentials, it is possible to
define custom secrets at the level of a single project. The project secrets are managed as any other project-related entities,
such as functions, dataitems, etc.

At the level of the project the secrets are represented as key-value pairs. The management of secrets is delegated to a secret
provider, and currently only Kubernetes Secret Manager is supported. Each project has its own Kubernetes secret, where
all the key-value pairs are stored.

To create a new secret value it is possible to use the Core UI console or directly via API, e.g., using the SDK.

## Creating and Managing Secrets via UI

Core console can be used to manage project secrets. To create a new one, it is necessary to provide
a secret key and a value to be stored.

![Create project secret](../images/console/secrets-create.png)

The entries may be then deleted and updated, as well as their metadata.

## Managing Secrets via SDK

Secrets can be created and managed as *entities* with the SDK CRUD methods.
Check the [SDK Secrets documentation](https://scc-digitalhub.github.io/sdk-docs/objects/secret/entity/) for more information.
