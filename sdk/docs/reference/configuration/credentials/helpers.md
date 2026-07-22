# Credentials helpers

These helpers let you inspect and manage the active credentials profile used by the SDK.

## Get current profile

```python
import digitalhub as dh

profile = dh.get_current_profile()
```

::: digitalhub.get_current_profile
    options:
        heading_level: 3
        show_signature: true
        show_source: false
        show_root_heading: true
        show_symbol_type_heading: true
        show_root_full_path: false
        show_root_toc_entry: true

## Set current profile

```python
import digitalhub as dh

dh.set_current_profile("other-env")
```

::: digitalhub.set_current_profile
    options:
        heading_level: 3
        show_signature: true
        show_source: false
        show_root_heading: true
        show_symbol_type_heading: true
        show_root_full_path: false
        show_root_toc_entry: true

## Get credentials and config

```python
import digitalhub as dh

config = dh.get_credentials_and_config()
```

::: digitalhub.get_credentials_and_config
    options:
        heading_level: 3
        show_signature: true
        show_source: false
        show_root_heading: true
        show_symbol_type_heading: true
        show_root_full_path: false
        show_root_toc_entry: true

## Refresh token

Use this only if your profile uses OAuth2 credentials and you need a manual refresh.

```python
import digitalhub as dh

dh.refresh_token()
```

::: digitalhub.refresh_token
    options:
        heading_level: 3
        show_signature: true
        show_source: false
        show_root_heading: true
        show_symbol_type_heading: true
        show_root_full_path: false
        show_root_toc_entry: true
