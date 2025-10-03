# Scikit-Learn serve runtime

**Scikit-Learn serving runtime** is used to expose simple inference models created with Scikit-learn framework using Open Inference Protocol. It is expected that the model is packaged as pickle or joblib file and may be served directly, by deserializing model with the sklearn python library and creating a standard Open Inference API out of the box.

More specifically, to define the Scikit-Learn serving function it is necessary to provide

- ``path`` defining a reference to the packaged model
- ``model`` defining the name of the exposed model
- optional serving image if different from the one used by the platform by default.

The ``serve`` action of the runtime creates a dedicated deployment and exposes the model as a Open Inference Protocol API. The standard resource- and service-related configuration may be specified.

## Management with SDK

Check the [SDK python runtime documentation](https://scc-digitalhub.github.io/sdk-docs/reference/runtimes/modelserve/overview/) for more information.
