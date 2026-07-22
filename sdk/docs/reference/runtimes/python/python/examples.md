# Examples

## Function Creation

```python
import digitalhub as dh

project = dh.get_or_create_project("my_project")

# Create function from project
function = project.new_function(
    name="python-function",
    kind="python",
    code_src="main.py",
    handler="function",
    python_version="PYTHON3_10"
)

# Or create function from SDK
function = dh.new_function(
    project="my-project",
    name="python-function",
    kind="python",
    code_src="main.py",
    handler="function",
    python_version="PYTHON3_10"
)
```

## Task Execution

**Job execution:**

```python
run = function.run(
    action="job",
    inputs={"dataitem": dataitem.key},
    parameters={"param1": "value1"},
)
```

**Build image:**

```python
run = function.run(
    action="build",
    instructions=["apt-get install -y git"]
)
```

**Serve as service:**

```python
run = function.run(
    action="serve",
    replicas=2,
    service_type="NodePort"
)
```

## Service Invocation

After deploying a service:

```python
run = function.run("serve", ...)

# Pass some data to the function
json_data = {
    "some-func-param": data
}

# run invoke returns a requests.Response object
run.invoke(json=json_data)

# Run invoke method accept requests.request parameters.
# It accepts also url parameter. The url MUST start
# with a valid HTTP scheme (http:// or https://) and should
# include the service url. To check the service url:
run.status.service['url']
```

## Tutorials

Find additional examples in the [tutorial repository](https://github.com/scc-digitalhub/digitalhub-tutorials) of the DSLab GitHub organization.
