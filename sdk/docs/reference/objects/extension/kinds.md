# Extension kinds

At the moment, we support the following kinds:

- **`extension`**: represents a generic extension

For each different kind, the `Extension` object has its own subclass with different `spec` and `status` attributes.

## Extension

The `extension` kind indicates that the extension is a generic extension. It's usefull if you intend to manipulate the extension as a file, you can in fact download/upload it.

### Extension spec parameters

| Parameter | Type | Description | Default |
| --- | --- | --- | --- |
| `schema` | *str* | The schema of the extension. | *required* |

### Extension methods

The `extension` kind has no additional methods.
