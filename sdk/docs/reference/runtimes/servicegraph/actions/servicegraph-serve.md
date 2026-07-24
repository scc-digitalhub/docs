# ServiceGraph Serve

The `serve` action deploys a pipeline as a service on Kubernetes. A `Task` is created by calling `run()` on the Function; task parameters are passed through that call.

## Overview

## Quick example

```python
function = dh.new_function(
    name="my-servicegraph-service",
    kind="servicegraph",
    code_src="src/flow.yaml"
)

run = function.run(action="serve", 
    parameters={"input.url": "http://videosource:1984"},
    service_ports=[{"port": 7777, "target_port": 7777}]
    )

```

## Parameters

### Function Parameters

Must be specified when creating the function.

| Name | Type | Description |
| --- | --- | --- |
| project | str | Project name. Required only when creating from the library; otherwise **MUST NOT** be set. |
| name | str | Name that identifies the object. **Required.** |
| kind | str | Function kind. Must be `huggingfaceserve`. **Required.** |
| uuid | str | Object ID in UUID4 format. |
| description | str | Description of the object. |
| labels | list[str] | List of labels. |
| embedded | bool | Whether the object should be embedded in the project. |
| [code_src](../../../configuration/code_src/overview.md#code-source-uri) | str | URI pointing to the YAML of the pipeline. |
| [code](../../../configuration/code_src/overview.md#plain-text-source) | str | Pipeline code YAML provided as plain text. |
| base64 | str | Pipeline definition encoded as base64. |
| [image](#model-image) | str | Docker image where to serve the model. |

The pipeline code should be defined following the specification defined in [ServiceGraph](https://github.com/scc-digitalhub/digitalhub-servicegraph) project.

### Task Parameters

Can only be specified when calling `function.run()`.

| Name | Type | Description |
| --- | --- | --- |
| action | str | Task action. **Required. Must be `serve`** |
| service_ports | list[dict] | List of service ports. |
| [service_type](../../../configuration/kubernetes/overview.md#service-port-type) | str | Service type. |
| service_name | str | Service name. |
| [replicas](../../../configuration/kubernetes/overview.md#replicas) | int | Number of replicas. |
| [volumes](../../../configuration/kubernetes/overview.md#volumes) | list[dict] | List of volumes. |
| [resources](../../../configuration/kubernetes/overview.md#resources) | dict | Resource limits/requests. |
| [envs](../../../configuration/kubernetes/overview.md#secrets-envs) | list[dict] | Environment variables. |
| [secrets](../../../configuration/kubernetes/overview.md#secrets-envs) | list[str] | List of secret names. |
| [profile](../../../configuration/kubernetes/overview.md#profile) | str | Profile template. |


### Run Parameters

Can only be specified when calling `function.run()`.

| Name | Type | Description |
| --- | --- | --- |
| parameters | dict | Task parameters to customize the flow properties. |

