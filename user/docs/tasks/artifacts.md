# Artifacts

Artifacts (ARTIFACT) are (binary) objects stored in one of the artifact stores of the platform, and available to every process, module and component as files (or data streams).

## Managing artifacts with SDK

Artifacts can be created and managed as *entities* with the SDK CRUD methods. This can be done directly from the package or through the `Project` object.
To manage artifacts, you need to have `digitalhub_core` layer installed.

In the first section, we will see how to create, read, update and delete artifacts.
In the second section, we will see what can be done with the `Artifact` object.

### CRUD

An `artifact` is created entity can be managed with the following methods.

- **`new_artifact`**: create a new artifact
- **`get_artifact`**: get an artifact
- **`update_artifact`**: update an artifact
- **`delete_artifact`**: delete an artifact
- **`list_artifacts`**: list all artifacts

This is done in two ways. The first is through the SDK and the second is through the `Project` object.
Example:

```python
import digitalhub as dh

project = dh.get_or_create_project("my-project")

# From library
artifact = dh.new_artifact(project="my-project",
                           name="my-artifact",
                           kind="artifact",
                           path="s3://my-bucket/my-artifact.ext")

# From project
artifact = project.new_artifact(name="my-artifact",
                                kind="artifact",
                                path="s3://my-bucket/my-artifact.ext")
```

The syntax is the same for all CRUD methods. The following sections describe how to create, read, update and delete an artifact. It focus on managing artifacts from library. If you want to managie artifacts from the project, you can use the `Project` object and avoid to specify the `project` parameter.

#### Create

To create an artifact you can use the `new_artifact()` method.

The mandatory parameters are:

- **`project`**: the project in which the artifact will be created
- **`name`**: the name of the artifact
- **`kind`**: the kind of the artifact
- **`path`**: the remote path where the artifact is stored

The optional parameters are:

- **`uuid`**: the uuid of the artifact (this is automatically generated if not provided). **Must** be a valid uuid v4.
- **`description`**: the description of the artifact
- **`source`**: the remote source of the artifact (git repository)
- **`labels`**: the labels of the artifact
- **`embedded`**: whether the artifact is embedded or not. If `True`, the artifact is embedded (all the spec details are expressed) in the project. If `False`, the artifact is not embedded in the project
- **`src_path`**: local path of the artifact, used in case of upload into remote storage
- **`kwargs`**: keyword arguments passed to the *spec* constructor

Example:

```python
artifact = dh.new_artifact(project="my-project",
                           name="my-artifact",
                           kind="artifact",
                           path="s3://my-bucket/my-artifact.ext")
```

#### Read

To read an artifact you can use the `get_artifact()` or `import_artifact()` methods. The first one searches for the artifact into the backend, the second one load it from a local yaml.

##### Get

The mandatory parameters are:

- **`project`**: the project in which the artifact will be created

The optional parameters are:

- **`entity_name`**: to use the name of the artifact as identifier. It returns the latest version of the artifact
- **`entity_id`**: to use the uuid of the artifact as identifier. It returns the specified version of the artifact
- **`kwargs`**: keyword arguments passed to the client that comunicate with the backend

Example:

```python
artifact = dh.get_artifact(project="my-project",
                           entity_name="my-artifact")

artifact = dh.get_artifact(project="my-project",
                           entity_id="uuid-of-my-artifact")
```

##### Import

The mandatory parameters are:

- **`file`**: file path to the artifact yaml

Example:

```python
artifact = dh.import_artifact(file="./some-path/my-artifact.yaml")
```

#### Update

To update an artifact you can use the `update_artifact()` method.

The mandatory parameters are:

- **`artifact`**: artifact object to be updated

The optional parameters are:

- **`kwargs`**: keyword arguments passed to the client that comunicate with the backend

Example:

```python
artifact = dh.new_artifact(project="my-project",
                           name="my-artifact",
                           kind="artifact",
                           path="s3://my-bucket/my-artifact.ext")

artifact.metadata.description = "My new description"

artifact = dh.update_artifact(artifact=artifact)
```

#### Delete

To delete an artifact you can use the `delete_artifact()` method.

The mandatory parameters are:

- **`project`**: the project in which the artifact will be created

The optional parameters are:

- **`entity_name`**: to use the name of the artifact as identifier
- **`entity_id`**: to use the uuid of the artifact as identifier
- **`delete_all_versions`**: if `True`, all versions of the artifact will be deleted
- **`kwargs`**: keyword arguments passed to the client that comunicate with the backend

Example:

```python
artifact = dh.new_artifact(project="my-project",
                           name="my-artifact",
                           kind="artifact",
                           path="s3://my-bucket/my-artifact.ext")

dh.delete_artifact(project="my-project",
                   entity_id=artifact.id)
```

#### List

To list all artifacts you can use the `list_artifacts()` method.

The mandatory parameters are:

- **`project`**: the project in which the artifact will be created

The optional parameters are:

- **`kwargs`**: keyword arguments passed to the client that comunicate with the backend

Example:

```python
artifacts = dh.list_artifacts(project="my-project")
```

### Artifact object

The `Artifact` object is built using the `new_artifact()` method. There are several variations of the `Artifact` object based on the `kind` of the artifact. The SDK supports the following kinds:

- **`artifact`**: represents a generic artifact

For each different kind, the `Artifact` object has a different set of methods and different `spec`, `status` and `metadata`.
All the `Artifact` kinds have a `save()` and an `export()` method to save and export the *entity* artifact into backend or locally as yaml.

To create a specific artifact, you must use the desired `kind` in the `new_artifact()` method.

#### Artifact

The `artifact` kind indicates that the artifact is a generic artifact.
There are no specific `spec` parameters.

The `artifact` kind has the following methods:

- **`as_file()`**: collects the artifact into a local temporary file
- **`download()`**: downloads the artifact into a specified path
- **`upload()`**: uploads the artifact to a specified path

##### As file

The `as_file()` method returns the artifact as a temporary file. The file **is not** automatically deleted when the program ends.
The method returns the path of the downloaded artifact.

##### Download

The `download()` method downloads the artifact into a specified path.
The method returns the path of the downloaded artifact.
The method accepts the following parameters:

- **`target`**: remote path of the artifact to be downloaded (eg. `s3://my-bucket/my-artifact.ext`). By default, it is used the `spec` `path`
- **`dst`**: local path where the artifact will be downloaded. By default, it is in the current working directory
- **`overwrite`**: if `True`, the target path will be overwritten if it already exists

##### Upload

The `upload()` method uploads the artifact to a specified path.
The method returns the path of the uploaded artifact.
The method accepts the following parameters:

- **`source`**: local path of the artifact to be uploaded
- **`target`**: remote path of the artifact to be uploaded (eg. `s3://my-bucket/my-artifact.ext`). By default, it is used the `spec` `path`
