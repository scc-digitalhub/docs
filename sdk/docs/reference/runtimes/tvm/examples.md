---
render_macros: true
---

# Examples

```python
import digitalhub as dh

project = dh.get_or_create_project("my_project")

function = project.new_function(
    name="mobilenet",
    kind="tvm",
    model="s3://my-bucket/models/mobilenet.onnx",
    format="onnx",
)

build = function.run(
    action="build",
    wait=True,
)

compile = function.run(
    action="compile",
    target_architecture="auto",
    optimization={"opt_level": 3},
    wait=True,
)

serve = function.run(
    action="serve",
    served_name="mobilenet",
    replicas=1,
    wait=True,
)
```

CORE updates the function's `ir_model` and `so_model` after successful runs. The next
action uses those references unless you explicitly set `model_path`.
TVM options belong to the Run; Task settings cover resources, profiles and volumes.

## Explicit CPU target

Profile names come from CORE's `runtime-tvm.yaml`. Instead of selecting a profile,
an advanced run can provide the target directly:

```python
compile = function.run(
    "compile",
    target={"kind": "llvm", "mtriple": "aarch64-linux-gnu", "mcpu": "cortex-a72"},
    optimization={"cross_cc": "aarch64-linux-gnu-g++"},
    wait=True,
)
```

The compiler must exist in the selected compile image. See the
[compile reference](tvm-compile/run.md) for tuning and toolchain options.

## Tutorials

Find additional examples in the [tutorial repository](https://github.com/scc-digitalhub/digitalhub-tutorials) of the DSLab GitHub organization.

{{ page_navigation(("Overview", "overview.md")) }}
