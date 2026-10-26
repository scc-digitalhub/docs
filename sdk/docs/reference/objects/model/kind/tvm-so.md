---
render_macros: true
---

# TVM SO

The `tvm-so` kind stores a compiled TVM shared-object model. Kind-specific fields, including target, optimization level, manifest, and tensor signatures, are documented with the creation functions.

The bundle contains `model.so` **and** `metadata.json`. Normally a compile Run
creates it. For manual registration, retain the full metadata, including TVM
version/commit and target: serving requires it. `spec.manifest` contains this
metadata; it is distinct from `tuning/manifest.json`.

## Create

### Log

{{ function_doc("log_tvm_so", "digitalhub_runtime_tvm.entities.model.tvm_so.crud", separate_examples=True) }}

### Register

{{ function_doc("register_tvm_so", "digitalhub_runtime_tvm.entities.model.tvm_so.crud", separate_examples=True) }}

### New

Create a Model reference to an already uploaded bundle; this call does not compile
or upload files.

{% call function_doc("new_model", "digitalhub.entities") %}
    === "Creation example"

        ```python
        import json
        from pathlib import Path
        import digitalhub as dh

        metadata = json.loads(Path("compiled-model/metadata.json").read_text())

        model = dh.new_model(
            project="my-project",
            name="resnet18-tvm",
            kind="tvm-so",
            path="s3://my-bucket/models/resnet18-so/",
            target=metadata["target"],
            opt_level=metadata["opt_level"],
            entry=metadata["entry"],
            inputs=metadata["inputs"],
            outputs=metadata["outputs"],
            manifest=metadata,
        )
        ```
{% endcall %}

## Retrieve and manage

Use the shared [Model management reference](../manage.md) to retrieve, update, or delete a TVM SO Model.

## Related runtime

See the [TVM runtime](../../../runtimes/tvm/overview.md), including its [compile](../../../runtimes/tvm/tvm-compile/action.md) and [serve](../../../runtimes/tvm/tvm-serve/action.md) workflows.
