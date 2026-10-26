---
render_macros: true
---

# Serve a TVM Model

Call `function.run(action="serve", ...)` with the service settings. The Run uses
`function.so_model` unless you set `model_path` explicitly.

## Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| action | str | ✓ | Action to execute. Must be `serve`. |
| [volumes](../../../configuration/kubernetes.md#volumes) | list[dict] | | List of volumes. |
| [resources](../../../configuration/kubernetes.md#resources) | dict | | Resource values with optional `cpu`, `mem`, `gpu`, and `disk` keys. |
| [envs](../../../configuration/kubernetes.md#secrets-and-envs) | list[dict] | | Environment variables. |
| [secrets](../../../configuration/kubernetes.md#secrets-and-envs) | list[str] | | List of secret names. |
| [profile](../../../configuration/kubernetes.md#profile) | str | | Scheduling/resource profile; does not select the model target. |
| model_path | str | | Optional `store://` reference to a `tvm-so` Model; otherwise uses `function.so_model`. |
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

The selected Model is pinned in this Run. Compiling another target does not change
a running service; use a versioned `model_path` to select an earlier build.
`profile` must select a node compatible with the Model's architecture and CPU.

## Example

```python
run = function.run(
    action="serve",
    served_name="my-model",
    replicas=1,
    wait=True,
)
```

{{ page_navigation(("Create", "create.md"), ("Use", "use.md")) }}
