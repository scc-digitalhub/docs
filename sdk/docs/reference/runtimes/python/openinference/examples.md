# Examples

## Function Creation


```python
openinference_function = project.new_function(
    name="text-inference",
    kind="openinference",
    code_src="inference.py",
    handler="predict",
    python_version="PYTHON3_10",
    model_name="text-classifier",
    inputs=[{"name": "input-0", "shape": [-1, -1], "datatype": "BYTES"}],
    outputs=[{"name": "output-0", "shape": [-1, -1], "datatype": "FP32"}]
)
```

## Task Execution

**OpenInference build:**

```python
run = openinference_function.run(
    action="build",
    instructions=["pip install transformers"]
)
```

## Service Invocation

After deploying a service:


An OpenInference endpoint receives tensor-oriented payloads:

```python
json_payload = {
    "inputs": [
        {
            "name": "input-0",
            "shape": [-1],
            "datatype": "BYTES",
            "data": ["hello world"]
        }
    ]
}

serve_run = openinference_function.run(action="serve", replicas=1)
serve_run.invoke(json=json_payload)
```

## Tutorials

Find additional examples in the [tutorial repository](https://github.com/scc-digitalhub/digitalhub-tutorials) of the DSLab GitHub organization.
