---
render_macros: true
---

# Create a project

Use `new_project()` to create and save a project. Project configuration and setup options are documented in [Config](./config.md) and [Setup](./setup.md).

{% call function_doc("new_project", "digitalhub.entities") %}
    === "Creation example"

        ```python
        import digitalhub as dh

        project = dh.new_project(name="my-project")
        ```
{% endcall %}

## Get or create

Use `get_or_create_project()` to retrieve a project or create it when it does not exist.

{% call function_doc("get_or_create_project", "digitalhub.entities") %}
    === "Example"

        ```python
        import digitalhub as dh

        project = dh.get_or_create_project("my-project")
        ```
{% endcall %}

[Back to Project](./entity.md)
