---
render_macros: true
---

# Manage tasks

Tasks are unversioned and belong to a project. Use these methods to retrieve, import, load, update, or delete tasks.

## Read

{% call function_doc("get_task", "digitalhub.entities") %}
    === "Example"

        ```python
        import digitalhub as dh

        task = dh.get_task(
            identifier="my-task-id",
            project="my-project",
        )
        ```
{% endcall %}

{% call function_doc("list_tasks", "digitalhub.entities") %}
    === "Example"

        ```python
        import digitalhub as dh

        tasks = dh.list_tasks(project="my-project")
        ```
{% endcall %}

{% call function_doc("import_task", "digitalhub.entities") %}
    === "Example"

        ```python
        import digitalhub as dh

        task = dh.import_task("my-task.yaml")
        ```
{% endcall %}

{% call function_doc("load_task", "digitalhub.entities") %}
    === "Example"

        ```python
        import digitalhub as dh

        task = dh.load_task("my-task.yaml")
        ```
{% endcall %}

## Update

Update a task after changing its mutable metadata. Its specification is immutable where required by the backend.

{% call function_doc("update_task", "digitalhub.entities") %}
    === "Example"

        ```python
        import digitalhub as dh

        task = dh.get_task(
            identifier="my-task-id",
            project="my-project",
        )
        task.set_description("Updated task")
        task = dh.update_task(task)
        ```
{% endcall %}

## Delete

Delete a task from the backend.

{% call function_doc("delete_task", "digitalhub.entities") %}
    === "Example"

        ```python
        import digitalhub as dh

        dh.delete_task(
            identifier="my-task-id",
            project="my-project",
        )
        ```
{% endcall %}

[Back to Task](./entity.md)
