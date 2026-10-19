---
render_macros: true
---

# TVM Compile

Use the `compile` action to compile a Relax IR model for a target architecture and produce a deployable `model.so`.

## What the action does

Select a target CPU profile and optional compiler and TVM pipeline settings to produce the compiled artifact.

## Target architecture

Supported targets include `auto`, `amd64`, `amd64_v3`, `amd64_native`, `arm64`, `arm64_pi5`, and `arm32`. `auto` uses the compile node's architecture. Older aliases `cpu`/`llvm`, `x86`, `x86_v3`, `x86_native`, and `armv7l` map to `auto`, `amd64`, `amd64_v3`, `amd64_native`, and `arm32`.

{{ overview_cards([
    ("Create", "create.md", "Use the TVM Function created for the build action."),
    ("Run", "run.md", "Compile Relax IR and configure the target architecture."),
    ("Use", "use.md", "Pass the compiled model artifact to the serve action."),
]) }}

{{ page_navigation(("Overview", "../overview.md")) }}
