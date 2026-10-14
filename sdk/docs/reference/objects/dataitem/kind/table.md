---
render_macros: true
---

# Table

The `table` kind represents tabular data that can be read and written as a dataframe. The default dataframe engine is `pandas`; `polars` is also supported. Install the optional SDK extra for the engine you use, as described in the [SDK installation guide](../../../../how-to/installation.md).

The `path` identifies the table data and can use a supported [local or remote scheme](../../../configuration/paths.md#scheme-specific-paths). `log_table()` generates a destination path when one is not supplied. An optional `schema` follows the [Frictionless Table Schema](https://specs.frictionlessdata.io/table-schema/) format; `log_table()` infers it from the data when omitted.

## Create

### Log

{% call function_doc("log_table", "digitalhub.entities") %}
    === "Creation example"

        ```python
        import digitalhub as dh
        import pandas as pd

        table_from_source = dh.log_table(
            project="my-project",
            name="sales-from-file",
            source="./data/sales.csv",
            file_format="csv",
        )

        table_from_data = dh.log_table(
            project="my-project",
            name="sales-from-dataframe",
            data=pd.DataFrame(
                {
                    "customer_id": [101, 102],
                    "amount": [12.50, 8.75],
                }
            ),
        )
        ```
{% endcall %}

### Register

{% call function_doc("register_table", "digitalhub.entities") %}
    === "Creation example"

        ```python
        import digitalhub as dh

        dataitem = dh.register_table(
            project="my-project",
            name="registered-sales",
            source="s3://my-bucket/data/sales.parquet",
            schema={
                "fields": [
                    {"name": "customer_id", "type": "integer"},
                    {"name": "amount", "type": "float"},
                ]
            },
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
            name="sales",
            kind="table",
            path="s3://my-bucket/data/sales.parquet",
        )
        ```
{% endcall %}

## Methods

The `table` kind adds dataframe operations to the [common Dataitem methods](../use.md).

{{ member_doc("as_df", "digitalhub.entities.dataitem.table.entity.DataitemTable") }}

{{ member_doc("write_df", "digitalhub.entities.dataitem.table.entity.DataitemTable") }}

[Back to dataitem kind selection](../create.md)
