# Define a Python Function

This section describes the shared handler contract for Python-runtime functions. The same common model is used by `python`, `guardrail`, and `openinference` functions. A handler is a Python function declared with the standard `def` keyword. Handlers can be simple or accept platform-provided objects and inputs. The runtime injects reserved arguments and provides helpers to map inputs and outputs.

??? example "Example"

    ```python
    from digitalhub_runtime_python import handler

    @handler(outputs=["my-sdk-output", "my-primitive-output"])
    def func(project, run, context, event, input_1, parameter_1):
        project.log_artifact(source="some-file.ext", name="my-artifact")
        run.log_metric("my-metric", -14.6)
        context.logger.info("log-some-string")

        body = event.body
        # Process the event body

        df = input_1.as_df(sep=";")
        df.head(70)

        parameter_1.pop("some-key")

        return df, 19.45
    ```

    The function you define becomes the entrypoint when referenced as the `handler` in the run configuration.

There are 4 components to know when defining a Python function for the runtime:

<div class="list-cards" markdown>
- [Reserved arguments](#reserved-arguments){ .list-card-link }
- [Inputs and parameters](#inputs-and-parameters){ .list-card-link }
- [Handler and outputs](#handler-and-outputs){ .list-card-link }
- [Init function](#init-function){ .list-card-link }
- [Runtime-specific behavior](#runtime-specific-behavior){ .list-card-link }
</div>

## Reserved arguments

The runtime injects a small set of reserved arguments when it invokes your handler. Commonly injected values are:

- `project` — the current [`Project` object](../../objects/project/entity.md).
- `run` — the active [`Run` object](../../objects/run/entity.md).
- `context` — the Nuclio runtime context object (see Nuclio Python runtime docs) — only available in remote execution.
- `event` — the Nuclio event object — only available in remote execution.

!!! warning "Local execution: Nuclio context and event"
    When running locally, `context` and `event` are not provided automatically; if your handler expects them you must pass them explicitly through `function.run()`.

## Inputs and parameters

Inputs and parameters map function argument names to values provided at run time. They are passed to the run via the `inputs` and `parameters` arguments of `function.run()` and are stored in the `Run` spec.

- Inputs must reference platform entities (for example `Dataitem`, `Artifact`, or `Model`) by their keys.
- Parameters may be plain Python values (strings, numbers, dicts, lists, etc.).
- The argument names in the two maps must match the handler signature. Reserved names (`project`, `run`, `context`, and `event`) are supplied by the runtime when they appear in the signature.

??? example "Example"

    ```python
    # Function signature: di is a Dataitem, param1 is a string
    def func(di: Dataitem, param1: str):
        # do something
        ...

    # Create or obtain the dataitem
    sdk_dataitem = sdk.new_dataitem(...)

    # Run the function, mapping the argument name to the dataitem key
    sdk_function.run(inputs={"di": sdk_dataitem.key},
                    parameters={"param1": "some value"})
    ```

!!! warning "Inputs vs parameters"
    Passing a parameter where an input is expected can produce an error stating the SDK cannot parse an `entity_key`. If you see that error, double-check which values you provided in `inputs` vs `parameters`.

## Handler and outputs

Decorating a function with `@handler` (from `digitalhub_runtime_python`) allows you to name and collect outputs from the run. The decorator maps returned values to `outputs` and `results` on the resulting `Run` object.

??? example "Example"

    ```python
    from digitalhub_runtime_python import handler

    @handler(outputs=["data", "string"])
    def func(di: Dataitem, param1: str):
        # produce a Dataitem and a primitive
        return pd.DataFrame, "some value"


    run = sdk_function.run(inputs={"di": sdk_dataitem.key},
                        parameters={"param1": "some value"},
                        ...)

    # After the run completes
    run.output("data")   # returns a Dataitem object
    run.result("string") # returns "some value"
    ```

The `outputs` list can contain names or descriptors. A descriptor explicitly
selects the entity kind to log and can pass kind-specific specification fields:

??? example "Example with descriptor"

    ```python
    @handler(outputs=[
        {"name": "model", "kind": "sklearn", "spec_kwargs": {"framework": "sklearn"}},
    ])
    def train():
        return trained_model_path
    ```

Returned values are classified as follows:

- `Dataitem`, `Artifact`, or `Model` objects are recorded as entity outputs.
- Supported dataframe objects are logged as table dataitems.
- Other objects are serialized and logged as artifacts.
- Strings, numbers, booleans, and bytes are stored as primitive results.
- `None` produces no result. A tuple or list is treated as multiple positional results.

Entity outputs are available through `run.output(name)`; primitive values are
available through `run.result(name)`. If the decorator is omitted, returned
values receive default names such as `output_0`. If the number of declared
names differs from the number of returned values, missing names also use this
default pattern and extra names are ignored.

## Init function

When executing remotely, the Nuclio wrapper calls an `init` function (if present) before invoking your handler. The runtime injects the Nuclio `context` into `init` at invocation time. Additional parameters may be supplied via `init_parameters` in `function.run()`.

??? example "Init function"

    ```python
    def init(context, param1, param2):
        # initialization logic
        ...


    run = sdk_function.run(...,
                        init_parameters={"param1": "some value",
                                            "param2": "some value"})
    ```

## Runtime-specific behavior

The runtime-specific behavior section describes differences in how various runtimes handle function execution, inputs, outputs, and other aspects of the function lifecycle.

### Openinference

In addition to the common `project`, `run`, `context`, and `event` arguments, an OpenInference handler receives `request`, an OpenInference `InferRequest` object.

The handler returns a response object containing the protocol outputs.

??? example "Example"

    ```python
    def func(project, run, context, event, request):
        run.log_metric("my-metric", -14.6)
        image_bytes = request.inputs[0].data

        return {
            "outputs": [
                {
                    "name": "caption",
                    "datatype": "BYTES",
                    "data": [caption],
                    "shape": [1, len(caption)],
                }
            ]
        }
    ```

See the [Open Inference Protocol](https://github.com/open-inference/open-inference-protocol) for the protocol details.

### Guardrail

For a guardrail handler, the following assumptions apply:

A - Eventual processing errors are suppressed and ignored by the middleware; the request passes through.

B - To change the response status in pre-processing or post-processing mode, return a `nuclio_sdk.Response` structure containing a non-zero `status_code`.

C - In `wrapprocessor` mode, return a `nuclio_sdk.Response` with the corresponding status code to prevent propagation to the upstream service.

D - To distinguish the ExtProc processing phase, the processing-phase header is appended to the event object. Possible values are:

   - process request headers: 1
   - process request body: 2
   - process response headers: 4
   - process response body: 5
