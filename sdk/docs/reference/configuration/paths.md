# Paths

The SDK supports several storage path schemes. Artifacts, Dataitems and Models use these paths to locate their data. Choose the scheme that matches where the data lives.

## Supported schemes

| Store | Schemes | Typical value |
| --- | --- | --- |
| Local | No scheme | `./dir/file.csv` |
| Remote | `http`, `https` | `https://example.com/data.csv` |
| Hugging Face | `hf` | `hf://owner/repository` |
| S3 | `s3` | `s3://bucket/key` |
| SQL | `sql` | `sql://database/schema/table` |

## Scheme-specific paths

=== "Local"

    Local paths point to files or directories that the runtime or build process can access.

    Format

    ``` bash
    ./relative/path/to/file
    /absolute/path/to/file
    ./relative/path/to/directory/
    /absolute/path/to/directory/
    ```

    Behavior

    No scheme is required. The SDK treats paths without a scheme as local.

=== "S3"

    S3 paths point to objects in S3 or S3-compatible storage.

    Format

    ``` bash
    s3://bucket/key
    s3://bucket/prefix/
    ```

    A trailing slash denotes a prefix or partition and is treated like a directory.

    Behavior

    The first path segment is the bucket; the remainder is the object key or prefix.

    ??? note "Access"

        Ensure the runtime has permission to read the bucket. See [S3 credentials](credentials.md#resource-credentials).

=== "Remote HTTP(S)"

    Remote paths point to files accessible over HTTP or HTTPS.

    Format

    ``` bash
    http://host/path/file
    https://host/path/file
    ```

    Behavior

    The SDK downloads HTTP(S) paths as files.

=== "Hugging Face"

    Hugging Face paths point to model repositories on the Hub. The SDK downloads the repository to a local directory when needed.

    Format

    ``` bash
    hf://owner/repository
    huggingface://owner/repository
    ```

    Behavior

    The destination must be a directory. Existing non-empty destinations are rejected unless overwrite is explicitly enabled.
    Downloads are supported; uploads and DataFrame reads or writes are not.
    Add `?revision=...` to select a branch, tag or commit.

    ??? note "Requirements"

        Install the optional dependency in the environment that performs the download:

        ```bash
        pip install "digitalhub[huggingface]"
        ```

        Private or gated repositories also require the credentials expected by `huggingface_hub`.

=== "SQL"

    SQL paths reference a single table in a configured database.

    Format

    ``` bash
    sql://database/schema/table (schema is optional)
    ```

    Behavior

    A SQL path always points to one table and requires at least a database and table name.

    ??? note "Access"

        Configure database connection parameters in the environment or runtime settings. See [SQL credentials](credentials.md#resource-credentials).
        SQL paths represent tables or queryable objects, not files.
