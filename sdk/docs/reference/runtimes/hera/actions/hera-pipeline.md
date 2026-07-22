# Hera Pipeline

The `pipeline` action executes the built pipeline on Kubernetes. A `Task` is created by calling `run()` on the Workflow; task parameters are passed through that call.

## Overview

The Hera pipeline action executes the compiled Argo Workflows pipeline on the Kubernetes cluster. This action runs the actual workflow with the provided parameters.

## Quick example

```python
workflow = dh.new_workflow(
    name="my-workflow",
    kind="hera",
    code_src="pipeline.py",
    handler="pipeline"
)

run = workflow.run(
    action="pipeline",
    parameters={"url": "https://example.com"}
)
```

## Parameters

### Workflow Parameters

Must be specified when creating the workflow.

| Name | Type | Description |
| --- | --- | --- |
| project | str | Project name. Required only when creating from the library; otherwise **MUST NOT** be set. |
| name | str | Name that identifies the object. **Required.** |
| kind | str | Workflow kind. Must be `hera`. **Required.** |
| uuid | str | Object ID in UUID4 format. |
| description | str | Description of the object. |
| labels | list[str] | List of labels. |
| embedded | bool | Whether the object should be embedded in the project. |
| [code_src](../../../configuration/code_src/overview.md#code-source-uri) | str | URI pointing to the source code. |
| [code](../../../configuration/code_src/overview.md#plain-text-source) | str | Source code provided as plain text. |
| base64 | str | Source code encoded as base64. |
| [handler](../../../configuration/code_src/overview.md#handler) | str | Function entrypoint. |
| lang | str | Source code language (informational). |

### Task Parameters

Can only be specified when calling `workflow.run()`.

| Name | Type | Description |
| --- | --- | --- |
| action | str | Task action. **Required. Must be `pipeline`** |
| [volumes](../../../configuration/kubernetes/overview.md#volumes) | list[dict] | List of volumes. |
| [resources](../../../configuration/kubernetes/overview.md#resources) | dict | Resource limits/requests. |
| [envs](../../../configuration/kubernetes/overview.md#secrets-envs) | list[dict] | Environment variables. |
| [secrets](../../../configuration/kubernetes/overview.md#secrets-envs) | list[str] | List of secret names. |
| [profile](../../../configuration/kubernetes/overview.md#profile) | str | Profile template. |

### Run Parameters

Can only be specified when calling `workflow.run()`.

| Name | Type | Description |
| --- | --- | --- |
| parameters | dict | Inputs for the pipeline execution. |

## Entity methods

### Run methods

No runtime-specific helper methods are available for this action.
