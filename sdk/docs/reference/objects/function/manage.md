---
render_macros: true
---

# Manage functions

The methods below retrieve, import, update, or delete functions. They can be called directly from the SDK or through a `Project` object. When using a `Project` object, omit the `project` parameter and pass the other parameters as keyword arguments.

## Read

Use the read methods to retrieve functions from the backend or import them from a YAML descriptor.

{% call function_doc("get_function", "digitalhub.entities") %}
    === "Example"

        ```python
        import digitalhub as dh

        function = dh.get_function(
            identifier="my-function",
            project="my-project",
        )
        ```
{% endcall %}

{% call function_doc("get_function_versions", "digitalhub.entities") %}
    === "Example"

        ```python
        import digitalhub as dh

        functions = dh.get_function_versions(
            identifier="my-function",
            project="my-project",
        )
        ```
{% endcall %}

{% call function_doc("list_functions", "digitalhub.entities") %}
    === "Example"

        ```python
        import digitalhub as dh

        functions = dh.list_functions(project="my-project")
        ```
{% endcall %}

{% call function_doc("import_function", "digitalhub.entities") %}
    === "Example"

        ```python
        import digitalhub as dh

        function = dh.import_function("my-function.yaml")
        ```
{% endcall %}

## Update

Update a function after changing its mutable metadata.

{% call function_doc("update_function", "digitalhub.entities") %}
    === "Example"

        ```python
        import digitalhub as dh

        function = dh.get_function(
            identifier="my-function",
            project="my-project",
        )
        function.set_description("Updated function")
        function = dh.update_function(function)
        ```
{% endcall %}

## Delete

Delete one function version or all versions of a function.

{% call function_doc("delete_function", "digitalhub.entities") %}
    === "Example"

        ```python
        import digitalhub as dh

        dh.delete_function(
            identifier="my-function",
            project="my-project",
            delete_all_versions=True,
        )
        ```
{% endcall %}

[Back to Function](./entity.md)
