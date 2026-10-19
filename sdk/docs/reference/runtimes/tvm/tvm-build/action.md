---
render_macros: true
---

# TVM Build

Use the `build` action to convert an ONNX or TFLite source model into Relax IR.

## What the action does

The resulting Relax IR artifact can be passed to the `compile` action as `model_path` or referenced through the Function's `ir_model` field.

{{ overview_cards([
    ("Create", "create.md", "Configure the source model and artifact store keys."),
    ("Run", "run.md", "Convert the model and configure build options."),
    ("Use", "use.md", "Pass the Relax IR artifact to the compile action."),
]) }}

{{ page_navigation(("Overview", "../overview.md")) }}
