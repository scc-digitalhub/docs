---
render_macros: true
---

# Create a function

Use `new_function()` to create and save a function. Its `kind` and specification parameters depend on the selected runtime. See the [runtime documentation](../../runtimes/index.md) for kind-specific requirements and examples.

{% call function_doc("new_function", "digitalhub.entities") %}
    === "Creation example"

        ```python
        import digitalhub as dh

        function = dh.new_function(
            project="my-project",
            name="my-function",
            kind="python",
            code_src="function.py",
            handler="function-handler",
        )
        ```
{% endcall %}

[Back to Function](./entity.md)
