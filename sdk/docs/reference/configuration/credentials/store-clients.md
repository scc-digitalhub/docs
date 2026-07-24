# Store clients

These helpers return ready-to-use clients for data stores based on the current credentials
profile.

## Prerequisites

Before using store clients, configure credentials for the target store:

- [S3 storage](./s3.md)
- [Databases](./sql.md)

If you use multiple profiles, set the active one with `dh.set_current_profile()`.

## S3 client

Use `get_s3_client()` to access a configured boto3 S3 client.

```python
import digitalhub as dh

s3 = dh.get_s3_client()
response = s3.list_buckets()
```

::: digitalhub.get_s3_client
    options:
        heading_level: 3
        show_signature: true
        show_source: false
        show_root_heading: true
        show_symbol_type_heading: true
        show_root_full_path: false
        show_root_toc_entry: true

## SQL engine

Use `get_sql_engine()` to create a SQLAlchemy engine connected to the configured database.
You can optionally pass a schema name.

```python
import digitalhub as dh

engine = dh.get_sql_engine(schema="public")
```

::: digitalhub.get_sql_engine
    options:
        heading_level: 3
        show_signature: true
        show_source: false
        show_root_heading: true
        show_symbol_type_heading: true
        show_root_full_path: false
        show_root_toc_entry: true
