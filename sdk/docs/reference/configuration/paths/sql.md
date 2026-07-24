# SQL paths

SQL paths reference a single table in a database and are used where the SDK integrates with SQL-backed storage.

## Format

- `sql://database/schema/table` (schema is optional)

## Behavior

- A SQL path always points to a single table. The SDK expects at least database and table names.

## Example

```python
sql_path = "sql://my-database/my-schema/my-table"
```

## Notes

- Ensure database connection parameters are configured in the environment or runtime settings. Check [S3 credentials handling](../credentials/sql.md).
- SQL paths are not files; they represent a table or queryable object in the configured DB.
