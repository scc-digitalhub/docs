# Data and transformations

The platform supports data of different type to be stored and operated by the underlying storage subsystems. 

Digital Hub natively supports two types of storages: 

- *persistence* object storage (datalake S3 Minio), which manages immutable data in the form of files. 
-  *operational* relational data storage (PostgreSQL database), which is used for efficient querying of mutable data. *Postgres* 
   is rich with extensions, most notably for geo-spatial and time-series data.

The data is represented in the platform as entities of different types, depending on its usage and format. More specifically, we distinguish

- *data items* which represent immutable tabular datasets resulting from different transformation operations and ready for use in differerent types of analysis. Data items are enriched with metadata (e.g., versions, lineage, stats, profiling, schema) and unique keys and managed and persisted to the datalake directly by the platform in the form of Apache Parquet files.
- *artifacts* which represent arbitrary files stored to the datalake with some extra metadata, but are not limited to tabular formats.

Each data entity may be accessed and manipulated by the platform via UI or using the API, e.g., with SDK.

## Manipulating data via UI
### Artifacts

Artifacts can be created and managed as *entities* with the console. This can be done accessing through the user's menu or using the shortcut on the dashboard.

![Artifact intro](../images/console/artifacts-intro.png)

Pressing on Artifact side menu button, the paginated list of the artifacts is showed. From this pages is possible:

-  `create` a new artifact
-  `expand` an artifact and see the last 5 versions
-  `show` the details of an artifact 
-  `edit` an artifact
-  `delete` an artifact
-  `filter` the artifact by name and kind

![Artifact list](../images/console/artifacts-list.png)

In the next section, we will see how to create, read, update and delete artifacts.

#### CRUD

Here we analyze how to Create, Read, Update and Delete Artifacts using the UI, similarly to what happens with the SDK.

##### Create

A project is created pressing the button `CREATE` in the Artifacts' list page. After pressing the button, the dialog asking the Artifact's parameter is shown:

![Artifact form](../images/console/artifacts-form.png)

It has the following mandatory parameters:
The mandatory parameters are:

- **`name`**: the name of the artifact
- **`kind`**: the kind of the artifact

The only `Metadata` mandatory parameter is:

- **`path`**: the remote path where the artifact is stored

The other `Metadata` parameters are optional and mutable after the creation:

- **`name`**: the name of the artifact
- **`version`**: the version of the artifact
- **`description`**: a human readable description of the artifact
- **`updated`**: the date of the last modification made to the artifact
- **`src_path`**: local path of the artifact, used in case of upload into remote storage
- **`labels`**: the labels of the artifact


##### Read

To read an artifact you can click on the `SHOW` button.

![Artifact read](../images/console/artifacts-read.png)

The page shows the following details

- **`id`**: the id of the artifact
- **`kind`**: the kind of the artifact
- **`Key`**: the unique URL that identifies the resource

The `Metadata` values are:
- **`name`**: the name of the artifact
- **`description`**: a human readable description of the artifact
- **`version`**: the version of the artifact
- **`created`**: the date of the creation to the artifact
- **`updated`**: the date of the last modification made to the artifact
- **`labels`**: the labels of the artifact
- **`path`**: the remote path where the artifact is stored
- **`src_path`**: local path of the artifact, used in case of upload into remote storage

On the right side of this page are all the version of the resource is listed and the actual version is highlighted. Selecting a different element
the different version is shown.

![Artifacts version](../images/console/artifacts-version.png)

From the menu on top is possible to `EDIT`, `DELETE`, `INSPECT` or `EXPORT` the current artifact. For the first 2 options there are specific section
of this document. 

Clicking on `INSPECTOR` a dialog that shows the artifact in JSON format is shown.

![Artifact inspector](../images/console/artifacts-inspector.png)

Clicking the `EXPORT` button the artifact is downloaded in a yaml file.


##### Update

You can update artifact's `Metadata` pressing the button `EDIT` in the list or in the show page. All the `Metadata` values can be modified

- **`name`**: the name of the artifact
- **`description`**: a human readable description of the artifact
- **`version`**: the version of the artifact
- **`updated`**: the date of the last modification made to the artifact
- **`labels`**: the labels of the artifact
- **`path`**: the remote path where the artifact is stored
- **`src_path`**: local path of the artifact, used in case of upload into remote storage

![Artifact edit](../images/console/artifact-edit.png)

##### Delete

You can delete an artifact from the list or from the detail pressing the button `DELETE`. A dialog asking confirmation is shown 

![Artifact delete](../images/console/artifact-delete.png)


### Dataitems

Dataitems can be created and managed as *entities* with the console. This can be done accessing through the user's menu or using the shortcut on the dashboard.

![Dataitem intro](../images/console/artifacts-intro.png)

Pressing on Data items side menu button, the paginated list of the resource is showed. From this pages is possible:

-  `create` a new dataitem
-  `expand` an dataitem and see the last 5 versions
-  `show` the details of an dataitem 
-  `edit` an dataitem
-  `delete` an dataitem
-  `filter` the dataitem by name and kind

![Dataitem list](../images/console/dataitems-list.png)

In the next section, we will see how to create, read, update and delete dataitems.

#### CRUD

Here we analyze how to Create, Read, Update and Delete Dataitems using the UI, similarly to what happens with the SDK.

##### Create

A project is created pressing the button `CREATE` in the Dataitems' list page. After pressing the button, the dialog asking the Dataitem's parameter is shown:

![Dataitem form](../images/console/dataitems-form.png)

It has the following mandatory parameters:
The mandatory parameters are:

- **`name`**: the name of the dataitem
- **`kind`**: the kind of the dataitem

The only `Metadata` mandatory parameter is:

- **`path`**: the remote path where the dataitem is stored

The other `Metadata` parameters are optional and mutable after the creation:

- **`name`**: the name of the dataitem
- **`version`**: the version of the dataitem
- **`description`**: a human readable description of the dataitem
- **`updated`**: the date of the last modification made to the dataitem
- **`src_path`**: local path of the dataitem, used in case of upload into remote storage
- **`labels`**: the labels of the dataitem


###### Kind

There are 2 possible kinds for dataitems:

- **`Dataitem`**: indicates that the dataitem is a generic dataitem. There are no specific attributes in the creation page.
- **`table`**: indicates that the dataitem point to a table. The optional parameter is the schema of the table in [table_schema](https://specs.frictionlessdata.io/table-schema/) format

##### Read

To read an dataitem you can click on the `SHOW` button.

![Dataitem read](../images/console/dataitems-read.png)

The page shows the following details

- **`id`**: the id of the dataitem
- **`kind`**: the kind of the dataitem
- **`Key`**: the unique URL that identifies the resource

The `Metadata` values are:

- **`name`**: the name of the dataitem
- **`description`**: a human readable description of the dataitem
- **`version`**: the version of the dataitem
- **`created`**: the date of the creation to the dataitem
- **`updated`**: the date of the last modification made to the dataitem
- **`labels`**: the labels of the dataitem
- **`path`**: the remote path where the dataitem is stored

Based on the kind of the dataitem, there may be **`schema`**, indicates that the dataitem point to a table.

On the right side of this page are all the version of the resource is listed and the actual version is highlighted. Selecting a different element
the different version is shown.

![Dataitems version](../images/console/dataitems-version.png)

From the menu on top is possible to `EDIT`, `DELETE`, `INSPECT` or `EXPORT` the current dataitem. For the first 2 options there are specific section
of this document. 

Clicking on `INSPECTOR` a dialog that shows the dataitem in JSON format is shown.

![Dataitems inspector](../images/console/dataitems-inspector.png)

Clicking the `EXPORT` button the dataitem is downloaded in a yaml file.


##### Update

You can update dataitem's `Metadata` pressing the button `EDIT` in the list or in the show page. All the `Metadata` values can be modified

- **`name`**: the name of the dataitem
- **`description`**: a human readable description of the dataitem
- **`version`**: the version of the dataitem
- **`updated`**: the date of the last modification made to the dataitem
- **`labels`**: the labels of the dataitem
- **`path`**: the remote path where the dataitem is stored

Based on the kind of the dataitem, there may be **`schema`**, indicates that the dataitem point to a table.

![Dataitems edit](../images/console/dataitems-edit.png)

##### Delete

You can delete an dataitem from the list or from the detail pressing the button `DELETE`. A dialog asking confirmation is shown 

![Dataitems delete](../images/console/dataitems-delete.png)

## Manipulating data via SDK
TODO
