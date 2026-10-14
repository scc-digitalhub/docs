---
render_macros: true
---

# Secrets

Secrets store sensitive values such as external API or storage credentials through the configured secret provider. They can be managed as project-level entities, while secret values are handled separately from entity metadata.

The SDK currently supports Kubernetes Secret Manager. Each project stores its secret key-value pairs through its configured provider.

{{ entity_overview_cards("secret") }}

[Back to Entities](../index.md)
