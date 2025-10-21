# Federated Learning with Flower

[Flower Federated Learning](https://flower.ai/) framework allows for running federated learning tasks where different client nodes perform local training and cooperatively create a more robust solution without exchanging the data but only the weight necessary to progress the training process. 

The platform support this approach natively integrating the Flower framework in the following manner:

- support creating a federation, with central Superlink node and a set of client Supernodes distributed potentially outside of the platform in a secure manner (with TLS verification and client authentication)
- activate the training procedures defined with the server coordination code and client training code managed by the platform. 

See more details in the description of the corresponding [Flower runtime](../../runtimes/fl.md).

This tutorial  demonstrates how to use the Flower FL framework for execution of federated learning tasks. The tutorial is based on official Pandas example of Flower framework.

## Initalize the project

Create a project where we define and start the federation Superlink node and the training function.

```python
import digitalhub as dh

project = dh.get_or_create_project("test-flower")
```

## Create and Start Server part: Superlink

The following defines the Superlink function, build the corresponding image, and activates the server container with the dependencies.  
Note that the server is started in `insecure` mode, meaning that no TLS verification is performed. While this is ok for the purpose of this tutorial, should not be used in a production federation.

In secure mode the server will be equipped with a custom platform-level TLS certificate that should also be used by client SuperNode nodes.

```python
server_function = project.new_function(
    name="my-flower-server",
    kind="flower-server",
    requirements=["pandas==2.2.3", "flwr-datasets[vision]==0.5.0"]
)
# Build the server
server_function.run(action="build", wait=True)

# Deploy the server
run = server_function.run(action="deploy", insecure=True)
```

## Create and Start Client part: Supernode

The following defines the Supernode function, build the corresponding image, and activates 3 client nodes container with the dependencies and the node-specific configuration.  

Note that the server is started in `insecure` mode as no root certificate is provided. To enable secure mode, it is necessary to specify the `root_certificates` attribute to each run containing the body of the public root certificate.

Also the node authentication is not enabled in this scenario. The node authentication allows for controlling which nodes are allowed to communicate with the server. To achieve this, it is necessary

- at each node define a public-private key pair and store the values in project secrets.
- pass the secret names as `public_key_secret` and `private_key_secret` parameters to the supernode spec
- ensure the public key is included in `auth_public_keys` field of the server Superlink node

Each client is started with the own set of parameters (`node_config`) and a reference to the `superlink` pointing to the superlink address (port 9092 by default).

```python 
server_url = run.refresh().status.service['url'].split(':')[0] + ':9092' 

client_function = project.new_function(
    name="my-flower-client",
    kind="flower-client",
    requirements=["pandas==2.2.3", "flwr-datasets[vision]==0.5.0"]
)

client_function.run(action="build", wait=True)

# Deploy client 1
run = client_function.run(action="deploy", superlink=server_url, node_config={
        "partition-id": 0,
        "num-partitions": 3,
        "local-epochs": 2
})

# Deploy client 2
run = client_function.run(action="deploy", superlink=server_url, node_config={
        "partition-id": 1,
        "num-partitions": 3,
        "local-epochs": 2
})

# Deploy client 3
run = client_function.run(action="deploy", superlink=server_url, node_config={
        "partition-id": 2,
        "num-partitions": 3,
        "local-epochs": 2
})
```

# Create and Start the training execution

To perform the actual training procedure, we define a new flower app function with the application code for client and server.
Specifically, it is necessary to provide either the reference to a complete Git project or, as in this case, the reference to the client and server source code files:

- `client_src` provides reference to the  client source code, while `client_app` defines the reference in the code to the ClientApp instance.
- `server_src` provides reference to the  server source code, while `server_app` defines the reference in the code to the ServerApp instance.

```python
app_function = project.new_function(
    name="my-flower-app",
    kind="flower-app",
    client_src="src/client.py",
    server_src="src/server.py",
    client_app="app",
    server_app="app"

)
```

The code of the client looks as follows:

```python
"""pandas_example: A Flower / Pandas app."""

import warnings

import numpy as np
from flwr_datasets import FederatedDataset
from flwr_datasets.partitioner import IidPartitioner

from flwr.client import ClientApp
from flwr.common import Context, Message, MetricRecord, RecordDict

fds = None  # Cache FederatedDataset

warnings.filterwarnings("ignore", category=UserWarning)


def get_clientapp_dataset(partition_id: int, num_partitions: int):
    # Only initialize `FederatedDataset` once
    global fds
    if fds is None:
        partitioner = IidPartitioner(num_partitions=num_partitions)
        fds = FederatedDataset(
            dataset="scikit-learn/iris",
            partitioners={"train": partitioner},
        )

    dataset = fds.load_partition(partition_id, "train").with_format("pandas")[:]
    # Use just the specified columns
    return dataset[["SepalLengthCm", "SepalWidthCm"]]


# Flower ClientApp
app = ClientApp()


@app.query()
def query(msg: Message, context: Context):
    """Construct histogram of local dataset and report to `ServerApp`."""

    # Read the node_config to fetch data partition associated to this node
    partition_id = context.node_config["partition-id"]
    num_partitions = context.node_config["num-partitions"]

    dataset = get_clientapp_dataset(partition_id, num_partitions)

    metrics = {}
    # Compute some statistics for each column in the dataframe
    for feature_name in dataset.columns:
        # Compute histogram
        freqs, _ = np.histogram(dataset[feature_name], bins=np.linspace(2.0, 10.0, 10))
        metrics[feature_name] = freqs.tolist()

        # Compute weighted average
        metrics[f"{feature_name}_avg"] = dataset[feature_name].mean() * len(dataset)
        metrics[f"{feature_name}_count"] = len(dataset)

    reply_content = RecordDict({"query_results": MetricRecord(metrics)})

    return Message(reply_content, reply_to=msg)
```

The code of the server part looks like follows:

```python
"""pandas_example: A Flower / Pandas app."""

import random
import time
from collections.abc import Iterable
from logging import INFO

import numpy as np

from flwr.common import Context, Message, MessageType, RecordDict
from flwr.common.logger import log
from flwr.server import Grid, ServerApp

app = ServerApp()


@app.main()
def main(grid: Grid, context: Context) -> None:
    """This `ServerApp` construct a histogram from partial-histograms reported by the
    `ClientApp`s."""

    num_rounds = context.run_config["num-server-rounds"]
    min_nodes = 2
    fraction_sample = context.run_config["fraction-sample"]

    for server_round in range(num_rounds):
        log(INFO, "")  # Add newline for log readability
        log(INFO, "Starting round %s/%s", server_round + 1, num_rounds)

        # Loop and wait until enough nodes are available.
        all_node_ids: list[int] = []
        while len(all_node_ids) < min_nodes:
            all_node_ids = list(grid.get_node_ids())
            if len(all_node_ids) >= min_nodes:
                # Sample nodes
                num_to_sample = int(len(all_node_ids) * fraction_sample)
                node_ids = random.sample(all_node_ids, num_to_sample)
                break
            log(INFO, "Waiting for nodes to connect...")
            time.sleep(2)

        log(INFO, "Sampled %s nodes (out of %s)", len(node_ids), len(all_node_ids))

        # Create messages
        recorddict = RecordDict()
        messages = []
        for node_id in node_ids:  # one message for each node
            message = Message(
                content=recorddict,
                message_type=MessageType.QUERY,  # target `query` method in ClientApp
                dst_node_id=node_id,
                group_id=str(server_round),
            )
            messages.append(message)

        # Send messages and wait for all results
        replies = grid.send_and_receive(messages)
        log(INFO, "Received %s/%s results", len(replies), len(messages))

        # Aggregate partial histograms
        aggregated_hist = aggregate_partial_histograms(replies)

        # Display aggregated histogram
        log(INFO, "Aggregated histogram: %s", aggregated_hist)


def aggregate_partial_histograms(messages: Iterable[Message]):
    """Aggregate partial histograms."""

    aggregated_hist = {}
    total_count = 0
    for rep in messages:
        if rep.has_error():
            continue
        query_results = rep.content["query_results"]
        # Sum metrics
        for k, v in query_results.items():
            if k in ["SepalLengthCm", "SepalWidthCm"]:
                if k in aggregated_hist:
                    aggregated_hist[k] += np.array(v)
                else:
                    aggregated_hist[k] = np.array(v)
            if "_count" in k:
                total_count += v

    # Verify aggregated histogram adds up to total reported count
    assert total_count == sum([sum(v) for v in aggregated_hist.values()])
    return aggregated_hist
```

## Running the training function

The execution of the application run is a single job that bundles the application and interacts with the superlink to deploy, activate, and coordinate the federated learning execution. 

Each execution requires the reference to the corresponding execution API of the Superlink (port 9093) and optionally a set of hyperparameters.

Note that the server is started in `insecure` mode as no root certificate is provided. To enable secure mode, it is necessary to specify the `root_certificates` attribute to each run containing the body of the public root certificate.

```python
server_url = server_url.split(':')[0] + ':9093' 

app_run = app_function.run("train", superlink=server_url, parameters={
    "num-config-rounds":3,
    "fraction-sample": 1.0
})
```

The status and log of the execution may be obtained from the corresponding app run, e.g., through the Core Web UI. While not included in this example, the server procedure may create a model that can be logged using the platform SDK and used later for further operations (e.g., inference).