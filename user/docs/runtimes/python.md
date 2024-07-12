# Python

The **python runtime** allows you to run generic python function within the platform.
The runtime introduces a function of kind `python` and three task of kind `job`, `serve` and `build`.

## Prerequisites

Python version and libraries:

- `python >= 3.9`
- `digitalhub-runtime-python`

The package is available on PyPI:

```bash
python -m pip install digitalhub-runtime-python
```

## HOW TO

With the python runtime you can use the function's `run()` method to execute a python function you have defined.
The python runtime execution workflow follows roughly these steps:

1. Define somewhere a [python function](./python.md#python-function-definition).
2. Create a `Function` object in the platform and execute the function's `run()` method.
3. The runtime collects the [inputs](./python.md#run) specified in the function as SDK objects (`Dataitem`, `Artifact`, `Model`).
4. It fetches the function [source code](./python.md#source-code) and import the function handler.
5. It [composes](./python.md#parameters-composition) the parameters for the handler function.
6. It executes the function and map the outputs as SDK objects or as simple results.

### Python function definition

You can declare a generic python function as usual with the `def` keyword.
There are some restriction that must be applied when defining the function:

1. The argument `project` is reserved. The runtime overrides the function parameters and assign to the `project` argument a `Project` object, used as SDK context. With the `Project` object you can manipulate entities like `Artifact`, `Dataitem`, etc. If you provide a `project` argument into the function and use it as a non `Project` object, you will probably get an error. If you define the `project` argument into your functions signature, you can use the `project` variable as `Project` object.
2. The arguments `context` and `events` are reserved in remote execution. These arguments are reserved for `nuclio` `context` and `events` function parameters. If you define these arguments into your functions signature, you can use the `context` and `events` variables as `nuclio` `context` and `events` objects.
3. If some arguments of the function refer to some SDK objects, they must be mapped inside the run's `inputs` parameter. Other arguments of the function can be mapped inside the run's `parameter` parameter. More on that on the [Parameters composition](./python.md#parameters-composition) section.
4. You may or may not decorate your function with the `@handler` decorator you can import from the `digitalhub_runtime_python` package. If you decorate your function and return something, you need to map the outputs in the decorator and in the run's `outputs` parameter. More on that on the [Parameters composition](./python.md#parameters-composition) section.

#### Function definition example

```python
from digitalhub_runtime_python import handler

# 1. Simple function that returns a string

def func1():
   return "hello world"

# 2. Decorated function that returns a string

# If you decorate your function and return something, you need to map the outputs
# in the decorator and in the run's `outputs` parameter
@handler(outputs=["result"])
def func2():
   return "hello world"


# 3. Function with project argument
def func3(project):
   # allowed use of project variable
   project.log_artifact(name="example",
                        kind="artifact",
                         source_path="/path/to/file")

   # not allowed use of project variable
   project.some_method_not_from_sdk() # Probably there will be an error


# 4. Function with context and events arguments
def func4(context, events):
   # allowed use of context and events variables in remote execution
   context.logger.info("Some log")

# 5. Function with mixed input arguments
def func5(di: Dataitem, param1: str):
   # di refers to a Dataitem object, so it must be mapped
   # into runs inputs paramaters
   # param1 is a string, it must be mapped into runs input parameters
```

### Parameters composition

#### Inputs

To properly pass the parameters you need to your function, you must map them in the `function.run()` method.
Ther are some rules you need to follow:

- If you expect one of your arguments to be a `Dataitem`/`Artifact`/`Model` object, you need to explicit the reference to the object into the run's `inputs` parameter using the argument name as key and the object key as value.

```python

# Define your function and declare di argument as Dataitem
def func(di: Dataitem):
   # do something with di


# Create a dataitem
sdk_dataitem = sdk.new_dataitem(...)

# Reference the di argument as key and the dataitem key as value
sdk_function.run(inputs={"di": sdk_dataitem.key})
```

- Other function arguments must be mapped inside the run's `parameter` parameter.

```python

# Define your function and declare di argument as Dataitem
def func(di: Dataitem, param1: str):
   # do something with di


# Create a dataitem
sdk_dataitem = sdk.new_dataitem(...)

# Reference the di argument as key and the dataitem key as value
sdk_function.run(inputs={"di": sdk_dataitem.key},
                 parameter={"param1": "some value"})
```

#### Outputs

The outputs of the function must be mapped inside the run's `outputs` parameter if you return something and you decorate your function.

```python
from digitalhub_runtime_python import handler

@handler(outputs=["result", "other_result"])
def func(di: Dataitem, param1: str):
   # do something with di
   return "some value", "some other value"


sdk_function.run(inputs={"di": sdk_dataitem.key},
                 parameter={"param1": "some value"},
                 outputs={"result": "named_result",
                          "other_result": "named_other_result"})
```

### Source code

Once you have defined your function, you can store your code in several ways. You will then refernce the source code according to a specific `Function` parameter as shown in the following table:

| Format | Parameter | Type | Example |
| --- | --- | --- | --- |
| local file path | code_src | `str` | "path/to/file.py" |
| remote git repository | code_src | `str` | "git+https://github.com/some-user/some-repo" |
| zip s3 archive | code_src | `str` | "zip+s3://some-bucket/some-key.zip" |
| base64 encoded string | base64 | `str` | "encodedstring" |
| string | code | `str` | "def func():\n   return \"hello world\"" |

### Function

The python runtime introduces a function of kind `python`.

#### Function parameters

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| project | str | Project name | required (if creating from library) |
| name | str | Name that identifies the object | required |
| kind | str | Kind of the object | required (must be `python`) |
| uuid | str | ID of the object in form of UUID | None |
| description | str | Description of the object | None |
| git_source | str | Remote git source for object | None |
| labels | list[str] | List of labels | None |
| embedded | bool | Flag to determine if object must be embedded in project | True |
| code_src | str | Pointer to source code | None |
| code | str | Source code (plain text)| None |
| base64 | str | Source code (base64 encoded)| None |
| handler | str | Function entrypoint | None |
| init_function | str | Init function for remote nuclio execution | None |
| lang | str | Source code language (hint)| None |
| source | dict | Source code details as dictionary | None |
| python_version | str | Python version to use, must be one of: <li>`PYTHON3_9`</li><li>`PYTHON3_10`</li> | None |
| image | str | Image where the function will be executed | None |
| base_image | str | Base image used to build the image where the function will be executed | None (required when using `build` task) |
| requirements | list | Requirements list to be installed in the image where the function will be executed | None |

#### Function example

```python
import digitalhub_core as dh

# From project ...

function = project.new_function(name="python-function",
                                kind="python",
                                code_src="main.py",
                                handler="function",
                                python_version="PYTHON3_9")

# .. or from sdk

function = dh.new_function(project="my-project",
                           name="python-function",
                           kind="python",
                           source={
                              "source": "main.py",
                              "handler": "function",
                           }
                           python_version="PYTHON3_9")
```

### Task

The python runtime introduces three tasks of kind `job`, `serve` and `build` that allows you to run a python function execution, serving a function as a service or build a docker image where the function is executed.
A `Task` is created with the `run()` method, so it's not managed directly by the user. The parameters for the task creation are passed directly to the `run()` method, and may vary depending on the kind of task.

#### Task parameters

| Name | Type | Description | Default | Kind specific |
| --- | --- | --- | --- | --- |
| action | str | Task action. Must be one of: <li>`job`</li><li>`serve`</li><li>`build`</li> | required | |
| [node_selector](../tasks/kubernetes-resources.md#node_selector) | list[dict] | Node selector | None | |
| [volumes](../tasks/kubernetes-resources.md#volumes) | list[dict] | List of volumes | None | |
| [resources](../tasks/kubernetes-resources.md#resources) | dict | Resources restrictions | None | |
| [affinity](../tasks/kubernetes-resources.md#affinity) | dict | Affinity | None | |
| [tolerations](../tasks/kubernetes-resources.md#tolerations) | list[dict] | Tolerations | None | |
| [envs](../tasks/kubernetes-resources.md#envs) | list[dict] | Env variables | None | |
| [secrets](../tasks/kubernetes-resources.md#secrets) | list[str] | List of secret names | None | |
| backoff_limit | int | Backoff limit | None | `job` |
| instructions | list[str] | Build instructions to be executed as RUN instructions in Dockerfile.<br>Example: `apt install git -y` | None | `build` |
| replicas | int | Number of replicas | None | `serve` |
| service_type| str | Service type. Must be one of: <li>`ClusterIP`</li><li>`LoadBalancer`</li><li>`NodePort`</li> | `NodePort` | `serve` |

#### Task example

```python
run = function.run(
    action="job",
    backoff_limit=1,
)
```

### Run

The `Run` object is, similar to the `Task`, created with the `run()` method.
The run's parameters are passed alongside the task's ones.

#### Run parameters

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| loacal_execution | bool | Flag to indicate if the run will be executed locally | False |
| inputs | dict | Input entity key. | None |
| outputs | dict | Outputs mapped. | None |
| parameters | dict | Extra parameters for a function. | None |

#### Run example

```python
run = function.run(
    action="job",
    inputs={
        "dataitem": dataitem.key
    },
    outputs={
        "dataitem": "mapped-name",
        "label": "some-label"
    }
)
```
