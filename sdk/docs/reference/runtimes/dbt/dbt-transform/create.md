---
render_macros: true
---

# Create a DBT Function

Define the Function with dbt SQL or a source reference. Use the `dh.new_function()` method to create it.

## Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| project | str | (✓) | Project name. **Required when calling `dh.new_function()` directly. Forbidden when using project.** |
| name | str | ✓ | Name that identifies the object. |
| kind | str | ✓ | Function kind. Must be `dbt` |
| uuid | str | | Object ID in UUID4 format. |
| description | str | | Description of the object. |
| labels | list[str] | | List of labels. |
| embedded | bool | | Whether the object should be embedded in the project. |
| [code_src](../../../configuration/code-sources.md#code-source-uri) | str | | URI pointing to the source code. |
| [code](../../../configuration/code-sources.md#plain-text-source) | str | | SQL source provided as plain text. |
| base64 | str | | SQL source encoded as base64. |
| [handler](../../../configuration/code-sources.md#handler) | str | | Source file path used with repository or archive sources. |
| lang | str | | Source language hint. Defaults to `sql`; dbt transformations use SQL. |

## Example

```python
import digitalhub as dh

function = dh.new_function(
    project="my-project",
    name="my-function",
    kind="dbt",
    code="SELECT * FROM {% raw %}{{ ref('my_table_ref') }}{% endraw %}"
)
```

{{ page_navigation(("Action", "action.md"), ("Run", "run.md")) }}
