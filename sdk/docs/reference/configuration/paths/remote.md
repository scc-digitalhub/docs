# Remote paths (HTTP/S)

Remote paths point to files accessible over HTTP or HTTPS.

## Format

- `http://host/path/file` or `https://host/path/file`

## Behavior

- The SDK treats HTTP(S) paths as remote resources and downloads them as files.

## Examples

```python
http_path = "https://example.com/data.csv"
```

For HTTP(S) code archives, use the `zip+http://` or `zip+https://` form in `code_src`; see [HTTP(S) code sources](../code_src/http.md).
