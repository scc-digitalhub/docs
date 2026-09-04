# Flower runtime

The Flower runtime enables you to execute federated learning tasks using the [Flower](https://flower.dev/) framework. It registers Function kinds `flower-app`, `flower-client`, and `flower-server` for training, building and deploying federated applications.

## Prerequisites

| Requirement | Details |
| --- | --- |
| Python | >= 3.10, < 3.15 |
| Package | `digitalhub-runtime-flower` |
| Local simulation extra | `digitalhub-runtime-flower[local]` |

## Supported kinds and actions

| Function kind | Supported actions | Purpose |
| --- | --- | --- |
| `flower-app` | `train` | Execute Flower simulations |
| `flower-client` | `build`, `deploy` | Define a Flower client |
| `flower-server` | `build`, `deploy` | Coordinate federated learning |

## Usage pattern

To execute a federated learning task, follow this pattern:

1. Implement the Flower application, client or server.
2. Use `dh.new_function()` or `project.new_function()` to create the function, passing function parameters.
3. Call `function.run()` with the desired action, passing task parameters and run parameters.

??? example "Run a Flower application"

	```python
	function = dh.new_function(
		name="my-flower-app",
		kind="flower-app",
		source="git+https://github.com/your-org/your-repo"
	)

	run = function.run(
		action="train",
		federation="my-federation",
		superlink="superlink-service",
		parameters={"num_rounds": 10}
	)
	```

## Local vs remote execution

Only `flower-app` with the `train` action supports local execution.

- **Local execution** (`local_execution=True`): Runs directly on the local machine using Flower simulation mode. Install the `local` extra and the application dependencies.
- **Remote execution** (`local_execution=False`, default): Runs on a server or cluster managed by the platform.

For `flower-client` and `flower-server`, `run()` automatically builds an image when none is configured. Set `auto_build=False` when you want to deploy only an existing image.

## Action documentation

Review the detailed parameters for each Flower action:

<div class="list-cards" markdown>

- [**flower-app train**](actions/flower-app-train.md){ .list-card-link }

	Run a Flower federated-learning simulation.

- [**flower-client build**](actions/flower-client-build.md){ .list-card-link }

	Build a Flower client image.

- [**flower-client deploy**](actions/flower-client-deploy.md){ .list-card-link }

	Deploy a Flower client.

- [**flower-server build**](actions/flower-server-build.md){ .list-card-link }

	Build a Flower server image.

- [**flower-server deploy**](actions/flower-server-deploy.md){ .list-card-link }

	Deploy a Flower server.

</div>

## Examples

<div class="list-cards" markdown>

- [**Flower examples**](examples.md){ .list-card-link }

	Explore complete examples for local simulations and federated roles.

</div>
