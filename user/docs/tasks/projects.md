# Projects

A project in Digital Hub is a container for everything (code, assets, configuration, ...) that concerns an application.

Often, they have a structure like this:
```
my-project           # Parent directory of the project (context)
├── data             # Data for local tests
├── docs             # Documentation
├── src              # Source code (functions, libs, workflows)
├── tests            # Unit tests (pytest) for functions
├── project.yaml     # MLRun project spec file
├── README.md        # README file
└── requirements.txt # Default Python requirements file
```

Projects may be created and managed from the UI, but also by using DH Core's API using, e.g, Python SDK. 

## Managing Projects via UI

In the following sections we document the Project management through UI available using the  `Digital Hub Console`.

### CRUD

Here we analyze how to Create, Read, Update and Delete Projects using the UI, similarly to what happens with the SDK

#### Create

A project is created pressing the button `CREATE` in the Homepage od the Console.

![Project create](../images/console/project-create.png)

After pressing the button, the dialog asking the Project's parameter is shown:

![Project form](../images/console/project-form.png)

 It has the following mandatory parameters:

- **`name`**: the name of the project, it is also the identifier of the project 
- **`description`**: a human readable description of the project

The other `Metadata` parameters are optional and mutable after the creation:

- **`name`**: the name of the project
- **`description`**: a human readable description of the project
- **`updated`**: the date of the last modification made to the project
- **`labels`**: a list of labels (strings)

Pressing on the `Save` button, the project is added to the list of the projects in Homepage
#### Read

In the Home Page are listed all the projects present in the database. The tile shows:

- **`name`**: the name of the project
- **`id`**: the identifier of the project
- **`created`**: the date of the creation of the project
- **`updated`**: the date of the last modification made to the project

On the bottom the button for `Open` and enter in the Project and the `Delete`

![Project form](../images/console/project-tile.png)

Clicking on the `Open` button, the following Dashboard is shown

![Dashboard](../images/console/dashboard-prj.png)

This dashboard reports a summary of the resources associated with the project and a series
of features to access the management of these resources.
 
- **`Artifacts`**: the number and the list of the last Artifacts created
- **`Data items`**: the number and the list of the last Data items created
- **`Functions and code`**: the number and the list of the last Functions created
- **`Jobs and runs`**: the status and list of runs performed

From any page of the dashboard it is possible to change the project by selecting from the menu at the top of the bar

![Dashboard](../images/console/root-project.png)

#### Update

You can update a project `Metadata` pressing the button `Configuration` in the side Menubar.

![Configuration](../images/console/configuration.png)

Pressing the `Edit` button on the top right of the page the form for editing the `Metadata` values of the project is shown.
In the example below, the labels `test` and `prj1` are added

![Update conf](../images/console/update-prj.png)
After the modification, pressing Save the new configuration is stored

#### Delete

You can delete a project from the `Home page`  and from the `Configuration` pressing the `Delete` button.
For confirm the choice of deleting, insert the name of the project in the dialog

![Update conf](../images/console/project-delete.png)


## Managing projects via SDK

Here we look briefly at how to do it from a Jupyter Python notebook. Access your Jupyter instance and create a new notebook.

Import the `digitalhub` library:
``` python
import digitalhub as dh
```

### Create
TODO: align

A new project is created with ``get_or_create_project`` method: the only required fields is `name` (`my-project`).
``` python
project = dh.get_or_create_project("my-project")
```

You can check in the interface that the project has been created: go to Digital Hub to see the project successfully created.

### Load
TODO: align


### Delete
TODO: align
