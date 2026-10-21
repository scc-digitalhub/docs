---
render_macros: true
---

# Compile a TVM Model

Call `function.run(action="compile", ...)` with the target settings. The Run uses
`function.ir_model` unless you set `model_path` explicitly.

## Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| action | str | ✓ | Action to execute. Must be `compile`. |
| [volumes](../../../configuration/kubernetes.md#volumes) | list[dict] | | List of volumes. |
| [resources](../../../configuration/kubernetes.md#resources) | dict | | Resource values with optional `cpu`, `mem`, `gpu`, and `disk` keys. |
| [envs](../../../configuration/kubernetes.md#secrets-and-envs) | list[dict] | | Environment variables. |
| [secrets](../../../configuration/kubernetes.md#secrets-and-envs) | list[str] | | List of secret names. |
| [profile](../../../configuration/kubernetes.md#profile) | str | | Profile template. |
| model_path | str | | Optional IR override; otherwise uses `function.ir_model`. |
| target_architecture | str | | Profile from CORE's YAML catalogue; default `auto`. See [target architectures](action.md#target-architecture). |
| target | dict | | Explicit standard LLVM target; omit the profile or leave it at `auto`. |
| optimization | dict | | Compiler settings described below. |
| tuning | dict | | MetaSchedule settings described below; mode defaults to `off`. |
| tag | str | | Tag for the compiled model. |
| image | str | | TVM execution image. |
| inputs | dict[str, str] | | Mapping of input names to Dataitem or store keys. |

TVM options belong to the Run. Reusable Tasks contain only common infrastructure
settings, for example:

```python
task = function.new_task(action="compile", resources={"cpu": "4", "mem": "8Gi"})
```

## Example

```python
run = function.run(
    action="compile",
    target_architecture="amd64",
    optimization={"opt_level": 3},
    wait=True,
)
```

## Optimization settings

These fields go inside `optimization`. Flat keyword arguments are also accepted;
explicit grouped values take precedence.

| Field | Default | Meaning |
| --- | --- | --- |
| `target_num_cores` | Job CPU request | Threads used to optimize the target. |
| `opt_level` | `3` | TVM optimization level, 0–3. |
| `cross_cc` | profile default | C++ compiler linking `model.so`. |
| `cross_cc_options` | profile defaults | Separate compiler arguments; e.g. `["--sysroot=/opt/sysroots/arm64"]`. An explicit `[]` clears profile arguments. |
| `exec_mode` | `bytecode` | Relax VM `bytecode` or `compiled` graph execution. |
| `relax_pipeline`, `tir_pipeline` | `default` | Standard TVM pipeline names. |
| `benchmark_runs` | `10` | Timed inferences on a compatible compile host; `0` disables them. |
| `system_lib` | `false` | Static/system library mode; not supported by the serve images. |
| `params_path` | IR `params.bin` | Optional weights path inside the compile container. |

## Tuning settings

Use `tuning={"tuning_mode": "off"}` to compile without tuning. Inactive values are
preserved but not applied. `apply` needs `tuning_model_path`; `tune` needs a positive
`tuning_trials` budget. Databases must match the model, effective target and TVM build.

```python
run = function.run(
    "compile",
    target_architecture="amd64_native",
    optimization={"target_num_cores": 4},
    tuning={"tuning_mode": "tune", "tuning_trials": 8000, "tuning_runner": "local"},
    wait=True,
)
```

Further tuning fields:

- Search: `max_trials_per_task`, `tuning_trials_per_iter`, `tuning_workers`,
  `tuning_seed`, `tuning_ops`, `allow_partial_tuning`.
- Measurements: `tuning_number`, `tuning_repeat`, `tuning_min_repeat_ms`,
  `tuning_alloc_repeat`, `tuning_enable_cpu_cache_flush`.
- Timeouts: `tuning_builder_timeout_sec`, `tuning_runner_timeout_sec`.
- RPC: `rpc_tracker_host`, `rpc_tracker_port`, `rpc_tracker_key`,
  `rpc_session_timeout_sec`, with `tuning_runner="rpc"`.

Local tuning checks the actual compile host, not the presence of `cross_cc`.
For an incompatible target, measure on an RPC device or apply an existing database.

## Explicit target

```python
run = function.run(
    "compile",
    target={"kind": "llvm", "mtriple": "aarch64-linux-gnu", "mcpu": "cortex-a72"},
    optimization={"cross_cc": "aarch64-linux-gnu-g++"},
    wait=True,
)
```

The target uses standard TVM keys. The selected `image` must contain the matching
LLVM backend, compiler and libraries. Adding a target does not add a serving image,
and this pipeline does not enable GPU/CUDA execution.

{{ page_navigation(("Create", "create.md"), ("Use", "use.md")) }}
