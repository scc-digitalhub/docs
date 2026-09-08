# Examples

```python
import digitalhub as dh

project = dh.get_or_create_project("my_project")

ir_model = "store://my_project/model/mobilenet-relax:version"
so_model = "store://my_project/model/mobilenet-so:version"

function = project.new_function(
    name="mobilenet",
    kind="tvm",
    model="s3://my-bucket/models/mobilenet.onnx",
    format="onnx",
)

build = function.run(
    action="build",
    ir_model=ir_model,
    wait=True,
)

compile = function.run(
    action="compile",
    model_path=ir_model,
    ir_model=ir_model,
    so_model=so_model,
    target_architecture="llvm",
    opt_level=3,
    wait=True,
)

serve = function.run(
    action="serve",
    model_path=so_model,
    ir_model=ir_model,
    so_model=so_model,
    served_name="mobilenet",
    replicas=1,
    wait=True,
)
```

## Tutorials

Find additional examples in the [tutorial repository](https://github.com/scc-digitalhub/digitalhub-tutorials) of the DSLab GitHub organization.
