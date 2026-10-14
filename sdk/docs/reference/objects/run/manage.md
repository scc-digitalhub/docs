---
render_macros: true
---

# Manage runs

Use these methods to retrieve, import, update, or delete runs.

## Read

Retrieve runs from the backend or import them from a YAML descriptor.

{% call function_doc("get_run", "digitalhub.entities") %}
    === "Example"

        ```python
        import digitalhub as dh

        run = dh.get_run(
            identifier="my-run-id",
            project="my-project",
        )
        ```
{% endcall %}

{% call function_doc("list_runs", "digitalhub.entities") %}
    === "Example"

        ```python
        import digitalhub as dh

        runs = dh.list_runs(project="my-project")
        ```
{% endcall %}

{% call function_doc("import_run", "digitalhub.entities") %}
    === "Example"

        ```python
        import digitalhub as dh

        run = dh.import_run("my-run.yaml")
        ```
{% endcall %}

## Update

Update a run after changing its mutable metadata.

{% call function_doc("update_run", "digitalhub.entities") %}
    === "Example"

        ```python
        import digitalhub as dh

        run = dh.get_run(
            identifier="my-run-id",
            project="my-project",
        )
        run.set_description("Updated run")
        run = dh.update_run(run)
        ```
{% endcall %}

## Delete

Delete a run from the backend.

{% call function_doc("delete_run", "digitalhub.entities") %}
    === "Example"

        ```python
        import digitalhub as dh

        dh.delete_run(
            identifier="my-run-id",
            project="my-project",
        )
        ```
{% endcall %}

[Back to Run](./entity.md)
