---
render_macros: true
---

# TVM runtime

Use Apache TVM to convert ONNX or TFLite models to Relax IR, compile them for a target architecture, and deploy the compiled `model.so` as a service.

{{ runtime_prerequisites("digitalhub-runtime-tvm") }}

Run the actions in order: **Build → Compile → Serve**. Configure the Function with
the source model and format. CORE updates its `ir_model` and `so_model` references
after successful runs; the next action uses them unless the Run sets `model_path`.

| Spec | Responsibility |
| --- | --- |
| Function | Source `model`, `format`; generated `ir_model` and `so_model` references |
| Task | Function reference and common resources, profiles, environment, secrets and volumes |
| Run | Per-execution TVM options; compile groups them under `optimization` and `tuning` |

Common Task settings can be overridden for one Run. TVM options from previous Runs
or old Tasks are not defaults for new Runs.
Compile CPU profiles come from CORE's `runtime-tvm.yaml`; advanced runs can provide
a standard LLVM target instead. The separate `profile` chooses where a Job or
service executes; it does not choose the generated Model's target.

TVM actions run on Kubernetes through CORE. Running a compiled model directly in
a local Go/Rust container is distinct from an SDK `local_execution` implementation.

{{ runtime_actions([
    ("Build", "tvm-build/action.md", "Convert an ONNX or TFLite model to Relax IR."),
    ("Compile", "tvm-compile/action.md", "Compile a Relax IR model to `model.so` for a target architecture."),
    ("Serve", "tvm-serve/action.md", "Deploy a compiled TVM model as a service."),
]) }}

{{ runtime_examples("Create, build, compile and serve a TVM model.") }}
