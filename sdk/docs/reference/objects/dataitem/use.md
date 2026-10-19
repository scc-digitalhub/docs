---
render_macros: true
---

# Use a dataitem

The common `Dataitem` object methods apply across dataitem kinds. They let you persist or refresh an entity and handle its files.

## Persist and refresh

These methods interact with the entity in the backend or locally.

{{ member_doc("update", "digitalhub.entities.dataitem._base.entity.Dataitem") }}

{{ member_doc("export", "digitalhub.entities.dataitem._base.entity.Dataitem") }}

{{ member_doc("refresh", "digitalhub.entities.dataitem._base.entity.Dataitem") }}

## File I/O

Use these methods to handle dataitem files.

{{ member_doc("as_file", "digitalhub.entities.dataitem._base.entity.Dataitem") }}

{{ member_doc("download", "digitalhub.entities.dataitem._base.entity.Dataitem") }}

{{ member_doc("upload", "digitalhub.entities.dataitem._base.entity.Dataitem") }}

## Kind-specific methods

The `table` and `croissant` kinds add methods for working with their data. See the [dataitem kind references](./create.md#choose-a-dataitem-kind).

{{ page_navigation(("Manage", "manage.md"), ("Entity", "entity.md")) }}
