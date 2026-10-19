---
render_macros: true
---

# Hydra Build

Use the `build` action to create an execution image containing the Hydra function and its dependencies.

## What the action does

The resulting image can be used to execute the function remotely without reinstalling its requirements for each job.

{{ overview_cards([
    ("Create", "create.md", "Define the Hydra application, configuration and dependencies."),
    ("Run", "run.md", "Build the execution image and configure the build task."),
    ("Use", "use.md", "Retrieve the built image and build outputs."),
]) }}

{{ page_navigation(("Overview", "../overview.md")) }}
