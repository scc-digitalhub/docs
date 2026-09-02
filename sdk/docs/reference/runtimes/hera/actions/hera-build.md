# Hera Build

The `build` action builds the pipeline definition in Argo YAML format. A `Task` is created by calling `run()` on the Workflow; task parameters are passed through that call.

## Overview

The Hera build action imports the workflow source, calls its handler without arguments, and serializes the returned Hera `Workflow` to Argo Workflows YAML. It does not execute the generated workflow.

The source must include a `handler` and at least one of `code_src`, `code` or `base64`. The only supported source language is Python, which is also the default.

An explicit build is optional before a `pipeline` run because `auto_build=True` builds the workflow automatically. Use `workflow.build()` when you need a separate build run or want to access the generated YAML.

## Quick example

```python
workflow = dh.new_workflow(
    name="my-workflow",
    kind="hera",
    code_src="pipeline.py",
    handler="pipeline"
)

run = workflow.build(
    wait=True
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
| [handler](../../../configuration/code_src/overview.md#handler) | str | Function entrypoint. **Required.** The handler function must not accept arguments and must return a Hera `Workflow`. |
| lang | str | Source code language. Only `python` is supported; defaults to `python`. |

### Task Parameters

Can only be specified when calling `workflow.run()`.

| Name | Type | Description |
| --- | --- | --- |
| action | str | Task action. **Required. Must be `build`** |
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
| parameters | dict | Stored in the run specification but ignored by the current build executor. |

## Entity methods

### Run methods

The build result is available through `run.results()["workflow"]` or `run.result("workflow")`. The value is the generated YAML encoded as base64.

::: digitalhub_runtime_hera.entities.run._base.entity.RunHeraRun.results
    options:
        heading_level: 6
        show_signature: false
        show_source: false
        show_root_heading: true
        show_symbol_type_heading: true
        show_root_full_path: false
        show_root_toc_entry: true

::: digitalhub_runtime_hera.entities.run._base.entity.RunHeraRun.result
    options:
        heading_level: 6
        show_signature: false
        show_source: false
        show_root_heading: true
        show_symbol_type_heading: true
        show_root_full_path: false
        show_root_toc_entry: true
