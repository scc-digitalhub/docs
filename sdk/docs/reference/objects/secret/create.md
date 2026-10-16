---
render_macros: true
---

# Create a secret

Secrets are project-level entities. The `secret` kind stores values through the configured secret provider; values are managed separately from entity metadata.

## Choose a secret kind

The SDK provides one concrete secret kind.

{{ kind_cards([
    ("Secret", "./kind/secret.md", "Store a project secret through the configured secret provider", "secret"),
]) }}

{{ page_navigation(("Entity", "entity.md"), ("Manage", "manage.md")) }}
