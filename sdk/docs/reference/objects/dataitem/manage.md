---
render_macros: true
---

# Manage dataitems

The CRUD methods are used to read, update, and delete dataitems. They can be called through the SDK or through the `Project` object. When managing dataitems from a project, omit the `project` parameter and pass every other parameter as a keyword argument. For dataitem creation functions, see the [Create a dataitem guide](./create.md).

## Read

Use the read methods to retrieve dataitems from the backend or load them from a YAML descriptor.

{% call function_doc("get_dataitem", "digitalhub.entities") %}
    === "Example"

        ```python
        import digitalhub as dh

        dataitem = dh.get_dataitem(
            identifier="my-dataitem",
            project="my-project",
        )
        ```
{% endcall %}

{% call function_doc("get_dataitem_versions", "digitalhub.entities") %}
    === "Example"

        ```python
        import digitalhub as dh

        dataitems = dh.get_dataitem_versions(
            identifier="my-dataitem",
            project="my-project",
        )
        ```
{% endcall %}

{% call function_doc("list_dataitems", "digitalhub.entities") %}
    === "Example"

        ```python
        import digitalhub as dh

        dataitems = dh.list_dataitems(project="my-project")
        ```
{% endcall %}

{% call function_doc("import_dataitem", "digitalhub.entities") %}
    === "Example"

        ```python
        import digitalhub as dh

        dataitem = dh.import_dataitem("my-dataitem.yaml")
        ```
{% endcall %}

{% call function_doc("load_dataitem", "digitalhub.entities") %}
    === "Example"

        ```python
        import digitalhub as dh

        dataitem = dh.load_dataitem("my-dataitem.yaml")
        ```
{% endcall %}

## Update

Update a dataitem after changing its mutable metadata.

{% call function_doc("update_dataitem", "digitalhub.entities") %}
    === "Example"

        ```python
        import digitalhub as dh

        dataitem = dh.get_dataitem(
            identifier="my-dataitem",
            project="my-project",
        )
        dataitem.set_description("Updated dataitem")
        dataitem = dh.update_dataitem(dataitem)
        ```
{% endcall %}

## Delete

Delete one dataitem version or all versions of a dataitem.

{% call function_doc("delete_dataitem", "digitalhub.entities") %}
    === "Example"

        ```python
        import digitalhub as dh

        dh.delete_dataitem(
            identifier="my-dataitem",
            project="my-project",
            delete_all_versions=True,
        )
        ```
{% endcall %}
