# ServiceGraph runtime

The ServiceGraph runtime enables deploying real-time synchronous and asyncronous service pipelines based on [ServiceGraph](https://github.com/scc-digitalhub/digitalhub-servicegraph) project. The pipelines may be used to orchestrate a set of AI services, build processing chains for streaming data, etc. See the project documentation for more details.

The runtime allows defining and deploying a service graph orchestrator as a service from declarative pipeline definitions. It supports the `serve` action for orchestrator deployment.

## Prerequisites

| Requirement | Details |
| --- | --- |
| Python | >= 3.10, < 3.15 |
| Package | `digitalhub-runtime-servicegraph` |

## Usage pattern

To deploy a ServiceGraph pipeline as a service, follow this pattern:

1. Define the pipeline model using ServiceGraph DSL in YAML format.
2. Use `dh.new_function()` or `project.new_function()` to create the function, passing function parameters.
3. Call `function.run(action="serve")` with task and run parameters to customize the specification, such as service endpoints and source references.

??? example "Deploy a ServiceGraph pipeline"

    ```python
    function = dh.new_function(
        name="my-graph",
        kind="servicegraph",
        code_src="src/flow.yaml"
    )

    run = function.run(
        action="serve",
        parameters={"input.url": "http://videosource:1984"}
    )
    ```

ServiceGraph functions are executed remotely on Kubernetes clusters managed by the platform.

Use `run.refresh()` and inspect `run.status`. When ready, the `status` will include a `service` attribute.

??? example "Wait for readiness"

    ```python
    run.refresh()
    run.status
    ```

Testing the deployed pipeline depends on the pipeline source.

For synchronous pipelines with the HTTP source, call the inference endpoint with `run.invoke()`. By default the `url` is taken from the `run` object; override it with an explicit `url` parameter if needed.

??? example "Invoke a synchronous pipeline"

    ```python
    data = [[...]]
    json = {"inputs": data}

    run.invoke(json=json)
    ```

For streaming services, the testing can be done attaching the pipeline to some data source (e.g., RTSP, MJPEG) and then observing one of the defined outputs (e.g., log output, MJPEG output).

If needed, it is possible to customize the ports the service exposes in order to access inputs/outputs of the pipeline.

## Sync, streaming and port customization

For streaming services, attach the pipeline to a data source such as RTSP or MJPEG and observe one of the defined outputs, such as a log or MJPEG output. Customize the exposed ports when you need direct access to pipeline inputs or outputs.

## Action documentation

Review the detailed parameters for the ServiceGraph action:

<div class="list-cards" markdown>

- [**Serve**](actions/servicegraph-serve.md){ .list-card-link }

    Deploy a synchronous or streaming ServiceGraph pipeline.

</div>

## Examples

<div class="list-cards" markdown>

- [**ServiceGraph examples**](examples.md){ .list-card-link }

    Explore complete examples for YAML pipelines, synchronous requests and streaming services.

</div>
