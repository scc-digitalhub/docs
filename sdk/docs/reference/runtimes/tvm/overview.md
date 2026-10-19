---
render_macros: true
---

# TVM runtime

Use Apache TVM to convert ONNX or TFLite models to Relax IR, compile them for a target architecture, and deploy the compiled `model.so` as a service.

{{ runtime_prerequisites("digitalhub-runtime-tvm") }}

Run the actions in order: **Build → Compile → Serve**. Configure the Function with the source model and format; use `ir_model` and `so_model` store keys to pass artifacts between actions.

{{ runtime_actions([
    ("Build", "tvm-build/action.md", "Convert an ONNX or TFLite model to Relax IR."),
    ("Compile", "tvm-compile/action.md", "Compile a Relax IR model to `model.so` for a target architecture."),
    ("Serve", "tvm-serve/action.md", "Deploy a compiled TVM model as a service."),
]) }}

{{ runtime_examples("Create, build, compile and serve a TVM model.") }}
