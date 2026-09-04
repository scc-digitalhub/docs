# DBT runtime

The DBT runtime lets you run [dbt](https://www.getdbt.com/) transformations against your data. It wraps the dbt CLI and exposes a Function of kind `dbt` with a `transform` action.

## Prerequisites

| Requirement | Details |
| --- | --- |
| Python | >= 3.10, < 3.15 |
| Package | `digitalhub-runtime-dbt` |
| Local execution extra | `digitalhub-runtime-dbt[local]` |

The `local` extra installs the dbt Core and PostgreSQL adapter dependencies required for local execution.

## Usage pattern

To execute a dbt transformation, follow this pattern:

1. Use `dh.new_function()` or `project.new_function()` to create the function, passing function parameters.
2. Call `function.run(action="transform")` with task and run parameters.

For a dbt transformation, `inputs`, `outputs` and `local_execution` are run parameters. Kubernetes options such as `resources`, `envs` and `volumes` are task parameters.

??? example "Create and run a dbt transformation"

	```python
	function = dh.new_function(
		name="my-function",
		kind="dbt",
		code="SELECT * FROM {{ ref('my_table_ref') }}"
	)

	run = function.run(
		action="transform",
		inputs={"my_table_ref": dataitem.key},
		outputs={"output_table": "mapped-name"}
	)
	```

## Local vs remote execution

Set `local_execution` in the run parameters to choose where the transformation runs.

- **Local execution** (`local_execution=True`): The function runs on the local machine. Install the `local` extra and make sure the PostgreSQL connection used by DigitalHub is configured and reachable.
- **Remote execution** (`local_execution=False`, default): The function runs on a server or cluster managed by the platform.

## Action documentation

Review the detailed parameters for the DBT action:

<div class="list-cards" markdown>

- [**Transform**](actions/dbt-transform.md){ .list-card-link }

	Execute a dbt transformation with its function, task and run parameters.

</div>

## Examples

<div class="list-cards" markdown>

- [**DBT examples**](examples.md){ .list-card-link }

	Explore complete examples for local and remote dbt transformations.

</div>
