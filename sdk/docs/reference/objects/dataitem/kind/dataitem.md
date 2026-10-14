---
render_macros: true
---

# Dataitem

The `dataitem` kind stores a generic dataset in an addressable repository. Use it when you need to manage data without the additional behavior of a specialized kind.

When creating a dataitem with `new_dataitem()`, provide a `path` to its data. For source-based creation, `log_dataitem()` uses `path` as the destination and generates it when omitted. Paths can use the supported [local or remote schemes](../../../configuration/paths.md#scheme-specific-paths).

## Create

### Log

{% call function_doc("log_dataitem", "digitalhub.entities") %}
    === "Creation example"

        ```python
        import digitalhub as dh

        dataitem = dh.log_dataitem(
            project="my-project",
            name="raw-events",
            source="./data/events.jsonl",
            labels=["raw", "events"],
        )
        ```
{% endcall %}

### Register

{% call function_doc("register_dataitem", "digitalhub.entities") %}
    === "Creation example"

        ```python
        import digitalhub as dh

        dataitem = dh.register_dataitem(
            project="my-project",
            name="registered-events",
            source="s3://my-bucket/data/events.jsonl",
        )
        ```
{% endcall %}

### New

{% call function_doc("new_dataitem", "digitalhub.entities") %}
    === "Creation example"

        ```python
        import digitalhub as dh

        dataitem = dh.new_dataitem(
            project="my-project",
            name="raw-events",
            kind="dataitem",
            path="s3://my-bucket/data/events.jsonl",
        )
        ```
{% endcall %}

## Methods

The generic `dataitem` kind adds no instance methods. See [Use a dataitem](../use.md) for the common methods.

[Back to dataitem kind selection](../create.md)
