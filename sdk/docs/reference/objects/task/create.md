---
render_macros: true
---

# Create a task

Tasks are normally created automatically when a Function or Workflow runs. Use `new_task()` for direct task creation. The `kind` combines an executable kind and an action, such as `python+job`. See the [runtime documentation](../../runtimes/index.md) for runtime-specific configuration.

{% call function_doc("new_task", "digitalhub.entities") %}
    === "Creation example"

        ```python
        import digitalhub as dh

        task = dh.new_task(
            project="my-project",
            kind="python+job",
            function="python://my-project/my-function:latest",
        )
        ```
{% endcall %}

[Back to Task](./entity.md)
