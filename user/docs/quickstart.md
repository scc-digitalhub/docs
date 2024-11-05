# Quick Start

To start with DigitalHub, the first step is to install the platform and all its components. For its functionality, DigitalHub relies on [Kubernetes](https://kubernetes.io/), a state-of-art Open-Source containerized application deployment, orchestration and execution platform. While it is possible to run DigitalHub on any Kubernetes installation, the quickest way is to deploy it on [Minikube](https://minikube.sigs.k8s.io/docs/start), a local Kubernetes environment with minimal settings. See [here](installation.md) instruction on how to set up DigitalHub on Minikube.

Once installed, you can access different platform components and perform different operations, ranging from exlorative data science with Jupyter Notebooks, creating projects for data processing or ML tasks, managing necessary resources (e.g., databases or datalake buckets), creating and running different functions, etc.

## Platform Components and Functionality

To access the different components of the platform start from the [landing page](./components/dashboard.md), where the components are linked:

- Use **Coder** to create interactive workspaces, such as Jupyter Notebooks, to perform explorative tasks, access and manage the data. See how to use [Workspaces](./tasks/workspaces.md) for these type of activities.
- Use **DH Core** UI to manage your data science and ML project and start with management activities, such as creating data items, defining and executing different functions and operations. Please note that these tasks may be done directly with the DH Core Python SDK from your interactive environment. See how to use [DH Console](./components/dh_console.md) for the management operations.
- To see and manage the relevant Kubernetes resources (e.g., services, jobs, secrets), as well as custom resources of the platform (e.g., databases, S3 buckets, data services), use **Kubernetes Resource Manager**. The operations and the functionality of the tool are described in the [Resource Management with KRM](./tasks/resources.md) section of the documentation.
- Use **Minio** browser to navigate your datalake, upload and manage the files. The datalake is based on S3 protocol and can be used also programmatically. See the [Data and Transformations](./tasks/data.md) section on how the data abstraction layer is defined and implemented.
- If you perform ML task with the Python runtime, you can prepare data, create and log ML Models using DH Core (see, e.g., [Python Runtime](./runtimes/python.md) if you want to use python operations through DHCore). 
- Use **Core** Serverless platform to deploy and expose Python functions or ML Models in different formats as services within the platform.
- It is possible to organize the data and ML operations in complex pipelines. Currently the platform relies on **Kubeflow Pipelines** specification for this purpose, orchestrating the activities as single Kubernetes Jobs. See more on this in the corresponding [Pipelines](./tasks/workflows.md) section.

## Tutorials

Start exploring the platform through a series of tutorials aiming at explaining the key usage scenarios for DigitalHub platform. Specifically

- Create your first [data management pipeline](./scenarios/etl/intro.md), from data exploration to automated data ETL procedure running on the platform.
- Perform [DBT data transformation](./scenarios//etl-core/scenario.md) and store the data in a database.
- [Train a scikit-learn ML Model](./scenarios/mlsklearn/intro.md) and deploy it as an inference server.
- [Train a MLFLow-compatible Model](./scenarios/mlmlflow/intro.md) and deploy it as an inference server.
- [Train a custom ML Model](./scenarios/ml/intro.md) and deploy it as a service with the serverless platform.
- [Work with LLM Model](./scenarios/mlllm/llm.md) and deploy it as a service with the serverless platform.
- Use Dremio distributed query engine to [organize data and visualize with Grafana](./scenarios/dremio_grafana/scenario.md).
- Store data in DB to perform efficient and complex queries and [expose the data as REST API](./scenarios/postgrest/intro.md).
