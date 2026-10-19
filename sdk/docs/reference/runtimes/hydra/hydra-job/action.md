---
render_macros: true
---

# Hydra Job

Use the `job` action to execute a Hydra function as a one-off multirun job on the platform.

## What the action does

The runtime passes run parameters to Hydra as configuration overrides. A job supports Hydra handlers that run to completion.

{{ overview_cards([
    ("Create", "create.md", "Define the Hydra application, configuration and dependencies."),
    ("Run", "run.md", "Configure Hydra overrides, workers and execution mode."),
    ("Use", "use.md", "Read results produced by the job."),
]) }}

{{ page_navigation(("Overview", "../overview.md")) }}
