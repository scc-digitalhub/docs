# Open Inference v2 Runtime

Open Inference v2 protocol allows for exposing a Python function or an ML model as an inference API following the [Open Inference v2 protocol](https://github.com/kserve/open-inference-protocol). The protocol defines a set of methods to get the status of the inference service, the model metadata, and to make inference requests.

The inference contract is defined with the definition of input and output tensors, which describe, for each of the input and output tensors, the data type and the shape of the data.

The protocol has two flavors, HTTP REST and gRPC, and both variants are exposed with the runtime. 

The Open Inference runtime defines the functions with

- ``model_name`` - the name of the model to refer to in the Open Inference protocol
- list of ``inputs`` tensor definitions;
- list of ``outputs`` output tensors definitions;

- source code, being an inline python code, a reference to the git repository, or a zip archive. The source code should provide also a reference to the ``handler`` - the procedure to be called (i.e., specific python function to be executed). This will be the operation executed by the platform upon handling the inference request. Additionally, it is possible to specify the ``init`` operation that will be called once upon the service start.
- Python version (supported by the platform).
- optional list of Python dependencies and optionally a custom base image to be used.

Each tensor definition is described with

- ``name`` - the name of the tensor;
- ``shape`` - the shape of the tensor. In case of variable dimensions, the coresponding axis should be set to ``-1``;
- ``datatype`` - the data type of the tensor corresponding to one of the allowed Open Inference protocol data types.

To facilitate the operation start and optimize the use of resources, it is possible to perform ``build`` operation on the function. This operation creates a container image starting from the source code, dependency list and optional list of additional instructions. Next time the Job or Service starts, this prebuilt container image will be used for execution.

The details about the specification, parameters, execution, and semantics of the Open Inference runtime may be found in the SDK Open Inference Runtime reference.

## Management with SDK

Check the [SDK Open Inference runtime documentation](https://scc-digitalhub.github.io/sdk-docs/reference/runtimes/openinference/overview/) for more information.
