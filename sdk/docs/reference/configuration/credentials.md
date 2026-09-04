# Credentials

Credentials provide access to protected APIs, databases, cloud storage and Git repositories.
They can be supplied through environment variables or a `.dhcore.ini` configuration file.

## Common setup

The SDK checks environment variables first and falls back to the active profile in `.dhcore.ini`.
Git credentials are the exception: they are injected as environment variables and are not stored in `.dhcore.ini`.

=== "Environment variables"

    Set credentials in the shell or CI environment:

    ```bash
    export DHCORE_ENDPOINT=https://dhcore.example.com
    export AWS_ENDPOINT_URL=https://s3.example.com
    export DB_HOST=postgres.example.com
    ```

=== ".dhcore.ini"

    Place `.dhcore.ini` in the user home directory and select the active profile from `[DEFAULT]`:

    ```text
    [DEFAULT]
    current_environment = local

    [local]
    dhcore_endpoint = https://dhcore.example.com
    aws_endpoint_url = https://s3.example.com

    [production]
    dhcore_endpoint = https://dhcore.production.example.com
    aws_endpoint_url = https://s3.production.example.com
    ```

    The profile name is user defined. Use `dh.get_current_profile()` to inspect it and `dh.set_current_profile("production")` to change it.

## Resource credentials

=== "DHCore API"

    DHCore credentials authenticate requests to the DHCore backend.
    The configurator selects the first available flow in this order: PAT exchange, access and refresh tokens, access token only, then basic authentication.

    | Variable | Purpose |
    | --- | --- |
    | `DHCORE_ENDPOINT` | DHCore endpoint, including `https://` |
    | `DHCORE_ISSUER` | OpenID issuer for refresh or exchange flows |
    | `DHCORE_PERSONAL_ACCESS_TOKEN` | Personal access token |
    | `DHCORE_CLIENT_ID` | OAuth2 client id |
    | `DHCORE_ACCESS_TOKEN` | Bearer access token |
    | `DHCORE_REFRESH_TOKEN` | Refresh token |
    | `DHCORE_USER` | Username for basic authentication |
    | `DHCORE_PASSWORD` | Password for basic authentication |

    ??? example "Environment variables"

        ```bash
        export DHCORE_ENDPOINT=https://dhcore.example.com
        export DHCORE_ISSUER=https://auth.example.com

        # PAT authentication
        export DHCORE_PERSONAL_ACCESS_TOKEN=pat_...
        export DHCORE_CLIENT_ID=client-id

        # Access token and refresh token
        export DHCORE_ACCESS_TOKEN=eyJ...
        export DHCORE_REFRESH_TOKEN=...
        export DHCORE_CLIENT_ID=client-id

        # Access token only
        export DHCORE_ACCESS_TOKEN=eyJ...

        # Basic authentication
        export DHCORE_USER=myuser
        export DHCORE_PASSWORD=mypassword
        ```

    ??? example "Profile configuration"

        ```text
        [local]
        dhcore_endpoint = https://dhcore.example.com
        dhcore_issuer = https://auth.example.com
        dhcore_personal_access_token = pat_...
        dhcore_client_id = client-id
        ```

    If credentials are not available, log in interactively with the [DigitalHub CLI](https://scc-digitalhub.github.io/docs/components/cli/).

=== "S3 storage"

    S3 credentials configure access to S3-compatible object storage. The endpoint, access key id and secret access key are required.

    | Variable | Purpose |
    | --- | --- |
    | `AWS_ENDPOINT_URL` | S3 endpoint, including `https://` |
    | `AWS_ACCESS_KEY_ID` | Access key id |
    | `AWS_SECRET_ACCESS_KEY` | Secret access key |
    | `AWS_SESSION_TOKEN` | Optional session token |
    | `AWS_REGION` | Optional region |
    | `S3_SIGNATURE_VERSION` | Optional signature version |
    | `S3_PATH_STYLE` | Optional path-style addressing flag |
    | `AWS_CREDENTIALS_EXPIRATION` | Optional RFC3339 expiration timestamp |

    ??? example "Environment variables"

        ```bash
        export AWS_ENDPOINT_URL=https://s3.example.com
        export AWS_ACCESS_KEY_ID=access-key
        export AWS_SECRET_ACCESS_KEY=secret-key
        export AWS_SESSION_TOKEN=session-token
        export AWS_REGION=eu-west-1
        export S3_SIGNATURE_VERSION=s3v4
        export S3_PATH_STYLE=True
        ```

    ??? example "Profile configuration"

        ```text
        [local]
        aws_endpoint_url = https://s3.example.com
        aws_access_key_id = access-key
        aws_secret_access_key = secret-key
        aws_session_token = session-token
        aws_region = eu-west-1
        s3_signature_version = s3v4
        s3_path_style = True
        aws_credentials_expiration = 2025-08-26T12:00:00Z
        ```

    The SDK checks environment variables first, then falls back to `.dhcore.ini` and refreshes file-based credentials when applicable.

=== "SQL databases"

    SQL credentials configure the database used by SQL-backed stores. Username, password, host, port and database are required.

    | Variable | Purpose |
    | --- | --- |
    | `DB_HOST` | Database host or socket |
    | `DB_PORT` | Database port |
    | `DB_USERNAME` | Database user |
    | `DB_PASSWORD` | Database password |
    | `DB_DATABASE` | Database name |
    | `DB_PLATFORM` | Optional adapter hint, such as `postgres` or `mysql` |
    | `DB_SCHEMA` | Optional PostgreSQL schema |

    ??? example "Environment variables"

        ```bash
        export DB_HOST=postgres.example.com
        export DB_PORT=5432
        export DB_USERNAME=myuser
        export DB_PASSWORD=s3cr3t
        export DB_DATABASE=mydb
        export DB_PLATFORM=postgres
        export DB_SCHEMA=public
        ```

    ??? example "Profile configuration"

        ```text
        [local]
        db_host = postgres.example.com
        db_port = 5432
        db_username = myuser
        db_password = s3cr3t
        db_database = mydb
        db_platform = postgres
        db_schema = public
        ```

=== "Git repositories"

    Git credentials are used when the SDK fetches a private [Git code source](code-sources.md#code-source-uri).
    Tokens take precedence over username and password credentials.

    Credentials can be provided in the local process environment or through a DigitalHub Secret for managed executions.

    ??? example "Local environment"

        ```python
        import os

        os.environ["GIT_TOKEN"] = "ghp_..."
        os.environ["GIT_USER"] = "my-username"
        os.environ["GIT_PASSWORD"] = "my-password"
        ```

    ??? example "DigitalHub Secret"

        ```python
        import digitalhub as dh

        project = dh.get_or_create_project("my-project")
        project.new_secret(name="GIT_TOKEN", secret_value="ghp_...")
        project.new_secret(name="GIT_USER", secret_value="my-username")
        project.new_secret(name="GIT_PASSWORD", secret_value="my-password")

        func = dh.new_function(
            name="f",
            kind="python",
            code_src="git+https://github.com/my/repo",
            handler="src.app:run",
        )
        run = func.run(action="build", secrets=["GIT_TOKEN"])
        ```

## Helpers and clients

Credentials helpers

These helpers inspect and manage the active credentials profile.

??? example "Get current profile"

    ```python
    import digitalhub as dh

    profile = dh.get_current_profile()
    ```

??? example "Set current profile"

    ```python
    import digitalhub as dh

    dh.set_current_profile("production")
    ```

    ::: digitalhub.set_current_profile
        options:
            heading_level: 4
            show_signature: true
            show_source: false
            show_root_heading: true
            show_symbol_type_heading: true
            show_root_full_path: false
            show_root_toc_entry: true

??? example "Get credentials and config"

    ```python
    import digitalhub as dh

    config = dh.get_credentials_and_config()
    ```

??? example "Refresh token"

    Use this when an OAuth2 profile needs a manual refresh.

    ```python
    import digitalhub as dh

    dh.refresh_token()
    ```

Store clients

Recieve a client for the configured S3 or SQL store.

=== "S3 client"

    ```python
    import digitalhub as dh

    s3 = dh.get_s3_client()
    response = s3.list_buckets()
    ```

=== "SQL engine"

    ```python
    import digitalhub as dh

    engine = dh.get_sql_engine()
    ```
