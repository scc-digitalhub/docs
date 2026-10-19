---
render_macros: true
---

# Use an artifact

The common `Artifact` object methods apply across artifact kinds. They let you persist or refresh an entity and handle its files.

## Persist and refresh

These methods interact with the entity in the backend or locally.

{{ member_doc("update", "digitalhub.entities.artifact._base.entity.Artifact") }}

{{ member_doc("export", "digitalhub.entities.artifact._base.entity.Artifact") }}

{{ member_doc("refresh", "digitalhub.entities.artifact._base.entity.Artifact") }}

## File I/O

Use these methods to handle artifact files.

{{ member_doc("as_file", "digitalhub.entities.artifact._base.entity.Artifact") }}

{{ member_doc("download", "digitalhub.entities.artifact._base.entity.Artifact") }}

{{ member_doc("upload", "digitalhub.entities.artifact._base.entity.Artifact") }}

{{ member_doc("files", "digitalhub.entities.artifact._base.entity.Artifact") }}

{{ page_navigation(("Manage", "manage.md"), ("Entity", "entity.md")) }}
