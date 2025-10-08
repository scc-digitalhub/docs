# Container runtime

The **Container runtime** allows you to create deployments, jobs and services on Kubernetes starting from arbitrary user-defined container image. That is, container function may be run

- as a **Job** (``action="job"``) representing a single piece of work (e.g., model training, data processing), or
- as a "**Service** (``action="serve"``) representing a Serverless function responding to HTTP requests, or
- as a "**Deployment** (``action="deploy"``) representing a deployment without exposing it as a service.
 
Each container function is defined with

- image specification
- command to run within container. If not provided, the default entry point is triggered.

To customize the image to a specific context, it is possible to perform ``build`` operation on the function. This operation creates a container image starting from the base image and optional list of additional instructions. Next time the Job or Service starts, this prebuilt container image will be used for execution.

When the run is created, it is possible to specify the following information

- resource configuration (see [here](../tasks/run-resources.md) for details about configuring run resources)
- file system properties (e.g., ``run_as_user``, ``fs_group``, ``run_as_group``)
- container arguments defining the specific execution parameters to pass to the container entry point or command.

The details about the specification, parameters, execution, and semantics of the container runtime may be found in the SDK Container Runtime reference.

## Management with SDK

Check the [SDK container runtime documentation](https://scc-digitalhub.github.io/sdk-docs/reference/runtimes/container/overview/) for more information.
