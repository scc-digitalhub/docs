---
render_macros: true
---

# Manage an artifact

The CRUD methods are used to read, update, and delete artifacts. They can be called through the SDK or through the `Project` object. When managing artifacts from a project, omit the `project` parameter and pass every other parameter as a keyword argument. For artifact creation functions, see the [Create an artifact guide](./create.md).

## Read

Use the read methods to retrieve artifacts from the backend or load them from a YAML descriptor.

{% call function_doc("get_artifact", "digitalhub.entities") %}
    === "Example"

        ```python
        import digitalhub as dh

        artifact = dh.get_artifact(
            identifier="my-artifact",
            project="my-project",
        )
        ```
{% endcall %}

{% call function_doc("get_artifact_versions", "digitalhub.entities") %}
    === "Example"

        ```python
        import digitalhub as dh

        artifacts = dh.get_artifact_versions(
            identifier="my-artifact",
            project="my-project",
        )
        ```
{% endcall %}

{% call function_doc("list_artifacts", "digitalhub.entities") %}
    === "Example"

        ```python
        import digitalhub as dh

        artifacts = dh.list_artifacts(project="my-project")
        ```
{% endcall %}

{% call function_doc("import_artifact", "digitalhub.entities") %}
    === "Example"

        ```python
        import digitalhub as dh

        artifact = dh.import_artifact("my-artifact.yaml")
        ```
{% endcall %}

{% call function_doc("load_artifact", "digitalhub.entities") %}
    === "Example"

        ```python
        import digitalhub as dh

        artifact = dh.load_artifact("my-artifact.yaml")
        ```
{% endcall %}

## Update

Update an artifact after changing its mutable metadata.

{% call function_doc("update_artifact", "digitalhub.entities") %}
    === "Example"

        ```python
        import digitalhub as dh

        artifact = dh.get_artifact(
            identifier="my-artifact",
            project="my-project",
        )
        artifact.set_description("Updated artifact")
        artifact = dh.update_artifact(artifact)
        ```
{% endcall %}

## Delete

Delete one artifact version or all versions of an artifact.

{% call function_doc("delete_artifact", "digitalhub.entities") %}
    === "Example"

        ```python
        import digitalhub as dh

        dh.delete_artifact(
            identifier="my-artifact",
            project="my-project",
            delete_all_versions=True,
        )
        ```
{% endcall %}
