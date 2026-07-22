# Quickstart

This quickstart shows a minimal, copy-paste Python example. It creates a handler that returns a greeting, registers it with a project, runs it, and prints the result.

Prerequisite: an environment where the SDK is available (installed into the active virtualenv).

- Create a file named `hello.py` with the handler:

```python
from digitalhub_runtime_python import handler

@handler(outputs=["message"])
def hello(name: str = "world"):
    return f"Hello, {name}!"
```

- Create a short script `run_hello.py` that registers the function and runs it:

```python
import digitalhub as dh

project = dh.get_or_create_project(name="hello-quickstart", description="Quickstart project")

func = project.new_function(
    name="hello",
    kind="python",
    code_src="hello.py",
    handler="hello",
    python_version="PYTHON3_10",
)

run = func.run(action="job", parameters={"name": "World"}, wait=True)

print(run.output("message"))
```
