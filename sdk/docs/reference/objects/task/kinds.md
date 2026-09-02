# Task kinds

Task kinds are derived from the kind of the Function or Workflow and the action it executes. Examples include `python+job`, `python+serve`, `container+job`, and `hera+pipeline`.

The task kind determines the task specification validator and the runtime parameters accepted by the action. See the relevant [runtime action](../../runtimes/index.md) documentation for the parameters supported by each action.

## Common task parameters

Function and Workflow tasks can include:

- `resources`: CPU, memory, GPU and disk requests.
- `volumes`: Kubernetes volumes mounted into the task.
- `envs`: Environment variables.
- `secrets`: Secret names injected into the task.
- `profile`: A cluster-defined resource profile.
