---
render_macros: true
---

# Manage functions

The methods below retrieve, import, update, or delete functions. They can be called directly from the SDK or through a `Project` object. When using a `Project` object, omit the `project` parameter and pass the other parameters as keyword arguments.

## Read

Use the read methods to retrieve functions from the backend or import them from a YAML descriptor.

{{ function_doc("get_function", "digitalhub.entities", separate_examples=True) }}

{{ function_doc("get_function_versions", "digitalhub.entities", separate_examples=True) }}

{{ function_doc("list_functions", "digitalhub.entities", separate_examples=True) }}

{{ function_doc("import_function", "digitalhub.entities", separate_examples=True) }}

## Update

Update a function after changing its mutable metadata.

{{ function_doc("update_function", "digitalhub.entities", separate_examples=True) }}

## Delete

Delete one function version or all versions of a function.

{{ function_doc("delete_function", "digitalhub.entities", separate_examples=True) }}

{{ page_navigation(("Create", "create.md"), ("Use", "use.md")) }}
