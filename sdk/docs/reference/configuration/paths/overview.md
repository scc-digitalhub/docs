# Paths

The SDK supports a small set of storage path schemes. Put short: choose the scheme that matches where your files live and follow the scheme-specific rules below.

## Supported schemes

- [Local paths](local.md) — files available on the local filesystem.
- [S3 paths](s3.md) — S3 or S3-compatible object storage (bucket/key or prefix).
- [Remote paths](remote.md) — HTTP(S) resources (single files or archives).
- [SQL paths](sql.md) — database tables (Postgres-compatible).

## Entity paths

When creating an Artifact, Dataitem or Model you pass a `path` (a Python `str`) to indicate where the data or artifact lives. Rules:

- Local paths have no scheme (e.g. `./dir/file.csv`).
- Non-local paths must include a scheme (for example `s3://`, `http://`, `https://`, `sql://`).
- A path can reference a single file, a directory/prefix, a partition, or — for `sql://` — a single table. See each scheme page for precise formats and examples.
