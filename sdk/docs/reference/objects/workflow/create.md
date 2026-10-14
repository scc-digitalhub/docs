---
render_macros: true
---

# Create a workflow

Use `new_workflow()` to create and save a workflow. The `kind` and specification parameters are determined by the Hera runtime. See the [Hera runtime documentation](../../runtimes/hera/overview.md) for runtime-specific requirements.

{% call function_doc("new_workflow", "digitalhub.entities") %}
    === "Creation example"

        ```python
        import digitalhub as dh

        workflow = dh.new_workflow(
            project="my-project",
            name="my-workflow",
            kind="hera",
            code_src="pipeline.py",
            handler="pipeline-handler",
        )
        ```
{% endcall %}

[Back to Workflow](./entity.md)
