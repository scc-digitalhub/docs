---
render_macros: true
---

# Create a run

Runs are normally created by calling `run()` on a Function or Workflow. Use `new_run()` for direct run creation; the `kind` and specification parameters depend on the runtime.

{% call function_doc("new_run", "digitalhub.entities") %}
    === "Creation example"

        ```python
        import digitalhub as dh

        run = dh.new_run(
            project="my-project",
            kind="python+run",
            task="task-string",
        )
        ```
{% endcall %}

[Back to Run](./entity.md)
