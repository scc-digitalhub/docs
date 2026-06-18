# Service Graph Runtime

The **Service Graph** runtime allows for creating and deploying distributed service pipelines for synchronous (HTTP) and asynchronous (RTSP, WebSocket) services. It incorporates the [Service Graph project](https://github.com/scc-digitalhub/digitalhub-servicegraph), with a proprietary declarative DSL for defining the service flows and information passing.

Refer to the ServiceGraph project GitHub for the documentation on how to declare and use the service graph notation in different scenarios, different types of nodes, sources, sinks, and control flow elements.

The runtime allows for defining and deploying the service graph functions, and for running the service graph functions. More specifically, once the flow is defined, the ``serve`` task allows for deploying the graph as a service, connecting to the streaming sources (e.g., MJPEG, RTSP) and exposing corresponding APIS and endpoints (e.g., HTTP, or Web Socket).

The configuration of the service allows for overwrting the default endpoints and other specification properties of the elements of the graph, which allows for reusing the same graph definitions in different settings.

The service graph function specification is therefore based on the Graph Definition in YAML format. The service gruph run specification allows for re-defining spec properties (as parameters) and to control which ports are exposed.

## Management with SDK

Check the [SDK runtime documentation](https://scc-digitalhub.github.io/sdk-docs/reference/runtimes/servicegraph/overview/) for more information.
