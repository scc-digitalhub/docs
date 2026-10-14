---
render_macros: true
---

# Manage projects

The methods below retrieve, import, update, or delete projects. For project creation, see [Create a project](./create.md).

## Read

Use the read methods to retrieve projects from the backend or load them from a YAML descriptor.

{% call function_doc("get_project", "digitalhub.entities") %}
    === "Example"

        ```python
        import digitalhub as dh

        project = dh.get_project("my-project")
        ```
{% endcall %}

{% call function_doc("import_project", "digitalhub.entities") %}
    === "Example"

        ```python
        import digitalhub as dh

        project = dh.import_project("my-project.yaml")
        ```
{% endcall %}

{% call function_doc("load_project", "digitalhub.entities") %}
    === "Example"

        ```python
        import digitalhub as dh

        project = dh.load_project("my-project.yaml")
        ```
{% endcall %}

## Update

Update a project after changing its mutable metadata.

{% call function_doc("update_project", "digitalhub.entities") %}
    === "Example"

        ```python
        import digitalhub as dh

        project = dh.get_project("my-project")
        project.set_description("Updated project")
        project = dh.update_project(project)
        ```
{% endcall %}

## Delete

Delete a project from the backend.

{% call function_doc("delete_project", "digitalhub.entities") %}
    === "Example"

        ```python
        import digitalhub as dh

        dh.delete_project("my-project")
        ```
{% endcall %}

[Back to Project](./entity.md)
