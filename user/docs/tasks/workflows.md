# Workflows

Workflows allow for organizing the single operations in a advanced management pipelines, to perform a series operation of data processing, ML model training and serving, etc. Workflows represent long-running procedures defined as Directed Acyclic Graphs (DAGs) where each node is a single unit of work performed by the platform (e.g., as a Kubernetes Job).

As in case of functions, it is possible for the platform to have different workflow runtimes. Currently, the only workflow runtime implemented is the one based on Kubeflow Pipelines infrastructure. See [KFP Runtime](../runtimes/kfp_pipelines.md) for further details about how the workflow is defined and executed with the Kubeflow Pipelines component of the platform.

Similarly, to functions the workflows may be managed via console UI or via Python SDK.

## Management via UI

Workflows can be created and managed as *entities* from the console. You can access them from the dashboard or the left menu. You can:

- `create` a new workflow
- `expand` a workflow to see its 5 latest versions
- `show` the details of a workflow
- `edit` a workflow
- `delete` a workflow
- `filter` workflows by name and kind

![Workflow list](../images/console/workflow-list.png)

We will now see how to [create](#create), [read](#read), [update](#update) and [delete](#delete) workflows using the UI, similarly to what is done with the SDK.

### Create

Click `CREATE` and a form will be shown:

![Workflow form](../images/console/workflow-form.png)

Mandatory fields are:

- **`Name`**: name and identifier of the workflow
- **`Kind`**: kind of workflow

Metadata fields are optional and may be updated later.

- **`Description`**: a human-readable description
- **`Labels`**: list of labels
- **`Name`**: name of the function
- **`Embedded`**: flag for embedded metadata
- **`Versioning`**: version of the function
- **`Openmetadata`**: flag to publish metadata
- **`Audit`**: author of creation and modification

In case of a `kfp` workflow, the source code and handler fields are required as well.

### Read

Click `SHOW` to view a workflow's details.

![Workflow read](../images/console/workflow-read.png)

On the right side, all versions of the resource are listed, with the current one highlighted. By clicking a different version, values displayed will change accordingly.

The `INSPECTOR` button will show a dialog containing the resource in JSON format.

![Workflow inspector](../images/console/workflow-inspector.png)

The `EXPORT` button will download the resource's information as a yaml file.

In case of ``kfp`` workflows, the executions of the workflow instances can be monitored with the corresponding DAG viewer.

![Workflow run](../images/scenario-etl/pipeline.png)

### Update

You can update a workflow by clicking `EDIT`. Greyed-out fields may not be updated.

### Delete

You can delete a workflow from either its detail page or the list of workflows, by clicking `DELETE`.

## Management via SDK

Workflows can be created and managed as *entities* with the SDK CRUD methods.
Check the [SDK Workflows documentation](https://scc-digitalhub.github.io/sdk-docs/objects/workflow/entity/) for more information.
