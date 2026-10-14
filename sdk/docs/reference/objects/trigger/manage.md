---
render_macros: true
---

# Manage triggers

The CRUD methods read, update, and delete triggers. For creation, see [Create a trigger](./create.md) and the examples in each trigger kind.

## Read

Use the read methods to retrieve triggers from the backend or load them from a YAML descriptor.

{% call function_doc("get_trigger", "digitalhub.entities") %}
    === "Example"

        ```python
        import digitalhub as dh

        trigger = dh.get_trigger(
            identifier="daily-run",
            project="my-project",
        )
        ```
{% endcall %}

{% call function_doc("list_triggers", "digitalhub.entities") %}
    === "Example"

        ```python
        import digitalhub as dh

        triggers = dh.list_triggers(project="my-project")
        ```
{% endcall %}

{% call function_doc("import_trigger", "digitalhub.entities") %}
    === "Example"

        ```python
        import digitalhub as dh

        trigger = dh.import_trigger("my-trigger.yaml")
        ```
{% endcall %}

## Update

Update a trigger after changing its mutable metadata.

{% call function_doc("update_trigger", "digitalhub.entities") %}
    === "Example"

        ```python
        import digitalhub as dh

        trigger = dh.get_trigger(
            identifier="daily-run",
            project="my-project",
        )
        trigger.set_description("Updated trigger")
        trigger = dh.update_trigger(trigger)
        ```
{% endcall %}

## Delete

Delete one trigger version or all versions of a trigger.

{% call function_doc("delete_trigger", "digitalhub.entities") %}
    === "Example"

        ```python
        import digitalhub as dh

        dh.delete_trigger(
            identifier="daily-run",
            project="my-project",
            delete_all_versions=True,
        )
        ```
{% endcall %}

[Back to Triggers](./entity.md)
