---
render_macros: true
---

# Secret

The `secret` kind stores a project-level sensitive value through the configured secret provider. Secret values are managed separately from entity metadata.

## Secret spec

| Parameter | Type | Description | Default |
| --- | --- | --- | --- |
| `path` | *str \| None* | Path to the secret. | `None` |
| `provider` | *str \| None* | Secret provider. | `None` |

## Create

### New

{{ function_doc("new_secret", "digitalhub.entities", separate_examples=True) }}

## Methods

Secret values and common entity methods are documented in [Use a secret](../use.md).

[Back to secret kind selection](../create.md)
