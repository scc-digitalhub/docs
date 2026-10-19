---
render_macros: true
---

# Container Job

Use the `job` action to run a container to completion; the container terminates when the command finishes.

## What the action does

The job action executes the configured container image as a one-off workload on Kubernetes.

{{ overview_cards([
    ("Create", "create.md", "Configure the Function with the container image and command."),
    ("Run", "run.md", "Execute the container as a one-off job."),
    ("Use", "use.md", "Work with the completed job Run."),
]) }}

{{ page_navigation(("Overview", "../overview.md")) }}
