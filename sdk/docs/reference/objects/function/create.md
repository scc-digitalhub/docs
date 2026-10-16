---
render_macros: true
---

# Create a function

Choose the runtime that matches the function you want to create. Its guide covers runtime-specific prerequisites, function parameters, execution, and examples.

## Choose a function kind

{{ kind_cards([
    ("Python", "../../runtimes/python/python/overview.md", "Create functions with the Python runtime", "python"),
    ("Container", "../../runtimes/container/overview.md", "Run functions packaged in a container image", "container"),
    ("Model serving", "../../runtimes/modelserve/overview.md", "Serve trained models through a model serving runtime", "modelserve"),
    ("DBT", "../../runtimes/dbt/overview.md", "Create a DBT Function and run SQL transformations", "dbt"),
    ("Federated learning", "../../runtimes/flower/overview.md", "Build federated learning functions with Flower", "flower"),
    ("Guardrail", "../../runtimes/python/guardrail/overview.md", "Define guardrail functions with the Python runtime", "guardrail"),
    ("OpenInference", "../../runtimes/python/openinference/overview.md", "Use OpenInference with the Python runtime", "openinference"),
    ("TVM", "../../runtimes/tvm/overview.md", "Create TVM models and services with the TVM runtime", "tvm"),
    ("Hydra", "../../runtimes/hydra/overview.md", "Create Hydra Python functions with the Hydra runtime", "hydra"),
]) }}

## Create a function

Use `new_function()` to create and save a function.

{{ function_doc("new_function", "digitalhub.entities", separate_examples=True) }}

{{ page_navigation(("Entity", "entity.md"), ("Manage", "manage.md")) }}
