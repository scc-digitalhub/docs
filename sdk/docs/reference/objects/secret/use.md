---
render_macros: true
---

# Use a secret

The common `Secret` methods let you persist or refresh a secret entity and manage its sensitive value through the configured provider.

## Persist and refresh

{{ member_doc("update", "digitalhub.entities.secret._base.entity.Secret") }}

{{ member_doc("export", "digitalhub.entities.secret._base.entity.Secret") }}

{{ member_doc("refresh", "digitalhub.entities.secret._base.entity.Secret") }}

## Manage secret values

Secret values are separate from the entity metadata.

{{ member_doc("set_secret_value", "digitalhub.entities.secret._base.entity.Secret") }}

{{ member_doc("read_secret_value", "digitalhub.entities.secret._base.entity.Secret") }}

{{ page_navigation(("Manage", "manage.md"), ("Entity", "entity.md")) }}
