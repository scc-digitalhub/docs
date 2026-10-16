---
render_macros: true
---

# Artifact

The `artifact` kind represents a generic artifact stored as a file in an artifact store. Use it when you need to upload, download, or register files without additional kind-specific behavior.

The destination `path` and original `src_path` are documented with the creation functions. Use a [supported local or remote path](../../../configuration/paths.md#scheme-specific-paths) for the artifact destination.

## Create

### Log

{{ function_doc("log_artifact", "digitalhub.entities", separate_examples=True) }}

### Register

{{ function_doc("register_artifact", "digitalhub.entities", separate_examples=True) }}

### New

{{ function_doc("new_artifact", "digitalhub.entities", separate_examples=True) }}

## Methods

The `artifact` kind does not add instance methods. See [Use an artifact](../use.md) for the common methods.

[Back to artifact creation](../create.md)
