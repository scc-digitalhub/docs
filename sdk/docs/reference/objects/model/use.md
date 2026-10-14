---
render_macros: true
---

# Use a model

The common `Model` object methods apply across model kinds. They let you persist or refresh an entity, handle its files, and log metrics.

## Persist and refresh

These methods interact with the entity in the backend or locally.

{{ member_doc("save", "digitalhub.entities.model._base.entity.Model") }}

{{ member_doc("update", "digitalhub.entities.model._base.entity.Model") }}

{{ member_doc("export", "digitalhub.entities.model._base.entity.Model") }}

{{ member_doc("refresh", "digitalhub.entities.model._base.entity.Model") }}

## File I/O

Use these methods to handle model files.

{{ member_doc("as_file", "digitalhub.entities.model._base.entity.Model") }}

{{ member_doc("download", "digitalhub.entities.model._base.entity.Model") }}

{{ member_doc("upload", "digitalhub.entities.model._base.entity.Model") }}

{{ member_doc("files", "digitalhub.entities.model._base.entity.Model") }}

## Metrics

The common `Model` object can record one or more metrics and exposes them through its `metrics` property.

{{ member_doc("metrics", "digitalhub.entities.model._base.entity.Model") }}

{{ member_doc("log_metric", "digitalhub.entities.model._base.entity.Model") }}

{{ member_doc("log_metrics", "digitalhub.entities.model._base.entity.Model") }}

## Kind-specific APIs and runtime workflows

Runtime-specific model classes only define their constructors and kind-specific data; they do not add instance methods beyond the common `Model` interface documented above. Kind-specific `log_*()` and `register_*()` APIs are functions, not `Model` methods; see the [kind pages](create.md).

Serving is a separate runtime workflow that uses a runtime `Function`, not a `Model` method. See the [ModelServe runtime](../../runtimes/modelserve/overview.md) or the [TVM runtime](../../runtimes/tvm/overview.md).
