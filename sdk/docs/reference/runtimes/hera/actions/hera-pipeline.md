# Hera Pipeline

## Pipeline reference

<div class="list-cards" markdown>

- [**Overview**](#overview){ .list-card-link } - Understand what the pipeline action does.

- [**Function**](#function){ .list-card-link } - Create a Hera Workflow.

- [**Task**](#task){ .list-card-link } - Configure the Hera pipeline Task.

- [**Run**](#run){ .list-card-link } - Execute the Hera pipeline.

</div>

## Overview

The `pipeline` action executes a Hera workflow on the platform. A `Task` is created by calling `run()` on the Workflow; task parameters are passed through that call.

The workflow is built automatically when `auto_build=True` and `workflow.spec.workflow` is `None`. Hera is used by the remote process that builds and runs the workflow, so it is not required in the client environment.

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
		| [handler](../../../configuration/code-sources.md#code-source-uri) | str | Function entrypoint. **Required.** The handler function must not accept arguments and must return a Hera `Workflow`. |
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

	A Task for the `pipeline` action is created when `workflow.run()` is called.

	=== "Parameters"

		Can only be specified when calling `workflow.run()`.

		| Name | Type | Description |
		| --- | --- | --- |
		| action | str | Task action. **Required. Must be `pipeline`** |
		| [volumes](../../../configuration/kubernetes.md#volumes) | list[dict] | List of volumes. |
		| [resources](../../../configuration/kubernetes.md#resources) | dict | Resource values with optional `cpu`, `mem`, `gpu` and `disk` keys. |
		| [envs](../../../configuration/kubernetes.md#secrets-and-envs) | list[dict] | Environment variables. |
		| [secrets](../../../configuration/kubernetes.md#secrets-and-envs) | list[str] | List of secret names. |
		| [profile](../../../configuration/kubernetes.md#profile) | str | Profile template. |

	=== "Creation example"

		```python
		run = workflow.run(action="pipeline")
		```

### Task methods

The Hera pipeline Task does not add runtime-specific methods.

## Run

??? example "Create a run"

	Execute the Hera pipeline and return the resulting `Run` entity.

	After an explicit `workflow.build()`, run the pipeline with `auto_build=False`.

	=== "Parameters"

		Can only be specified when calling `workflow.run()`.

		| Name | Type | Description |
		| --- | --- | --- |
		| auto_build | bool | Whether to invoke `build()` automatically when `workflow.spec.workflow` is `None`. Defaults to `True`. |
		| parameters | dict | Values for the Hera workflow parameters declared in the pipeline source. |

	=== "Creation example"

		```python
		run = workflow.run(
			action="pipeline",
			auto_build=True,
			parameters={"url": "https://example.com"},
			wait=True,
		)
		```

### Run methods

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
