# Dataitems

Dataitems are data objects which contain a dataset of a given type, stored in an addressable repository and accessible to every component able to understand the type (kind) and the source (path). Do note that data items could be stored in the artifact store as artifacts, but that is not a dependency or a requirement.

## Managing dataitems with SDK

Dataitems can be created and managed as *entities* with the SDK CRUD methods. This can be done directly from the package or through the `Project` object.
To manage dataitems, you need to have at least `digitalhub[data]` layer installed.

1. In the [CRUD section](./crud.md), we will see how to create, read, update and delete dataitems.
2. In the [methods section](./methods.md), we will see what can be done with the `Dataitem` object.
3. In the [kinds section](./kinds.md), we will see what kinds are supported.
