---
render_macros: true
---

# Manage container images

The CRUD methods are used to read, update, and delete container images. They can be called directly from the SDK or through a `Project` object. When using a `Project` object, omit the `project` parameter and pass every other parameter as a keyword argument. For image creation, see [Create a container image](./create.md).

## Read

Use the read methods to retrieve container images from the backend or load them from a YAML descriptor.

{{ function_doc("get_containerimage", "digitalhub.entities", separate_examples=True) }}

{{ function_doc("get_containerimage_versions", "digitalhub.entities", separate_examples=True) }}

{{ function_doc("list_containerimages", "digitalhub.entities", separate_examples=True) }}

{{ function_doc("import_containerimage", "digitalhub.entities", separate_examples=True) }}

{{ function_doc("load_containerimage", "digitalhub.entities", separate_examples=True) }}

## Update

Update a container image after changing its mutable metadata.

{{ function_doc("update_containerimage", "digitalhub.entities", separate_examples=True) }}

## Delete

Delete one container image version or all versions of an image.

{{ function_doc("delete_containerimage", "digitalhub.entities", separate_examples=True) }}

{{ page_navigation(("Create", "create.md"), ("Use", "use.md")) }}
