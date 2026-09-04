# Kubernetes resources for runs

This page describes the Kubernetes-related options accepted by `function.run()` and task specifications.
For Kubernetes concepts, see the [Kubernetes documentation](https://kubernetes.io/docs/concepts/).

<a id="resources"></a>
??? note "Resources"

    Declare hardware requests with the `resources` map, which can include `cpu`, `mem`, `gpu` and `disk`.

    ```python
    resources = {
        "cpu": 2, # Number of CPU cores
        "mem": "4Gi", # RAM amount with unit
        "gpu": 1, # Number of GPUs
        "disk": "10Gi", # Default disk space with unit
    }
    ```

<a id="profile"></a>
??? note "Profile"

    Profiles are administrator-provided templates for specific hardware, such as GPUs.

    ```python
    # Request one GPU V100
    profile = "1xv100"
    ```

    Use `dh.get_k8s_resource_profiles()` to list available profiles.

<a id="volumes"></a>
??? note "Volumes"

    Supported volume types are `persistent_volume_claim`, `empty_dir`, `ephemeral` and `shared_volume`.
    Each volume uses `volume_type`, `name`, `mount_path` and, where needed, a `spec` map.

    === "Persistent volume claim"

        Mount a PVC with an optional `spec.size`.

        ```python
        volumes = [{
            "volume_type": "persistent_volume_claim",
            "name": "my-pvc",
            "mount_path": "/data",
            "spec": {"size": "1Gi"},
        }]
        ```

    === "EmptyDir"

        Use `empty_dir` for ephemeral in-memory or node-local storage.

        ```python
        volumes = [{
            "volume_type": "empty_dir",
            "name": "my-empty-dir",
            "mount_path": "/data",
            "spec": {"size_limit": "1Gi"},
        }]
        ```

    === "Ephemeral"

        Use `ephemeral` when the runtime exposes ephemeral volume handling. `spec.size` is optional.

        ```python
        volumes = [{
            "volume_type": "ephemeral",
            "name": "tmp-ephemeral",
            "mount_path": "/tmp",
            "spec": {"size": "500Mi"},
        }]
        ```

    === "Shared"

        Use the same `name` in different tasks to mount a shared volume.

        ```python
        volumes = [{
            "volume_type": "shared_volume",
            "name": "shared-pvc",
            "mount_path": "/shared-data",
        }]
        ```

<a id="secrets-and-envs"></a>
??? note "Secrets and envs"

    Inject existing DigitalHub Secrets with `secrets`, a list of names.
    Set environment variables with `envs`, a list of `{name, value}` objects.

    ```python
    secrets = ["my-secret"]
    envs = [{"name": "ENV_NAME", "value": "value"}]
    ```

<a id="service-port-and-type"></a>
??? note "Service port and type"

    Expose services with `service_ports`, a list of `{port, target_port}` maps, and `service_type`.
    Supported service types are `ClusterIP`, `LoadBalancer`, `NodePort` and `ExternalName`.

    ```python
    service_ports = [{"port": 80, "target_port": 80}]
    service_type = "NodePort"
    ```

<a id="security-context"></a>
??? note "Security context"

    Set `run_as_user` and `run_as_group` to control the UID and GID of the container.
    Set `fs_group` to control the filesystem group.

    ```python
    run_as_user = 1000
    run_as_group = 1000
    fs_group = 1000
    ```

<a id="replicas"></a>
??? note "Replicas"

    Specify the desired number of pod or deployment replicas as an integer.

    ```python
    replicas = 3
    ```
