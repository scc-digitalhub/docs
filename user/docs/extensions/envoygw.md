# Gateway Extension

*Gateway Extension* allow for attaching a given service to an instance of [Envoy Gateway](https://www.envoyproxy.io/) and specify some extra properties that control the way the service is exposed as well as some extra functionality. More specifically, currently the platform allows for distinguishing

- GenAI services and expose them with [Envoy AI Gateway](https://aigateway.envoyproxy.io/). In this way, some extra functionality may be exploited, including dedicated observability metrics collection and tracing, data monitoring, guardrails, etc.  
- Generic services and expose them with [Envoy Gateway](https://www.envoyproxy.io/) with the additional capabilities of generic observability metrics collection and tracing, data monitoring, guardrails, etc.

In the current version the support for Gateway functionality is limited and includes only the possibility to attach the guardrails to the service instance. 

## Guardrails

Guardrails allow for controlling and adjusting the interaction with a service, for example blocking or changing the input if inappropriate or incomplete, cleaning the output, or responding with some error or default message if necessary. Typically guardrails are attached to GenAI services, but the pattern may be applied to other services as well.

In the current implementation the guardrails should be implemented as [ExtProc Envoy extension services](https://www.envoyproxy.io/docs/envoy/latest/configuration/http/http_filters/ext_proc_filter), using e.g. [Guardrail runtime](../runtimes/guardrail.md). 


To enable the guardrails for the service, it is necessary to add to the service run a list of guardrail endpoints (one for each guardrail), defined as ``host:port`` in the same platform context. It is expected that the ExtProc-compatible gRPC port is exposed at the specified address.