# ServiceGraph Runtime

The ServiceGraph runtime enables deploying real-time synchronous and asyncronous service pipelines based on [ServiceGraph](https://github.com/scc-digitalhub/digitalhub-servicegraph) project. The pipelines may be used to orchestrate a set of AI services, build processing chains for streaming data, etc. See the project documentation for more details.

The runtime allows for defining and deploying a service graph orchestrator as a service starting from declarative pipeline mode. It supports the `serve` action for orchestrator deployment.

## Prerequisites

**Supported Python versions:**

- Python ≥ 3.10, < 3.15

**Required packages:**

- `digitalhub-runtime-servicegraph`

Install from PyPI:

```bash
pip install digitalhub-runtime-servicegraph
```

## Usage overview

To deploy ServiceGraph pipelines as services on the platform:

1. Define the pipeline model using ServiceGraph DSL in YAML format.
2. Create a `Function` resource that references your graph definition.
3. Call `function.run()` to deploy the pipeline as a service customizing the defined specification (e.g., service endpoints, source references, etc).

Use `run.refresh()` and inspect `run.status`. When ready, the `status` will include a `service` attribute.

```python
run.refresh()
run.status
```

Testing the deployed pipeline depends on the pipeline source.

For synchronous pipelines with the HTTP source, call the inference endpoint with `run.invoke()`. By default the `url` is taken from the `run` object; override it with an explicit `url` parameter if needed.

```python
data = [[...]]  # some array
json = {
    ...
}

run.invoke(json=json)
```

For streaming services, the testing can be done attaching the pipeline to some data source (e.g., RTSP, MJPEG) and then observing one of the defined outputs (e.g., log output, MJPEG output).

If needed, it is possible to customize the ports the service exposes in order to access inputs/outputs of the pipeline.

See the [ServiceGraph execution model](../../../explanations/runtimes/servicegraph-execution.md) for supported graph-serving actions.
See [Examples](examples.md) for code samples.
