# Digital Hub Core UI

The Digital Hub console is a front-end application backed by the Digital Hub Core API. It provides a management interface 
for the organization and operations over the Data Science [Projects](../tasks/projects.md) and the associated entities, such as:

- **functions** of various runtimes (see the [Functions and Runtimes](../tasks/functions.md) section for details), as well as their executions (runs) grouped by the corresponding operations (tasks)
- **dataitems** - structured [Data Items](../tasks/data.md) managed by the project
- **artifacts** - unstructured files related and maanged by the project
- **models** - versioned ML Model artifacts with their metrics and metadata (see [ML Models](../tasks/models.md) section for details)

When you access the console, you land to the project management page, where you can create or delete projects.

## Create a Project

In order to create a new project, press the button on the first element of the list

![Coder buttons](../images/console/project-create.png)

Now you can fill the form with the data of your new project, adding Name, Description and its Metadata
![Coder buttons](../images/console/project-form.png)

Following the selection of a project, you can get an overview of the associated objects on its dashboard and manage them on the dedicated pages.

## Dashboard

The console dashboard shows the resources that have been created with a series of cards and allows you to quickly access them. In addition to the artifacts, data items and functions, the last card shows the runs present and their respective status
![Coder buttons](../images/console/dashboard.png)

## Objects
TODO
### Functions
TODO
### Dataitems 
TODO
### Artifacts 
TODO
### ML Models
TODO
### Secrets
TODO

## Versioning

All the entities operated by Core are versioned. When you visualize the details of an object, all of its versions are listed and browsable. Moreover, when you visualize a dataitem, its schema and data preview are available.

## Running functions

The console can be used to create function runs. When you visualize a function, different operations are available depending on its kind (i.e., its runtime). For example, when you create a Nefertem function, you can then perform either `validate`, `profile`, `infer` or `metric` tasks providing the desired run configuration.

