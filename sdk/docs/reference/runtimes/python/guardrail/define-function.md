# Define a Guardrail Function

This section describes how to define a Guardrail-runtime handler. A handler is a Python function declared with the standard `def` keyword. Handlers can be simple or accept platform-provided objects and inputs. The runtime injects reserved arguments and provides helpers to map inputs and outputs.

## Function Anatomy

![Function Diagram](../asset/function.png)

**Example handler:**

```python

def func(project, run, context, event):
    run.log_metric("my-metric", -14.6)
    context.logger.info("log-some-string")

    body = event.body
    # Process the event body

    df = input_1.as_df(sep=";")
    df.head(70)

    parameter_1.pop("some-key")

    return df, 19.45
```

**Simple handler (no parameters, no return):**

```python
def func():
    print("hello world")
```

The function you define becomes the entrypoint when referenced as the `handler` in the run configuration.

## Reserved arguments

The runtime injects a small set of reserved arguments when it invokes your handler. Commonly injected values are:

- `project` — the current [`Project` object](../../../objects/project/entity.md).
- `run` — the active [`Run` object](../../../objects/run/entity.md).
- `context` — the Nuclio runtime context object (see Nuclio Python runtime docs) — only available in remote execution.
- `event` — the Nuclio event object — only available in remote execution.

For the handler function the following assumptions should be taken into account

- eventual processing errors are suppressed and ignored by the middleware; the request passes through.
- if it is necessary to change the status of the response (in pre- or post mode), it is necessary for handler to return an ``nuclio_sdk.Response`` structure containing the ``status_code`` field with the corresponding status code different from 0.
- if in case of ``wrapprocessor`` upon request event it is necesary to prevent the propagation to the upstream service, the wrap processor should return the result as ``nuclio_sdk.Response`` with the corresponding status code.
- to distinguish the processing phase of ExtProc, the processing-phase header is appended to the event object. The possible values are:
  - process request headers: 1
  - process request body: 2
  - process response headers: 4
  - process response body: 5

## Init function

If defined, Nuclio wrapper calls an `init` function (if present) before invoking your handler. The runtime injects the Nuclio `context` into `init` at invocation time. Additional parameters may be supplied via `init_parameters` in `function.run()`.

```python
def init(context, param1, param2):
    # initialization logic
    ...


run = sdk_function.run(...,
                       init_parameters={"param1": "some value",
                                        "param2": "some value"})
```
