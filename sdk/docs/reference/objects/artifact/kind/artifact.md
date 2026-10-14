---
render_macros: true
---

# Artifact

The `artifact` kind represents a generic artifact stored as a file in an artifact store. Use it when you need to upload, download, or register files without additional kind-specific behavior.

The destination `path` and original `src_path` are documented with the creation functions. Use a [supported local or remote path](../../../configuration/paths.md#scheme-specific-paths) for the artifact destination.

## Create

### Log

{% call function_doc("log_artifact", "digitalhub.entities") %}
    === "Creation example"

        ```python
        import digitalhub as dh

        artifact = dh.log_artifact(
            project="my-project",
            name="training-report",
            source="./outputs/training-report.json",
            src_path="outputs/training-report.json",
            labels=["training", "report"],
        )
        ```
{% endcall %}

### Register

{% call function_doc("register_artifact", "digitalhub.entities") %}
    === "Creation example"

        ```python
        import digitalhub as dh

        artifact = dh.register_artifact(
            project="my-project",
            name="registered-training-report",
            source="s3://my-bucket/reports/training-report.json",
            src_path="outputs/training-report.json",
        )
        ```
{% endcall %}

### New

{% call function_doc("new_artifact", "digitalhub.entities") %}
    === "Creation example"

        ```python
        import digitalhub as dh

        artifact = dh.new_artifact(
            project="my-project",
            name="my-artifact",
            kind="artifact",
            path="s3://my-bucket/my-artifact",
        )
        ```
{% endcall %}

## Methods

The `artifact` kind does not add instance methods. See [Use an artifact](../use.md) for the common methods.

[Back to artifact creation](../create.md)
