# Key Concepts and Entities

## Projects

A *project* is used to scope an AI application and serves as a container for different entities (code, assets, configuration, ...) that make part of the application. It is the context in which you can develop the application, that is prepare the data, train and deploy the model etc. A project is therefore made of other types of entities, representing the data entities (data items and artifacts), AI models, source code (functions and their pipeline compositions). The evolution of these entities, their different versions, as well as execution of different functions and their metrics are scoped to the project.

Furthermore, the project defines the space of collaboration, allowing different users to work simultaneously, sharing the underlying operations and experiments, common secrets and configurations.

## Data and Artifacts

Data is the one of the key elements the project operate. Data entities may represent the raw data provided as input to the processes and services,
may represent features extracted from the raw data or synthetic datasets derived from it, etc. 

Logically, we support different types of data and their representations:

- *data items*, which represent immutable data sets resulting from different transformation operations and are ready for use in differerent types of analysis. Tabular data items are represented in the form of *Parquet* files. It is possible to treat tabular data (items of ``table`` kind) as, for example, *DataFrames*, using conventional libraries.
- *artifacts*, which represent arbitrary files and folders, not limited to tabular format, stored to the datalake with some extra metadata. 

All the data entities are enriched with metadata: common ones, such as versions, lineage, stats, and type-specific, such as profiling, schema. 
Each data entiy is equipped with unique key and version and managed and persisted to the datalake directly by the platform.

Even an external data object may be represented in the platform as a reference, provided a unique data URL and the associated kind for the appropriate management. 

Listing and tracking the data entities is one of the key functionality of the platform essential for structured, transparent, and reproducible data and ML operations.

## ML/AI Models

Support for MLOps is one of the key functionalities of the platform. Creating, managing and serving ML models is supported by the platform via ML Model entities and the corresponding functionality for their registration and serving.

ML Model entity represent the relevant information about the model - framework and algorithms used to create it, hyperparameters and metrics, necessary artifacts constituting the model, etc. The platform is agnostic to the specific framework used to create the model (e.g., pytorch or tensorflow), to package it (e.g., Huggingface or MLFlow), but for some of the frameworks the platform provides further support, such as model *serving* runtimes that allow for exposing the underlying inference function in a no-code or low-code manner.

An important functionality provided aby the platform as first-class support is the ability to run different ML experiments and track different versions with the models equipped with the model metrics in order to compare and identify the most appropriate ones. ML metrics may be associated to the model upon model validation. 

## Functions, Runtimes, and Runs

**Functions** are the logical description of something that the platform may execute and track for you. A function may represent code to run as a job, an ML model inference to be used as batch procedure or as a service, a data validation, etc.

In the platform we perform **actions** over functions (also referred to as "tasks"), such as job execution, deploy, container image build. A single action execution is called **run**, and the platform keeps track of these runs, with metadata about function version, operation parameters, and runtime parameters for a single execution.

In this way, functions and actions may represent a very different scenarios:

- Jobs that perform data preparation and extraction operations;
- ML model training and validation experiments;
- data analysis jobs to produce analysis reports and corresponding evidences;
- Converting a model into an inference function and exposing it as a service (API);
- Running a Retrieval Augmented Generation (RAG) application;
- Creating a monitoring application that observes the data and predictions of a model to identify the data drift and to trigger a new training;
- Run a Federated Learning algoritm across different distributed nodes.

The functions and the corresponding actions represent the key point of extension in order to add new functionality to the platform in a modular way. For this, functiona are associated with a **runtime**, which implements the actual execution and determines which actions are available. Examples of a runtime are DBT, Container, Python, Model Serving, etc. Runtimes  are highly specialized components which can translate the representation of a given execution, as expressed in the run, into an actual execution operation performed via libraries, code, external tools etc.

## Pipelines

*Workflows* allow for organizing the single operations in advanced management pipelines, to perform a series operation of data processing, ML model training and serving, etc. Workflows represent long-running procedures defined as Directed Acyclic Graphs (DAGs) where each node is a single unit of work performed by the platform (e.g., as a Kubernetes Job).

As such, each step of the workflow is a run of some function that is tracked by the platform and makes the whole workflow execution advance. As well as functions, the code of the workflows is versioned, and each run is tracked by the platform for further analysis. 

## Services

In the platform we use the *services* to expose some function as API, being a ML model inference, some supporting functionality like embedding or ranking, or an LLM. The services are often the entry points for the AI applications; they are deployed as Kubernetes services and managed accordingly. 

While not strictly necessary, the services are activated as *serve* action runs in the corresponding runtimes, being model serving runtime, LLM serving, Python serverless function, or even a custom container. Each server has the corresponding TCP port exposed and allows for invocation using the corresponding protocol, such as HTTP REST API or gRPC. The specific implementation and runtimes define the way the services are exposed and made available. For example

- the LLM model serving runtimes such as [KubeAI](./runtimes/modelserve.md) or [vLLM](./runtimes/modelserve.md) expose the HTTP protocol with OpenAI-compatible API for interacting with the LLMs;
- the Python serverless runtime allows for exposing an arbitrary Python function as a custom HTTP endpoint, a [Open Inference v2](https://kserve.github.io/website/docs/concepts/architecture/data-plane/v2-protocol) protocol;
- [MLFlow model serving](./runtimes/modelserve.md) runtime allows for exposing the MLFlow model as a Open Inference v2 endpoint with gRPC and HTTP protocol;
- the [container](./runtimes/container.md) runtime allows for exposing the container image as a custom HTTP endpoint.

Each serve run generates a separate Kubernetes service instance with a dedicated endpoint, managed by the platform. Through the SDK and UI of the platform it is possible to test the serve execution by sending requests to the exposed endpoint.

Furthermore, using the extensions mechanism, it is possible to enable 
some service-specific extensions to the serve run, such as Envoy gateway integration for observability metrics collection and tracing, data monitoring, guardrails, etc.

## Extensions

As it follows from the name, *extensions* provide a modular way to add extra functionality or extra information to the platform entities. The extensions are implemented as *plugins*, which are small components that are loaded at deployment time and make the platform more flexible and powerfull.

Typical scenarios for the extensions include, but not limited to:

- provide the way to extend the data entities with extra metadata regarding the data validation and profiling such as, profiling report, data validation test results;
- provide the way to extend the model entities with extra metadata regarding the model validation and profiling;
- extend the service runs with the capabilities to enable observability, monitoring, guardrails, etc.

The extensions may be activated on entity creation or added upon execution of some function. Consider for example a scenario, where the data validation procedure is triggered each time a new version of the data entity is being created, generating the corresponding data validation report and attaching it to the data entity status.