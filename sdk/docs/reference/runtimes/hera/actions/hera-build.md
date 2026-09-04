# Hera Build

## Build reference

<div class="list-cards" markdown>

- [**Overview**](#overview){ .list-card-link } - Understand what the build action does.

- [**Function**](#function){ .list-card-link } - Create a Hera Workflow.

- [**Task**](#task){ .list-card-link } - Configure the Hera build Task.

- [**Run**](#run){ .list-card-link } - Build the Hera workflow.

</div>

## Overview

The `build` action builds the pipeline definition in Argo YAML format. A `Task` is created by calling `run()` on the Workflow; task parameters are passed through that call.

The Hera build action imports the workflow source, calls its handler without arguments, and serializes the returned Hera `Workflow` to Argo Workflows YAML. It does not execute the generated workflow.

The source must include a `handler` and at least one of `code_src`, `code` or `base64`. The only supported source language is Python, which is also the default.

An explicit build is optional before a `pipeline` run because `auto_build=True` builds the workflow automatically. Use `workflow.build()` when you need a separate build run or want to access the generated YAML.

## Function

??? example "Create a function"

    Define the Workflow with a Python source and handler that returns a Hera `Workflow`.

    === "Parameters"

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
        | [code_src](../../../configuration/code-sources.md#code-source-uri) | str | URI pointing to the source code. |
        | [code](../../../configuration/code-sources.md#plain-text-source) | str | Source code provided as plain text. |
        | base64 | str | Source code encoded as base64. |
        | [handler](../../../configuration/code-sources.md#handler) | str | Function entrypoint. **Required.** The handler function must not accept arguments and must return a Hera `Workflow`. |
        | lang | str | Source code language. Only `python` is supported; defaults to `python`. |

    === "Creation example"

        ```python
        workflow = dh.new_workflow(
            name="my-workflow",
            kind="hera",
            code_src="pipeline.py",
            handler="pipeline"
        )
        ```

### Function methods

??? example "build"

    Build the workflow using the build action.

    ::: digitalhub_runtime_hera.entities.workflow.hera.entity.WorkflowHera.build
        options:
            heading_level: 6
            show_signature: false
            show_docstring_description: true
            show_source: false
            show_root_heading: true
            show_symbol_type_heading: true
            show_root_full_path: false
            show_root_toc_entry: true

## Task

??? example "Create a task"

    === "Parameters"

        Can only be specified when calling `workflow.run()`.

        | Name | Type | Description |
        | --- | --- | --- |
        | action | str | Task action. **Required. Must be `build`** |
        | [volumes](../../../configuration/kubernetes.md#volumes) | list[dict] | List of volumes. |
        | [resources](../../../configuration/kubernetes.md#resources) | dict | Resource values with optional `cpu`, `mem`, `gpu` and `disk` keys. |
        | [envs](../../../configuration/kubernetes.md#secrets-and-envs) | list[dict] | Environment variables. |
        | [secrets](../../../configuration/kubernetes.md#secrets-and-envs) | list[str] | List of secret names. |
        | [profile](../../../configuration/kubernetes.md#profile) | str | Profile template. |

    === "Creation example"

        ```python
        run = workflow.run(action="build")
        ```

### Task methods

The Hera build Task does not add runtime-specific methods.

## Run

??? example "Create a run"

    === "Parameters"

        Can only be specified when calling `workflow.run()`.

        | Name | Type | Description |
        | --- | --- | --- |
        | auto_build | bool | Whether to invoke `build()` automatically when `workflow.spec.workflow` is `None`. Defaults to `True`. |
        | parameters | dict | Stored in the run specification but ignored by the current build executor. |

    === "Creation example"

        ```python
        run = workflow.build(
            wait=True
        )
        ```

### Run methods

The build result is available through `run.results()["workflow"]` or `run.result("workflow")`. The value is the generated YAML encoded as base64.

??? example "results"

    Get the results returned by the run.

    ::: digitalhub_runtime_hera.entities.run._base.entity.RunHeraRun.results
        options:
            heading_level: 6
            show_signature: false
            show_docstring_description: true
            show_source: false
            show_root_heading: true
            show_symbol_type_heading: true
            show_root_full_path: false
            show_root_toc_entry: true

??? example "result"

    Get a result by name.

    ::: digitalhub_runtime_hera.entities.run._base.entity.RunHeraRun.result
        options:
            heading_level: 6
            show_signature: false
            show_docstring_description: true
            show_source: false
            show_root_heading: true
            show_symbol_type_heading: true
            show_root_full_path: false
            show_root_toc_entry: true
