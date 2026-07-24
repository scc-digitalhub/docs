# Local paths

Local paths point to files or directories on the local filesystem. Use them when the runtime or build process can access the same files.

## Format

- `./relative/path/to/file` or `/absolute/path/to/file`

## Behavior

- No scheme is required. The SDK treats paths without a scheme as local.
- Local paths may point to single files or to directories; behavior depends on the consuming entity (Artifact, Dataitem, Model).

## Examples

```python
local_dir = "./my-path"
local_file = "./my-path/my-file.csv"
```
