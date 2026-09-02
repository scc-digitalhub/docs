# Hera Pipeline

The `pipeline` action executes a Hera workflow on the platform. A `Task` is created by calling `run()` on the Workflow; task parameters are passed through that call.

## Overview

The workflow is built automatically when `auto_build=True` and `workflow.spec.workflow` is `None`. Hera is used by the remote process that builds and runs the workflow, so it is not required in the client environment.

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
	auto_build=True,
	parameters={"url": "https://example.com"},
	wait=True,
)
```

After an explicit `workflow.build()`, run the pipeline with `auto_build=False`.

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
| [handler](../../../configuration/code_src/overview.md#handler) | str | Function entrypoint. **Required.** The handler function must not accept arguments and must return a Hera `Workflow`. |
| lang | str | Source code language. Only `python` is supported; defaults to `python`. |

### Task Parameters

Can only be specified when calling `workflow.run()`.

| Name | Type | Description |
| --- | --- | --- |
| action | str | Task action. **Required. Must be `pipeline`** |
| [volumes](../../../configuration/kubernetes/overview.md#volumes) | list[dict] | List of volumes. |
| [resources](../../../configuration/kubernetes/overview.md#resources) | dict | Resource limits/requests. |
| [envs](../../../configuration/kubernetes/overview.md#secrets-and-envs) | list[dict] | Environment variables. |
| [secrets](../../../configuration/kubernetes/overview.md#secrets-and-envs) | list[str] | List of secret names. |
| [profile](../../../configuration/kubernetes/overview.md#profile) | str | Profile template. |

### Run Parameters

Can only be specified when calling `workflow.run()`.

| Name | Type | Description |
| --- | --- | --- |
| auto_build | bool | Whether to invoke `build()` automatically when `workflow.spec.workflow` is `None`. Defaults to `True`. |
| parameters | dict | Values for the Hera workflow parameters declared in the pipeline source. |

## Entity methods

### Run methods

The run object exposes `results()` and `result(name)` for results returned by the remote pipeline run.
