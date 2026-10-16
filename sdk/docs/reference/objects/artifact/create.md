---
render_macros: true
---

# Create an artifact

Choose the creation method based on where the artifact source is and whether you want to upload it.

## Choose a creation method

- **Log with `log_artifact()`** creates an artifact from a local source and uploads its files to an artifact store.
- **Register with `register_artifact()`** creates an artifact entity for a source that already exists in a store.
- **Create with `new_artifact()`** creates an entity from an explicit kind and path without uploading a source. Its example is in the Artifact kind reference below.

Artifact creation functions are provided by the SDK and do not require an additional runtime package.

## Choose an artifact kind

The `artifact` kind stores a generic artifact as a file in an artifact store.

{{ kind_cards([
    ("Artifact", "./kind/artifact.md", "Store a generic artifact as a file in an artifact store", "artifact"),
]) }}

{{ page_navigation(("Entity", "entity.md"), ("Manage", "manage.md")) }}
