---
render_macros: true
---

# Manage workflows

The methods below retrieve, import, update, or delete workflows. They can be called directly from the SDK or through a `Project` object. When using a `Project` object, omit the `project` parameter and pass the other parameters as keyword arguments.

## Read

Use the read methods to retrieve workflows from the backend or import them from a YAML descriptor.

{% call function_doc("get_workflow", "digitalhub.entities") %}
    === "Example"

        ```python
        import digitalhub as dh

        workflow = dh.get_workflow(
            identifier="my-workflow",
            project="my-project",
        )
        ```
{% endcall %}

{% call function_doc("get_workflow_versions", "digitalhub.entities") %}
    === "Example"

        ```python
        import digitalhub as dh

        workflows = dh.get_workflow_versions(
            identifier="my-workflow",
            project="my-project",
        )
        ```
{% endcall %}

{% call function_doc("list_workflows", "digitalhub.entities") %}
    === "Example"

        ```python
        import digitalhub as dh

        workflows = dh.list_workflows(project="my-project")
        ```
{% endcall %}

{% call function_doc("import_workflow", "digitalhub.entities") %}
    === "Example"

        ```python
        import digitalhub as dh

        workflow = dh.import_workflow("my-workflow.yaml")
        ```
{% endcall %}

## Update

Update a workflow after changing its mutable metadata.

{% call function_doc("update_workflow", "digitalhub.entities") %}
    === "Example"

        ```python
        import digitalhub as dh

        workflow = dh.get_workflow(
            identifier="my-workflow",
            project="my-project",
        )
        workflow.set_description("Updated workflow")
        workflow = dh.update_workflow(workflow)
        ```
{% endcall %}

## Delete

Delete one workflow version or all versions of a workflow.

{% call function_doc("delete_workflow", "digitalhub.entities") %}
    === "Example"

        ```python
        import digitalhub as dh

        dh.delete_workflow(
            identifier="my-workflow",
            project="my-project",
            delete_all_versions=True,
        )
        ```
{% endcall %}

[Back to Workflow](./entity.md)
