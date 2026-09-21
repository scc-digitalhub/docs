# Examples

## Function Creation

```python
import digitalhub as dh

project = dh.get_or_create_project("my_project")

# Create function from project
func = project.new_function(
		"test-hydra-function", 
		kind="hydra", 
		code_src="./example/my_app.py", 
		config_src="./example/config-dh.yaml", 
		python_version="PYTHON3_13", 
		handler="my_app",
		init_function="init",
		complete_function="complete",
		requirements=["hydra-optuna-sweeper==1.2.0"]
	) 

# Or create function from SDK
function = dh.new_function(
    project="my-project",
    name="hydra-function",
    kind="hydra",
    code_src="./example/my_app.py", 
    config_src="./example/config-dh.yaml", 
    python_version="PYTHON3_13", 
    handler="my_app",
    init_function="init",
    complete_function="complete",
    requirements=["hydra-optuna-sweeper==1.2.0"]
)
```

## Task Execution

**Job execution:**

```python
run = func.run(action="job", 
    parameters={
        "hydra.sweeper.n_trials": 5
    },
    workers=5
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
