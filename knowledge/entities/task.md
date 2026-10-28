---
title: Task Entity
description: Intermediary binding between a Function/Workflow and an execution action (build, job, serve, pipeline) auto-managed by dhcli run.
---

# Task Entity (`<kind>+<action>`)

A **Task** is the intermediary entity that binds a specific `Function` or `Workflow` version to an execution action (such as `python+build`, `python+job`, `python+serve`, `container+serve`, or `hera+pipeline`) along with default Kubernetes resource and environment settings.

- **Task reference URI**: `<task-kind>://<project>/<task-uuid>` (e.g., `python+job://my-project/9d249ef7762349e2a532e883ac4c378e`)

## How `dhcli` Manages Tasks Automatically

`dhcli` does not expose a separate `dhcli create tasks` command because **`dhcli run` manages Tasks automatically**:

1. When you run:
   ```bash
   dhcli run python+job -p my-project -n my-fn -f run.yaml
   ```
2. `dhcli` resolves the latest version of function `my-fn` (`python://my-project/my-fn:<fn-uuid>`).
3. `dhcli` queries DigitalHub Core for an existing Task of kind `python+job` attached to that function version. If none exists, `dhcli` automatically creates one via `POST /tasks`.
4. `dhcli` merges the task-level and run-level fields from `run.yaml`'s `spec:` block, injects `spec.task`, `spec.function`, and `spec.local_execution: false`, and submits the Run (`POST /runs`).

> **Rule for Agents**: Never write `spec.task` or `spec.function` manually inside `run.yaml` when invoking `dhcli run`. Configure all Kubernetes resources (`resources`, `envs`, `secrets`, `volumes`, `profile`, `replicas`, `service_ports`, `service_type`) directly under `spec:` in `run.yaml`—Core's Run schema inherits all Task fields automatically.
