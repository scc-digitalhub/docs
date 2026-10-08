# Examples

## Function Creation

```python
import digitalhub as dh

project = dh.get_or_create_project("my_project")

# Create function from project
func = project.new_function(
    name="ray-training",
    kind="ray",
    requirements=["torch==2.2.2", "torchvision==0.17.2", "numpy==1.24.1"],
    code_src="src/ray_train.py",
    handler="ray_handler"
)

# Or create function from SDK
function = dh.new_function(
    project="my-project",
    name="ray-training",
    kind="ray",
    requirements=["torch==2.2.2", "torchvision==0.17.2", "numpy==1.24.1"],
    code_src="src/ray_train.py",
    handler="ray_handler"
)
```

## Task Execution

**Job execution:**

```python
run = func.run(action="job", 
    replicas=2,
    min_replicas=2,
    max_replicas=2,
    parameters={"epochs": 1},
    volumes=[
        {
            "name": "data",
            "mount_path": "/data",
            "volume_type": "persistent_volume_claim",
            "spec": {"size": "1Gi"} 
        }
    ]
)
```

**Build image:**

```python
run = function.run(
    action="build",
    instructions=["apt-get install -y git"]
)
```

## Tutorials

Find additional examples in the [tutorial repository](https://github.com/scc-digitalhub/digitalhub-tutorials) of the DSLab GitHub organization.
