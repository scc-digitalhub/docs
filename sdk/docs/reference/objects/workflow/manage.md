---
render_macros: true
---

# Manage workflows

The methods below retrieve, import, update, or delete workflows. They can be called directly from the SDK or through a `Project` object. When using a `Project` object, omit the `project` parameter and pass the other parameters as keyword arguments.

## Read

Use the read methods to retrieve workflows from the backend or import them from a YAML descriptor.

{{ function_doc("get_workflow", "digitalhub.entities", separate_examples=True) }}

{{ function_doc("get_workflow_versions", "digitalhub.entities", separate_examples=True) }}

{{ function_doc("list_workflows", "digitalhub.entities", separate_examples=True) }}

{{ function_doc("import_workflow", "digitalhub.entities", separate_examples=True) }}

## Update

Update a workflow after changing its mutable metadata.

{{ function_doc("update_workflow", "digitalhub.entities", separate_examples=True) }}

## Delete

Delete one workflow version or all versions of a workflow.

{{ function_doc("delete_workflow", "digitalhub.entities", separate_examples=True) }}

{{ page_navigation(("Create", "create.md"), ("Use", "use.md")) }}
