---
render_macros: true
---

# TVM Build

Use the `build` action to convert an ONNX or TFLite source model into Relax IR.

## What the action does

CORE records the resulting Relax IR artifact in the Function's `ir_model` field.
The `compile` action uses it automatically; set its Run's `model_path` only to
choose a different IR artifact. Conversion options belong to the Run, not the Task.

{{ overview_cards([
    ("Create", "create.md", "Configure the source model and artifact store keys."),
    ("Run", "run.md", "Convert the model and configure build options."),
    ("Use", "use.md", "Pass the Relax IR artifact to the compile action."),
]) }}

{{ page_navigation(("Overview", "../overview.md")) }}
