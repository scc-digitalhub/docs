# Define a Guardrail Function

Guardrail functions use the shared handler contract documented in [Define a Python Function](../define-function.md). This page describes behavior specific to the guardrail middleware.

## Guardrail-specific behavior

For a guardrail handler, the following assumptions apply:

- eventual processing errors are suppressed and ignored by the middleware; the request passes through.
- to change the response status in pre- or post-processing mode, return a `nuclio_sdk.Response` structure containing a non-zero `status_code`.
- in `wrapprocessor` mode, return a `nuclio_sdk.Response` with the corresponding status code to prevent propagation to the upstream service.
- to distinguish the ExtProc processing phase, the processing-phase header is appended to the event object. Possible values are:
  - process request headers: 1
  - process request body: 2
  - process response headers: 4
  - process response body: 5

The handler receives the common `project`, `run`, `context`, and `event` arguments described in the shared page. The `context` and `event` arguments are available only during remote execution.

```python
def init(context, param1, param2):
    # initialization logic
    ...


run = sdk_function.run(...,
                       init_parameters={"param1": "some value",
                                        "param2": "some value"})
```
