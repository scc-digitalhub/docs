# Examples

```python
import digitalhub as dh

project = dh.get_or_create_project("my_project")

sql = """
SELECT * FROM {{ ref("my_table_ref") }}
"""

dataitem = project.new_dataitem("my_dataitem", kind="table", path="path-to-some-data")

function = dh.new_function(
    kind="dbt",
    name="my_function",
    code=sql
)

run = function.run(
    action="transform",
    inputs={
        "my_table_ref": dataitem.key
    },
    outputs={
        "output_table": "mapped-name"
    }
)
```

## Tutorials

Find additional examples in the [tutorial repository](https://github.com/scc-digitalhub/digitalhub-tutorials) of the DSLab GitHub organization.
