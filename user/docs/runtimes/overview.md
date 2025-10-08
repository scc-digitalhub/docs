# Runtime Overview

Runtimes define how the platform operationalizes the executable entities. The entities, or **Functions** are the logical description of something that the platform may execute, being a job, an ML model inference service, workflow, etc. A way a specific function is defined and executed depends on runtime. For example, a function may be defined as a piece of program written in Python, while the corresponding Python runtime defines how this code will be packaged into a container and executed in the underlying Kubernetes infrastructure. 

Runtime also defines the operations **actions** (also referred to as "tasks") that we can perform over these functions, such as job execution, deploy, container image build. A single action execution is called **run**, and the platform keeps track of these runs, with metadata about function version, operation parameters, and runtime parameters for a single execution.

Runtimes, therefore, are highly specialized components which can translate the representation (spec) of a given execution, as expressed in the run, into an actual execution operation performed via libraries, code, external tools etc. Runtimes define the key point of extension of the platform: new runtimes may be added in order to implement the low-level logic of "translating" the high level operation definition into an executable run. 

In general, the executables may be divided into the following categories:

- **Jobs** or single pieces of work, representing, e.g., a data transformation, quality check, model training. Once complete, the Job run is being destroyed and the resources are cleaned.
- **Services** (or deployments in general) representing a continuously running executable that possibly exposes some functionality as API. Example of a service may be a Serverless Python function, an LLM model with OpenAI-compatible interface, an inference server, etc.
- **Workflow** or a composite pipeline that integrates a series of jobs into a single procedure. 

Different runtimes follows these separation and provides actions (e.g., **job** action, **serve** action) to create and manage these executables. THe executables therefore may be started manually by the user, autamatically by a trigger, or as a part of a workflow.


