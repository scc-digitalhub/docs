# Examples

## ServiceGraph Example

```python
import digitalhub as dh

project = dh.get_or_create_project("my_project")

function = project.new_function(name="servicegraph-function",
                                kind="servicegraph",
                                code_src="src/flow.yaml")

run = function.run(action="serve", 
    parameters={"input.url": "http://videosource:1984"},
    service_ports=[{"port": 7777, "target_port": 7777}]
    )
```

## Service Invocation for Graphs with HTTP source

```python
# Prepare input data
input_data = {"inputs": "Your input text here"}

# Invoke the service
response = run.invoke(json=input_data)

# Run invoke method accept requests.request parameters.
# It accepts also url parameter. The url MUST start
# with a valid HTTP scheme (http:// or https://) and should
# include the service url. To check the service url:
run.status.service['url']
```

## Tutorials

Find additional examples in the [tutorial repository](https://github.com/scc-digitalhub/digitalhub-tutorials) of the DSLab GitHub organization.
