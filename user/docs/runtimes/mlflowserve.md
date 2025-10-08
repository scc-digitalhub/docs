# MLFlow serve runtime

**MLFLow serving runtime** is used to expose ML model created and packaged using the [MLFLow](https://mlflow.org/) format. When packaged, the MLFlow model contains all the necessary information for its deployment, including not only the model weights, but also the specification of the dependencies and versions, as well as the serving functions for the model. All this allows for great deployment flexibility without a need to define the custom functions.

o define the MLFLow serving function it is necessary to provide

- ``path`` defining a reference to the model (e.g., S3 URL pointing to the model content)
- ``model`` defining the name of the exposed model
- optional serving image if different from the one used by the platform by default.

The ``serve`` action of the runtime creates a dedicated deployment and exposes the model as a Open Inference Protocol API. The standard resource- and service-related configuration may be specified.

## Management with SDK

Check the [SDK python runtime documentation](https://scc-digitalhub.github.io/sdk-docs/reference/runtimes/modelserve/overview/) for more information.
