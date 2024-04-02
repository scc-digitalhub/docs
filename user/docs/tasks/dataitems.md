# Dataitems

Data items (DATAITEM) are data objects which contain a dataset of a given type, stored in an addressable repository and accessible to every component able to understand the type (kind) and the source (path). Do note that data items could be stored in the artifact store as artifacts, but that is not a dependency or a requirement.

## Managing dataitems with SDK

Dataitems can be created and managed as *entities* with the SDK CRUD methods. This can be done directly from the package or through the `Project` object.
To manage dataitems, you need to have `digitalhub_data` layer installed.

In the first section, we will see how to create, read, update and delete dataitems.
In the second section, we will see what can be done with the `Dataitem` object.

### CRUD

An `dataitem` is created entity can be managed with the following methods.

- **`new_dataitem`**: create a new dataitem
- **`get_dataitem`**: get a dataitem
- **`update_dataitem`**: update a dataitem
- **`delete_dataitem`**: delete a dataitem
- **`list_dataitems`**: list all dataitems

This is done in two ways. The first is through the SDK and the second is through the `Project` object.
Example:

```python
import digitalhub as dh

project = dh.get_or_create_project("my-project")

# From library
dataitem = dh.new_dataitem(project="my-project",
                           name="my-dataitem",
                           kind="dataitem",
                           path="s3://my-bucket/my-dataitem.ext")

# From project
dataitem = project.new_dataitem(name="my-dataitem",
                                kind="dataitem",
                                path="s3://my-bucket/my-dataitem.ext")
```

The syntax is the same for all CRUD methods. The following sections describe how to create, read, update and delete a dataitem. It focus on managing dataitems from library. If you want to managie dataitems from the project, you can use the `Project` object and avoid to specify the `project` parameter.

#### Create

To create a dataitem you can use the `new_dataitem()` method.

The mandatory parameters are:

- **`project`**: the project in which the dataitem will be created
- **`name`**: the name of the dataitem
- **`kind`**: the kind of the dataitem
- **`path`**: the remote path where the dataitem is stored

The optional parameters are:

- **`uuid`**: the uuid of the dataitem (this is automatically generated if not provided). **Must** be a valid uuid v4.
- **`description`**: the description of the dataitem
- **`source`**: the remote source of the dataitem (git repository)
- **`labels`**: the labels of the dataitem
- **`embedded`**: whether the dataitem is embedded or not. If `True`, the dataitem is embedded (all the spec details are expressed) in the project. If `False`, the dataitem is not embedded in the project
- **`kwargs`**: keyword arguments passed to the *spec* constructor

Example:

```python
dataitem = dh.new_dataitem(project="my-project",
                           name="my-dataitem",
                           kind="dataitem",
                           path="s3://my-bucket/my-dataitem.ext")
```

#### Read

To read a dataitem you can use the `get_dataitem()` or `import_dataitem()` methods. The first one searches for the dataitem into the backend, the second one load it from a local yaml.

##### Get

The mandatory parameters are:

- **`project`**: the project in which the dataitem will be created

The optional parameters are:

- **`entity_name`**: to use the name of the dataitem as identifier. It returns the latest version of the dataitem
- **`entity_id`**: to use the uuid of the dataitem as identifier. It returns the specified version of the dataitem
- **`kwargs`**: keyword arguments passed to the client that comunicate with the backend

Example:

```python
dataitem = dh.get_dataitem(project="my-project",
                           entity_name="my-dataitem")

dataitem = dh.get_dataitem(project="my-project",
                           entity_id="uuid-of-my-dataitem")
```

##### Import

The mandatory parameters are:

- **`file`**: file path to the dataitem yaml

Example:

```python
dataitem = dh.import_dataitem(file="./some-path/my-dataitem.yaml")
```

#### Update

To update a dataitem you can use the `update_dataitem()` method.

The mandatory parameters are:

- **`dataitem`**: dataitem object to be updated

The optional parameters are:

- **`kwargs`**: keyword arguments passed to the client that comunicate with the backend

Example:

```python
dataitem = dh.new_dataitem(project="my-project",
                           name="my-dataitem",
                           kind="dataitem",
                           path="s3://my-bucket/my-dataitem.ext")

dataitem.metadata.description = "My new description"

dataitem = dh.update_dataitem(dataitem=dataitem)
```

#### Delete

To delete a dataitem you can use the `delete_dataitem()` method.

The mandatory parameters are:

- **`project`**: the project in which the dataitem will be created

The optional parameters are:

- **`entity_name`**: to use the name of the dataitem as identifier
- **`entity_id`**: to use the uuid of the dataitem as identifier
- **`delete_all_versions`**: if `True`, all versions of the dataitem will be deleted
- **`kwargs`**: keyword arguments passed to the client that comunicate with the backend

Example:

```python
dataitem = dh.new_dataitem(project="my-project",
                           name="my-dataitem",
                           kind="dataitem",
                           path="s3://my-bucket/my-dataitem.ext")

dh.delete_dataitem(project="my-project",
                   entity_id=dataitem.id)
```

#### List

To list all dataitems you can use the `list_dataitems()` method.

The mandatory parameters are:

- **`project`**: the project in which the dataitem will be created

The optional parameters are:

- **`kwargs`**: keyword arguments passed to the client that comunicate with the backend

Example:

```python
dataitems = dh.list_dataitems(project="my-project")
```

### Dataitem object

The `Dataitem` object is built using the `new_dataitem()` method. There are several variations of the `Dataitem` object based on the `kind` of the dataitem. The SDK supports the following kinds:

- **`dataitem`**: represents a generic dataitem
- **`table`**: represents a table dataitem

For each different kind, the `Dataitem` object has a different set of methods and different `spec`, `status` and `metadata`.

To create a specific dataitem, you must use the desired `kind` in the `new_dataitem()` method.
All the `Dataitem` kinds have a `save()` and an `export()` method to save and export the *entity* dataitem into backend or locally as yaml.

#### Dataitem

The `dataitem` kind indicates that the dataitem is a generic dataitem.
There are no specific `spec` parameters nor specific method exposed. It acts as a generic dataitem.

#### Table

The `table` kind indicates that the dataitem point to a table.
The optional `spec` parameters are:

- **`schema`**: the schema of the table in [table_schema](https://specs.frictionlessdata.io/table-schema/) format

The `table` kind also has the following methods:

- **`as_df()`**: to collect the data in a pandas dataframe
- **`write_df()`**: to write the dataitem as parquet

##### Read table

The `as_df()` method returns the data in a pandas dataframe.
The method accepts the following parameters:

- **`format`**: the format of the data. If not provided, the format will be inferred from the file extension. We support **ONLY** parquet or csv.
- **`kwargs`**: keyword arguments passed to the pandas `read_parquet` or `read_csv` method

##### Write table

The `write_df()` method writes the dataitem as parquet.
The method accepts the following parameters:

- **`target_path`**: the path of the target parquet file. If not provided, the target path will created by the SDK and the dataitem will be stored in the default store
- **`kwargs`**: keyword arguments passed to the pandas `to_parquet` method
