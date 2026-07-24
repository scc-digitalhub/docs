# Remote paths (HTTP/S)

Remote paths point to resources accessible over HTTP or HTTPS. They are useful for single files or archives hosted on the web.

## Format

- `http://host/path/file` or `https://host/path/file`

## Behavior

- The SDK treats HTTP(S) paths as remote resources; behavior (single file vs archive) depends on the consumer.

## Examples

```python
http_path = "https://example.com/data.csv"
zip_http = "zip+https://example.com/code_bundle.zip"
```
