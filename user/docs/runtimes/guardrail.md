# Guardrail runtime

Guardrail runtime allows for defining supporting functions for controlling and adjusting invocation of some sensible services. A typical example of such a function is the guardrail that is used to control the interaction with a LLM service, for example blocking or changing the input if inappropriate or incomplete.

Tecnically, guardrails are defined in the runtime as Python functions that are invoked before the invocation of the service, and/or after the invocation of the service, with the input and output of the service as arguments. They are deployed as gRPC services following the contract defined by [Envoy Proxy ExtProc](https://www.envoyproxy.io/docs/envoy/latest/configuration/http/http_filters/ext_proc_filter) specification. To be able to invoke them, the protected service should be accessed via Envoy gateway, using the Envoy Gateway extension. The extension generates the proxy configuration for the Envoy gateway, which is used to route the requests to the protected service and the guardrails.

More specifically, each Guardrail function is defined with

- ``processing_mode`` bwing either ``preprocessor``, ``postprocessor``, or ``wrapprocessor`` with the corresponding meaning.
- source code, being an inline python code, a reference to the git repository, or a zip archive. The source code should provide also a reference to the ``handler`` - the procedure to be called (i.e., specific python function to be executed). This will be the operation executed by the platform upon handling the corresponding processing phase (e.g., input request body when ``preprocessor`` is used, output response body when ``postprocessor`` is used, and input request body and output response body when ``wrapprocessor`` is used). Additionally, it is possible to specify the ``init`` operation that will be called once upon the service start.
- Python version (supported by the platform).
- optional list of Python dependencies and optionally a custom base image to be used.

To facilitate the operation start and optimize the use of resources, it is possible to perform ``build`` operation on the function. This operation creates a container image starting from the source code, dependency list and optional list of additional instructions. Next time the Job or Service starts, this prebuilt container image will be used for execution.

For the handler function the following assumptions should be taken into account

- eventual processing errors are suppressed and ignored by the middleware; the request passes through.
- if it is necessary to change the status of the response (in pre- or post mode), it is necessary for handler to return an ``nuclio_sdk.Response`` structure containing the ``status_code`` field with the corresponding status code different from 0.
- if in case of ``wrapprocessor`` upon request event it is necesary to prevent the propagation to the upstream service, the wrap processor should return the result and additionally append the ``X-Processing-Status`` header to signal that the processing should be terminated with the corresponding status code. This is necessary to disntinguish from the default status code returned by the processing chain. 
- to distinguish the processing phase of ExtProc, the ``processing-phase`` header is appended to the event object. The possible values are:
  
    - process request headers: 1
    - process request body: 2
    - process response headers: 4
    - process response body: 5   

The details about the specification, parameters, execution, and semantics of the Guardrail runtime may be found in the SDK Guardrail Runtime reference.

## Management with SDK

Check the [SDK guardrail runtime documentation](https://scc-digitalhub.github.io/sdk-docs/reference/runtimes/guardrail/overview/) for more information.
