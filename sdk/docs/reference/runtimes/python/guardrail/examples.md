# Examples

## Function Creation


```python
guardrail_function = project.new_function(
    name="request-guardrail",
    kind="guardrail",
    code_src="guardrail.py",
    handler="process",
    python_version="PYTHON3_10",
    processing_mode="preprocessor"
)
```

## Task Execution


**Build image:**

```python
run = function.run(
    action="build",
    instructions=["apt-get install -y git"]
)
```

**Guardrail serve:**

```python
run = guardrail_function.run(
    action="serve",
    replicas=1,
    service_type="ClusterIP"
)
```

## Tutorials

Find additional examples in the [tutorial repository](https://github.com/scc-digitalhub/digitalhub-tutorials) of the DSLab GitHub organization.
