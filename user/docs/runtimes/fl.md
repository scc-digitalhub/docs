# Federated Learning: Flower Runtime

**Flower Runtime** represents the extension of the platform to support the scenarios of federated and compositional Machine Learning going potentially beyond the scope of the platform instance and making different instances or external environments collaborate.

This runtime relies on [Flower Framework](https://flower.ai/) and allows for deploying and running Flower FL applications in different modes. The details about Flower architecture, concepts, and applications may be found in the corresponding specificiation. The Flower runtime integrated in the platform is agnostic to a specific application scenario and supports the following activities

- deploy the nodes of the application federation referred to as Flower ``SuperNode``. The SuperNode represents a single participating element and controls computations of a single application part. In a fully distributed scenario a single node is deployed in platform instance for the given application, while the other nodes may belong to other instances. This is a typical case, e.g., in a medical domain where different tenants collaborate in order to build a single ML model without revealing proprietary data. Other scenario may represent a situation of a distributed paralllel computation, where different nodes run all in the same namespace in parallel each dealing with a dedicated data partition. 
- deploy the central server node of the  application federation referred to as Flower ``SuperLink``. The superlink is the coordinator of the federation; all the supernode connect to it in order to pass the intermediate weights or get the new training instructions. 
- Run the specific application that consists of two parts - server coordination code and the client supernode training part. The application is passed to the superlink that distributes the client code to the supernodes of the federation and coordinates the execution iterations.

Accordingly, the runtime consists of the following elements: 

- ``flower-client`` runtime to define the Flower SuperNode entity. Built upon standard base image, the Flower SuperNode allows for defining additional Python dependencies necessary for the application client part execution.
- ``flower-server`` runtime to define the Flower SuperLink entity. Built upon standard base image, the Flower SuperLink allows for defining additional Python dependencies necessary for the application server part execution.
- ``flower-app`` runtime to define the application to be executed. Requires the application code to be defined, which may be done in two different ways. First, it is possible to provide a reference to the full project (e.g., as git repository reference). The project should be defined as a standard Flower applciation with the corresponding ``pyproject.toml`` specification available in the project root. Second, it is possible to provide the code of client and server parts and reference to the ClientApp and ServerApp objects.

## Flower-server runtime execution

The SuperLink node defined with the corresponding configuration supports two actions: ``build`` and ``deploy``.  The first one creates a container image, which is useful if there are many dependencies to be integrated or custom instructions should be provided to the image.

The deploy tasks creates a new deployment and exposes the correponding interfaces - for the app execution and monitoring, and for the SuperNode nodes to exchange the training information and instructions. The information about the exposed endpoints are available as a part of the ``service`` status of the deployment run. 

The SuperLink deployment parameters include
- resource and environment parameters (e.g., resource profiles, secrets, variables, volumes)
- list of public keys corresponding to the SuperNode nodel that SuperLink will accept. If specified, the SuperLink will accept the only the correpsonding clients. If not specified, any SuperNode will be accepted to the federation and to the training procedure.
- insecure flag to disable TLS verification (for single namespace or test purpose only)

Once deployed, the SuperLink is ready to accept the application run execution requests.

## Flower-client runtime execution

The SuperNode node defined with the corresponding configuration supports two actions: ``build`` and ``deploy``.  The first one creates a container image, which is useful if there are many dependencies to be integrated or custom instructions should be provided to the image.

The deploy tasks creates a new deployment that connects to the specified SuperLink and ready to accept the application code.

The SuperNode deployment parameters include

- SuperLink endpoint: the address of the server node to connect to. 
- isolation mode: ``subprocess`` (default) meaning that the client code will be executed as a subprocess of the Node execution or ``process`` meaning that the client is executed elsewhere (e.g., as a separated container or application) and connects to the SuperNode through a dedicated gRPC port.
- optional private and public code of the node to communicate securely with the SuperLink. If not specified, it is assumed that any client may connect to the server node without restrictions.
- Root TLS certificate of the server node. If specified, a secure TLS communication is established between the server and client. If not specified, the communication s performed in "insecure" mode if supported by the server.
- resource and environment parameters (e.g., resource profiles, secrets, variables, volumes).
- dictionary of client node configuration parameters (key-value pairs) specific to the node environment.

Once deployed, the SuperNode connects to the SuperLink and waits for the training iterations, making polling requests to the SuperLink. In case of ``process`` isolation mode it exposes the corresponding client gRPC port ready for client application communication.

## Flower-app runtime execution

The app specification define the actual application to be executed by the federation. The corresponding ``train`` action performs the following steps following Flower procedure:

- the ``train`` execution packs the application archive and calls the corresponding SuperLink API for the application deployment and execution;
- SuperLink passes the code to the clients and triggers the execution following the execution configuration;
- the ``train`` execution receives the confirmation from the SuperLink and the execution ID. The execution is being monitored and the status of the train execution is updated upon completion.

The execution parameters of the action include

- name of the federation to use. Optional if the code is inline and the auto-generated federation name is used. Otherwise should correspond to the name defined in the application ``pyproject.toml``.
- SuperLink endpoint to connect to with the execution API port.
- SuperLink root TLS certificate if defined by the SuperLink node to establish secure connection. 

## Management with SDK

Check the [SDK flower runtime documentation](https://scc-digitalhub.github.io/sdk-docs/reference/runtimes/flower/overview/) for more information.
