---
render_macros: true
---

# Use a project

The `Project` object is the working context for project state, related entities, and project-level operations.

## Persist and refresh

{{ member_doc("save", "digitalhub.entities.project._base.entity.Project") }}

{{ member_doc("update", "digitalhub.entities.project._base.entity.Project") }}

{{ member_doc("export", "digitalhub.entities.project._base.entity.Project") }}

{{ member_doc("refresh", "digitalhub.entities.project._base.entity.Project") }}

## Manage related entities

The `Project` object exposes project-bound shortcuts for the entities it contains, so the project name is inferred from the object. See [Entities](../index.md) for the available entity types.

```python
artifact = project.get_artifact("my-artifact")
model = project.log_model(source="models/my-model", name="my-model")
functions = project.list_functions()
```

Entity collections are also available through the `artifacts`, `dataitems`, `models`, `functions`, and `workflows` properties.

## Run project operations

Use these methods to execute workflows, search project entities, and manage access.

{{ member_doc("share", "digitalhub.entities.project._base.entity.Project") }}

{{ member_doc("unshare", "digitalhub.entities.project._base.entity.Project") }}

{{ member_doc("search_entity", "digitalhub.entities.project._base.entity.Project") }}

{{ member_doc("run", "digitalhub.entities.project._base.entity.Project") }}

[Back to Project](./entity.md)
