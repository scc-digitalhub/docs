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

## Managing projects via UI
TODO


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
