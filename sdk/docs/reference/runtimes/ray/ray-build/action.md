---
render_macros: true
---

# Ray Build

Use the `build` action to create an execution image containing a Ray function and its dependencies.

## What the action does

The resulting image can be used to run the function on a Ray cluster.

{{ overview_cards([
    ("Create", "create.md", "Define the Ray application, handler and dependencies."),
    ("Run", "run.md", "Build the execution image and configure the build task."),
    ("Use", "use.md", "Retrieve the built image and build outputs."),
]) }}

{{ page_navigation(("Overview", "../overview.md")) }}
