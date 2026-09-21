# Hydra

The **hydra runtime** allows you to run complex Python jobs defined with the [Hydra framework](https://hydra.cc). More specifically,
the runtime allows for executing the Hydra configurations directly in the platform, on top of the DH Hydra launcher plugin. In this way, Hydra DH launcher 
suites for multirun execution of the same configuration with different parameters, delegating each configuration to a separate job on the platform. 
This allows for executing the same Python code  outside the platform and within the platform without changing the configurations or the code.

Since by default all the jobs in the platform start with empty storage which is destroyed on job completion, we provide some extra support to prepare the executions and to elaborate on the results. For example, in case of Hyper Parameter Optimization with, e.g., Optuna, it is possible to define some extra scripts that will be executed before the optimization starts (the ``init`` operation) and after the optimization is completed ()the ``complete`` operation.

Another important characteristic of Hydra runtime is that all the executions are provided by a shared persistent volume mounted at ``/shared`` folder where both the application code is executed and where the mutlirun results are stored. This allows the ``complete`` operation to access the single results (e.g., to find the best checkpoint of the optimal model). The dimension of the shared volume is configurable.

With this approach each Hydra runtime function is defined with

- Hydra application source code, being an inline python code, a reference to the git repository, or a zip archive. The source code should provide also a reference to the ``handler`` - the procedure to be called  (i.e., specific python function to be executed) annotated with ``@hydra.main`` wrapper. 
- Hydra configuration specifications, being an inline YAML configuration, or a reference to the configuration folder relative to the source code root.
- optional ``init`` operation to perform some initialization before the configurations are launched (e.g., download a dataset)
- optional ``complete`` operation to perform some cleanup after the all configurations are finished (e.g., upload a best model) and sweeper has completed its execution
- Python version (supported by the platform).
- optional list of Python dependencies and optionally a custom base image to be used.


To facilitate the operation start and optimize the use of resources, it is possible to perform ``build`` operation on the function. This operation creates a container image starting from the source code, dependency list and optional list of additional instructions. Next time the Job or Service starts, this prebuilt container image will be used for execution.

!!! info "Default dependencies"

    Please note that the core Hydra libraries, as well as OmegaConf is already present in the default dependencies. However, if you plan to use specific sweeper (e.g., Optuna), that one should be declared explicitly.

In a nutshell, the Hydra runtime execution is defined by the ``job`` action, which is executed as follows:

1. The container image is built and is started on the platform. The shared volume is mounted to the container.
2. The source code and application configuration is being downloaded, the DH launcher plugin configuration is injected with the values from the run instance parameters (e.g., number of ``workers`` available for parallel execution, job parameters defining the Hydra overrides, etc).
3. The ``init`` operation is called before Hydra app execution.
4. The ``handler`` function is called in the multirun mode with the DH launcher configured.
5. Based on the sweeper configuration and overwrites, a set of configurations is generated and triggered as a separate ``subtask`` action.
6. Each subtask triggered by the sweeper is executed on the platform as a standalone job, with the same image and shared volume, under the profile and resource configuration defined job.  
7. If one of the subtasks fails, the job fails as well.
8. Once all the subtasks are executed, the ``complete`` operation is called. Having the experiment data stored in the shared volume, it is possible to perform post-processing and analysis in that operation before the job completes and the shared volume is destroyed.


The execution parameters of the ``job`` action include
- ``init_parameters`` to be passed to the ``init`` operation (see Python runtime for reference)
- ``parameters`` to be passed to the orchestrating Hydra multirun as overrides (e.g., sweeper configuration)
- ``workers`` number as a maximum number of parallel executions available to sweeper
- ``resource`` specification as a CPU/MEM/shared volume size.
- ``profile`` to be used for the subtasks.
- optional ``secrets``, ``environment``, and extra volumes to be attached to each of the subtasks.


Please note that, like Python runtime jobs, Hydra jobs may be executed locally (``local_execution=True``) for testing purposes. In this case, the subtasks are triggered locally as well, running as separate threads in the same multirun Python process. 


The details about the specification, parameters, execution, and semantics of the Hydra runtime may be found in the SDK Hydra Runtime reference.

## Management with SDK

Check the [SDK hydra runtime documentation](https://scc-digitalhub.github.io/sdk-docs/reference/runtimes/hydra/overview/) for more information.
