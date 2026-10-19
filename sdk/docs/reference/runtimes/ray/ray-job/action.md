---
render_macros: true
---

# Ray Job

Use the `job` action to execute a Ray function as a one-off job on a dynamically created Ray cluster.

## What the action does

The job's worker count and per-worker resources are configured with replicas, resource limits and profiles. The platform configures the Ray head node.

{{ overview_cards([
    ("Create", "create.md", "Define the Ray application, handler and dependencies."),
    ("Run", "run.md", "Configure cluster size and pass parameters to the application."),
    ("Use", "use.md", "Read results produced by the job."),
]) }}

{{ page_navigation(("Overview", "../overview.md")) }}
