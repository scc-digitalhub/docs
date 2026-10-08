# Ray (Experimental)

The **ray runtime** allows you to run and scale AI and Python applications like machine learning. [Ray framework](https://ray.io) provides the compute layer for parallel processing so that you don’t need to be a distributed systems expert. Ray minimizes the complexity of running your distributed individual workflows and end-to-end machine learning workflows with these components:

- Scalable libraries for common machine learning tasks such as data preprocessing, distributed training, hyperparameter tuning, reinforcement learning, and model serving.

- Pythonic distributed computing primitives for parallelizing and scaling Python applications.

- Integrations and utilities for integrating and deploying a Ray cluster with existing tools and infrastructure such as Kubernetes, AWS, GCP, and Azure.

More specifically, in the context of the platform, the Ray runtime relies on the [KubeRay](https://github.com/ray-project/kuberay) Kubernetes operator to automatically deploy an appropriate Ray cluster alongside with the executed application. The characteristics of the Ray cluster, of its work nodes, is defined by the user: the number of work nodes to allocate and to scale, the resources requested (CPU, mem, storage, or GPU profile), the volumes to attach to the work nodes, the environment variables to be set, etc. The cluster head node is preconfigured.

When the Ray job is triggered with this runtime, the cluster is automatically created (if there exist sufficient resources to host it) and, when ready, the application is submitted to the cluster. It is possible to observe the execution using the UI of the platform or even directly with the integrated Ray dashboard within the Ray runtime run.

An important characteristic of the Ray runtime is that the volumes of type ``persistent_volume_claim`` as well as ``workflow_volume`` are automatically mapped as ``ReadWriteMany`` access to the work nodes.

With this approach each Ray runtime function is defined with

- Ray application source code, being an inline python code, a reference to the git repository, or a zip archive. The source code may provide also a reference to the ``handler``, i.e. the procedure to be called as an entry point to pass the data, parameters, and platform context if needed. 
- Optionally custom Ray image and version to be used for execution (defaults to ``2.55.1``).
- Optional additional Python  dependencies to be used by the application.
- Configuration of the cluster, with minimal, initial, ab maximum number of worker nodes, the resources to be allocated by each node, volumes, environment variables, secrets, etc.

To facilitate the operation start and optimize the use of resources, it is possible to perform ``build`` operation on the function. This operation creates a container image starting from the source code, dependency list and optional list of additional instructions. Next time the Job or Service starts, this prebuilt container image will be used for execution within the cluster.


In a nutshell, the Ray runtime execution is defined by the ``job`` action, which is executed as follows:

1. Based on the cluster configuration properties, the Ray cluster is created. If the necessary resorces are not awailable within the predefined time interval, the job fails. The cluster head node and the defined number of the worker nodes are composing the cluster. The head node does not use the GPU profiles and does not handle the worker tasks. It holds the Ray dashboard and the coordination logic.
2. Once the cluster is started, the submitter container is started, which submites the application code to the Ray cluster for execution.
3. The Ray Dashboard is started on the Ray cluster head node and is made available by the run (through UI or as a port-forward) to monitor the execution of the application.
4. Once the job completes, the resources are released and the cluster is destroyed.


The execution parameters of the ``job`` action include

- ``parameters`` to be passed to the entry point method (handler) if the handler is defined. 
- ``inputs`` to be passed to the entry point method (handler) if the handler is defined. The inputs represent the references to the project entities (e.g. artifacts or datasets) and are handled by the platform SDK.
- ``min_replicas``, ``max_replicas``, ``replicas`` as a minimum, maximum, and initial number of worker nodes for the Ray cluster.
- ``resource`` specification as a CPU/MEM/shared volume size.
- ``profile`` to be used for the subtasks.
- optional ``secrets``, ``environment``, and extra ``volumes`` to be attached to each of the subtasks. The ``volumes``  of type ``persistent_volume_claim`` and ``workflow_volume`` are automatically mapped with ``ReadWriteMany`` access to the work nodes.


The details about the specification, parameters, execution, and semantics of the Hydra runtime may be found in the SDK Ray Runtime reference.

## Management with SDK

Check the [SDK hydra runtime documentation](https://scc-digitalhub.github.io/sdk-docs/reference/runtimes/ray/overview/) for more information.
