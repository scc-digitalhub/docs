# Core UI

The Core console is a front-end application backed by the  Core API. It provides a management interface 
for the organization and operations over the Data Science [Projects](../tasks/projects.md) and the associated entities, such as:

- **functions** of various runtimes (see the [Functions and Runtimes](../tasks/functions.md) section for details), as well as their executions (runs) grouped by the corresponding operations (tasks)
- **dataitems** - structured [Data Items](../tasks/data.md) managed by the project
- **artifacts** - unstructured files related and maanged by the project
- **models** - versioned ML Model artifacts with their metrics and metadata (see [ML Models](../tasks/models.md) section for details)

When you access the console, you land to the project management page, where you can create or delete projects.

## Create a Project

Start by clicking the `CREATE A NEW PROJECT` button.

![Project list](../images/console/project-list.png)

Fill the form's properties.
![Coder buttons](../images/console/project-form.png)

Following the selection of a project, you can get an overview of the associated objects on its dashboard and manage them on their dedicated pages.

## Dashboard

The console dashboard shows the resources that have been created with a series of cards and allows you to quickly access them. You can see the runs performed and their respective status, as well as artifacts, data items and functions.
![Coder buttons](../images/console/dashboard-prj.png)

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

All entities operated by Core are versioned. When you view the details of an object, all of its versions are listed and browsable. Moreover, when you view a dataitem, its schema and data preview are available.

## Running functions

The console can be used to create function runs. When you view a function, different operations are available depending on its kind (i.e., its runtime). For example, when you create a Nefertem function, you can then perform either `validate`, `profile`, `infer` or `metric` tasks providing the desired run configuration.
