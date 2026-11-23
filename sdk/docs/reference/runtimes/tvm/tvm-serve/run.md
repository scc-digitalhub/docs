---
render_macros: true
---

# Serve a TVM Model

Call `function.run(action="serve", ...)` with the service settings and the required
`so_model_path`. Use the versioned Model key from the chosen Compile Run's
`status.outputs.compiled_so`.

## Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| action | str | ✓ | Action to execute. Must be `serve`. |
| [volumes](../../../configuration/kubernetes.md#volumes) | list[dict] | | List of volumes. |
| [resources](../../../configuration/kubernetes.md#resources) | dict | | Resource values with optional `cpu`, `mem`, `gpu`, and `disk` keys. |
| [envs](../../../configuration/kubernetes.md#secrets-and-envs) | list[dict] | | Environment variables. |
| [secrets](../../../configuration/kubernetes.md#secrets-and-envs) | list[str] | | List of secret names. |
| [profile](../../../configuration/kubernetes.md#profile) | str | | Scheduling/resource profile; does not select the model target. |
| so_model_path | str | ✓ | Versioned `store://.../model/tvm-so/<name>:<id>` key from the chosen Compile Run's `status.outputs.compiled_so`. |
| served_name | str | | Model name in `/v2/models/<name>`; defaults to the Function name. |
| image | str | | Go image by default; set the Rust image to use Rust for this Run. |
| replicas | int | | Number of pods, zero or greater; default `1`. |
| workers | int | | Parallel model copies per pod, at least one; default `1`. |
| [service_type](../../../configuration/kubernetes.md#service-port-and-type) | str | | `ClusterIP` (default), `NodePort` or `LoadBalancer`. |
| service_name | str | | Extra Kubernetes service name, `<function>-<service_name>`; distinct from `served_name`. |

Serving options belong to the Run. Reusable Tasks contain only common infrastructure
settings, for example:

```python
task = function.new_task(action="serve", resources={"cpu": "2", "mem": "2Gi"})
```

The selected Model is saved in this Run. Compiling another target does not change
its selection. Every new Serve Run needs `so_model_path`, including when reusing an
older compiled Model. If old Function data contains `so_model`, Serve ignores it.
`profile` must select a node compatible with the Model's architecture and CPU.
For a CUDA artifact, also select a CUDA-enabled runtime image and provide the
existing `resources={"gpu": "1"}`/GPU profile settings. The backend comes from Model
metadata; there is no new device option and no CPU fallback. A GPU profile does not
change the selected Model. See the
[CUDA guide](https://scc-digitalhub.github.io/docs/0.16/runtimes/tvm/#serve-on-a-gpu-node).

These parameters configure the service; inference tensors are sent directly to its
REST or gRPC endpoint. Request validation is implemented by the Go/Rust serving
image and does not require new SDK parameters. Go `0.26.0-r3` and Rust `0.26.0-r2`
include these checks. Set `image` to the desired version if the platform default
still uses an older runtime. See the
[input validation guide](https://scc-digitalhub.github.io/docs/0.16/runtimes/tvm/#input-validation).

## Example

```python
run = function.run(
    action="serve",
    so_model_path="store://my-project/model/tvm-so/my-model:<compiled-model-id>",
    served_name="my-model",
    replicas=1,
    wait=True,
)
```

{{ page_navigation(("Create", "create.md"), ("Use", "use.md")) }}
