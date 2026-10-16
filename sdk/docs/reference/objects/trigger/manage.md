---
render_macros: true
---

# Manage triggers

The CRUD methods read, update, and delete triggers. For creation, see [Create a trigger](./create.md) and the examples in each trigger kind.

## Read

Use the read methods to retrieve triggers from the backend or load them from a YAML descriptor.

{{ function_doc("get_trigger", "digitalhub.entities", separate_examples=True) }}

{{ function_doc("list_triggers", "digitalhub.entities", separate_examples=True) }}

{{ function_doc("import_trigger", "digitalhub.entities", separate_examples=True) }}

## Update

Update a trigger after changing its mutable metadata.

{{ function_doc("update_trigger", "digitalhub.entities", separate_examples=True) }}

## Delete

Delete one trigger version or all versions of a trigger.

{{ function_doc("delete_trigger", "digitalhub.entities", separate_examples=True) }}

{{ page_navigation(("Create", "create.md"), ("Use", "use.md")) }}
