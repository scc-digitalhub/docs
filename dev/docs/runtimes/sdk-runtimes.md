# Digitalhub-core SDK runtime implementation

On the `digitalhub` sdk side, to implement a new runtime it is required to define a new package that includes:

- Function specifications, status and metadata
- One or more task specifications, status and metadata
- A run specification, status and metadata
- A runtime class that handle execution
- Registries that allow sdk to import the required objects.

As an implementation example, we describe the creation of dbt runtime.

## Define a new package

First of all, we need to decide what runtime we want to implement. In our case, we want to create a runtime based on DBT.

The package we create **MUST** be compliant with this naming convention:

`digitalhub_<core/data/ml/ai>_<...>`

According to the specific functionality of the runtime, the package can be part of one of the 4 digitalhub layer.
Between the second brackets goes the name of the runtime which is the kind of the function we will implement. This is because a runtime corresponds to a function.

In our case the package is named `digitalhub_data_dbt`.

Is up to the developer to choose the way of installing the package. For `digitalhub_data_dbt` we use a `pyproject.toml` file for installation.

```toml
[build-system]
requires = ["setuptools", "wheel"]
build-backend = "setuptools.build_meta"

[project]
name = "digitalhub-data-dbt"
version = "0.2.3"
description = "DBT runtime for DHCore"
readme = "README.md"
authors = [
    { name = "Fondazione Bruno Kessler", email = "dslab@fbk.eu" },
    ...
]
license = { file = "LICENSE.txt" }
classifiers = [
    "License :: OSI Approved :: Apache Software License",
    "Programming Language :: Python :: 3.9",
    "Programming Language :: Python :: 3.10"
]
keywords = ["data", "dataops", "kubernetes"]
requires-python = ">=3.9"
dependencies = [
"digitalhub-data~=0.2",
]

[project.optional-dependencies]
local = [
    "dbt-postgres",
]
...
```

Please note that the external dependencies for the runtime  are placed in optional dependencies. Why? Because by default we want to support remote execution through `kubernetes`. Of course, the local execution **MUST** have all the dependencies required by the runtime in the python environment, but the remote execution only needs the function, task and run files definition. With this strategy, we can avoid some dependencies conflict with the digitalhub-core execution environment. This means that defined function, tasks and run **MUST NOT** contain elements that require external library dependencies, but **ONLY** python standard library or digitalhub core dependencies.

The package then requires, as bare minimum, an `__init__.py` top level file, function spec file, one or more task spec modules and a runtime module.

The folder structure could be like this:

```text
├── pyproject.toml            # Installation file
└── digitalhub_data_dbt       # Package name
    ├── entities
    │   ├── functions         # Function specification
    │   │   ├── spec.py
    │   |   ├── status.py
    │   |   └── metadata.py
    │   ├── tasks             # Task specification
    │   │   ├── spec.py
    │   │   ├── status.py
    │   │   └── metadata.py
    │   ├── runs              # Run specification
    │   │   ├── spec.py
    │   │   ├── status.py
    │   │   └── metadata.py
    │   └── registries.py     # Spec and status registires
    ├── runtime
    │   └── runtime.py        # Runtime class definition
    └── `__init__.py`           # Init file where to put runtime registry
```

Of course, if more modules are needed, treat the runtime implementation like any other python package creation.

## Definition of Function

We create three new modules in the `entities/functions` directory (spec.py, status.py and metadata.py).
In the spec.py file we define a FunctionSpec object that inherits from FunctionSpec.
The Spec object defines the specification of the function (e.g. reference to the code to be executed, sql query, etc.).
The Params object models how the arguments must be provided (e.g. code must be a str, etc.).

```python
"""
Dbt Function specification module.
"""
from __future__ import annotations

from digitalhub_core.entities.functions.spec import FunctionParams, FunctionSpec
from digitalhub_core.utils.exceptions import EntityError
from digitalhub_core.utils.generic_utils import decode_string, encode_string


class FunctionSpecDbt(FunctionSpec):
    """
    Specification for a Function Dbt.
    """

    def __init__(
        self,
        source: str | None = None,
        sql: str | None = None,
        **kwargs,
    ) -> None:
        """
        Constructor.

        Parameters
        ----------
        sql : str
            SQL query to run inside Dbt.
        """
        super().__init__(source, **kwargs)
        if sql is None:
            raise EntityError("SQL query must be provided.")

        # This is to avoid re-encoding the SQL query when
        # it is already encoded.
        try:
            sql = decode_string(sql)
        except Exception:
            ...
        self.sql = encode_string(sql)


class FunctionParamsDbt(FunctionParams):
    """
    Function Dbt parameters model.
    """

    sql: str = None
    """SQL query to run inside the container."""
```

In the status.py file we define a FunctionStatus object that inherits from FunctionStatus.

```python
"""
Dbt Function status module.
"""
from __future__ import annotations

from digitalhub_core.entities.functions.status import FunctionStatus


class FunctionStatusDbt(FunctionStatus):
    """
    Function Dbt status.
    """
```

Finally, in the metadata.py file we define a FunctionMetadata object that inherits from FunctionMetadata.

```python
"""
Dbt Function metadata module.
"""
from __future__ import annotations

from digitalhub_core.entities.functions.metadata import FunctionMetadata

class FunctionMetadataDbt(FunctionMetadata):
    """
    Function Dbt metadata.
    """
```

## Definition of Task

Once the function specifications are defined, we can create one or more tasks associated with the function. In the case of DBT, we have only one kind of task: `transform`. Similarly to the function definition procedure, we need to define the new specifications and relative model schema.

```python
"""
Task Transform specification module.
"""
from __future__ import annotations

from digitalhub_core.entities.tasks.spec import TaskParams, TaskSpec


class TaskSpecTransform(TaskSpec):
    """Task Transform specification."""


class TaskParamsTransform(TaskParams):
    """
    TaskParamsTransform model.
    """
```

Note that in the case of the transform task we do not have particular requirements for the specifications.
You must do the same for status and metadata.

## Definition of Run

The run is defined in the same way as the function and task.

Run spec:

```python
"""
Run specification module.
"""
from __future__ import annotations

from digitalhub_core.entities.runs.spec import RunParams, RunSpec
from pydantic import BaseModel


class RunSpecDbt(RunSpec):
    """Run Dbt specification."""

    def __init__(
        self,
        task: str,
        task_id: str,
        inputs: dict | None = None,
        outputs: dict | None = None,
        parameters: dict | None = None,
        local_execution: bool = False,
        function_spec: dict | None = None,
        transform_spec: dict | None = None,
        **kwargs,
    ) -> None:
        """
        Constructor.

        Parameters
        ----------
        """
        super().__init__(task, task_id, inputs, outputs, parameters, local_execution, **kwargs)
        self.function_spec = function_spec
        self.transform_spec = transform_spec


class DataitemList(BaseModel):
    """Dataitem list model."""

    dataitems: list[str]
    """List of dataitem names."""


class RunParamsDbt(RunParams):
    """Run Dbt parameters."""

    inputs: DataitemList
    """List of input dataitem names. Override RunSpec.inputs."""

    outputs: DataitemList
    """List of output dataitem names. Override RunSpec.outputs."""

    function_spec: dict = None
    """The function spec."""

    transform_spec: dict = None
    """The transform task spec."""
```

Run status:

```python
"""
Run status module.
"""
from __future__ import annotations

from digitalhub_core.entities.runs.status import RunStatus
from digitalhub_data.entities.dataitems.crud import get_dataitem_from_key
from digitalhub_data.entities.runs.results import RunResultsData


class RunStatusDbt(RunStatus):
    """
    Run Dbt status.
    """

    def __init__(
        self,
        state: str | None = None,
        message: str | None = None,
        results: dict | None = None,
        outputs: dict | None = None,
        **kwargs,
    ) -> None:
        """
        Constructor.

        Parameters
        ----------
        results : dict
            Runtime results.
        outputs : dict
            Runtime entities outputs.
        **kwargs
            Keyword arguments.


        See Also
        --------
        Status.__init__
        """
        super().__init__(state, message)
        self.results = results
        self.outputs = outputs

    def get_results(self) -> dict:
        """
        Get results.

        Returns
        -------
        dict
            The results.
        """
        dataitems = self.outputs.get("dataitems", [])
        dataitem_objs = [get_dataitem_from_key(dti.get("id")) for dti in dataitems]
        return RunResultsData(dataitems=dataitem_objs)
```

## Definition of Runtime

Once the task is defined, we finally need to create the runtime object which takes care of the run building and execution. We first create a new module like digitalhub_data_dbt/runtimes/runtime.py. In this module we import the base runtime class and define the specific operation that the runtime can execute:

```python
"""
Runtime DBT module.
"""
# Imports

class RuntimeDbt(Runtime):
    """
    Runtime Dbt class.
    """

    allowed_actions = ["transform"]

    def __init__(self) -> None:
        """
        Constructor.
        """
        super().__init__()
        ...

    def build(self, function: dict, task: dict, run: dict) -> dict:
        """
        Build run spec.

        Parameters
        ----------
        function : dict
            The function.
        task : dict
            The task.
        run : dict
            The run.

        Returns
        -------
        dict
            The run spec.
        """
        task_kind = task.get("kind").split("+")[1]
        return {
            "function_spec": function.get("spec", {}),
            f"{task_kind}_spec": task.get("spec", {}),
            **run.get("spec", {}),
        }

    def run(self, run: dict) -> dict:
        """
        Run function.

        Parameters
        ----------
        run : dict
            The run.

        Returns
        -------
        dict
            Status of the executed run.
        """
        # Handle execution of functions

    @staticmethod
    def _get_executable(action: str) -> Callable:
        """
        Select function according to action.

        Parameters
        ----------
        action : str
            Action to execute.

        Returns
        -------
        Callable
            Function to execute.
        """
        if action == "transform":
            return transform
        raise NotImplementedError
```

A runtime object must implement various methods.

To the build() method we pass a dictionary representation of function, task and run. This method returns the new run specification.
To the run() method we pass a run dictionary representation. This method parses the specification and determines which kind of task must be executed.

## Registries

There are three registry that need to be instantiated:

- *Runtime registry*
- *Spec registry*
- *Status registry*

*Runtime registry* goes in the package top level `__init__.py` file. The sdk uses a specific object to import the new classes.
The `__init__.py` will look like this:

```python
from digitalhub_core.runtimes.registry import RuntimeRegistry

registry = RuntimeRegistry()
registry.register("digitalhub_data_dbt.runtimes.runtime", "RuntimeDbt")
```

The registries for statuses and specs are located into a registries.py file in the entities directory.
It will look like this:

```python
from __future__ import annotations

from digitalhub_core.entities._base.spec import SpecRegistry
from digitalhub_core.entities._base.status import StatusRegistry

status_registry = StatusRegistry()
status_registry.register("dbt", "digitalhub_core.entities.functions.status", "FunctionStatus")
status_registry.register("dbt+transform", "digitalhub_core.entities.tasks.status", "TaskStatus")
status_registry.register("dbt+run", "digitalhub_data_dbt.entities.runs.status", "RunStatusDbt")

spec_registry = SpecRegistry()
spec_registry.register("dbt", "digitalhub_data_dbt.entities.functions.spec", "FunctionSpecDbt", "FunctionParamsDbt")
spec_registry.register(
    "dbt+transform", "digitalhub_data_dbt.entities.tasks.spec", "TaskSpecTransform", "TaskParamsTransform"
)
spec_registry.register("dbt+run", "digitalhub_data_dbt.entities.runs.spec", "RunSpecDbt", "RunParamsDbt")
```
