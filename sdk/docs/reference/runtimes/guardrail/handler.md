---
render_macros: true
---

# Define a Guardrail Handler

See the [Python handler definition](../python/define-function.md) for general handler arguments, inputs, outputs and initialization.

## Error handling and response status

- Processing errors are suppressed and ignored by the middleware; the request passes through.
- In `preprocessor` or `postprocessor` mode, return a `nuclio_sdk.Response` with a non-zero `status_code` to change the response status.
- In `wrapprocessor` mode, return a `nuclio_sdk.Response` with the corresponding status code to prevent propagation to the upstream service.

## Processing phase

The processing-phase header is appended to the event object. Its possible values are:

| Phase | Header value |
| --- | --- |
| Process request headers | `1` |
| Process request body | `2` |
| Process response headers | `4` |
| Process response body | `5` |

{{ page_navigation(("Overview", "overview.md"), ("Python handler definition", "../python/define-function.md")) }}
