# Using Kubernetes resources for runs

This page describes the Kubernetes-related options you can pass to `function.run()` (or to task specs).
To better understand the Kubernetes configuration options, refer to the [Kubernetes documentation](https://kubernetes.io/docs/concepts/).

## Quick checklist

- You need to manage resource limits (more cpu/memory) -> [Set resource requests/limits](#resources)
- You need a GPU -> [Request a GPU profile](#profile)
- You need to mount a volume -> [Declare a volume](#volumes)
- You need to set environment variables -> [Inject secrets and envs](#secrets-envs)
- You need to expose a service -> [Configure service ports](#service-port-type)
- You need to configure security settings -> [Set security context](#security-context)
- You need to scale your application -> [Set replicas](#replicas)

## Resources

Declare hardware requests/limits using the `resources` map. Supported keys:

- `cpu`, number of CPU cores (for example `2` or `500m` for 0.5 cores)
- `mem`, ram amount with unit (for example `4Gi`)
- `gpu`, number of GPUs
- `disk`, space for mounted default disk with unit (for example `10Gi`)

The SDK validates resource strings with a simple pattern (digits or digits+unit). Examples:

```python
resources = {
    "cpu": "2",
    "mem": "4Gi",
    "gpu": "1",
    "disk": "10Gi"
}
```

For GPU selection you need to use a `profile` (see below) depending on your cluster setup.

## Profile

Profiles are templates administrators provide to request specific hardware (for example GPUs). Ask your administrator for available profiles.

```python
# Request 1 GPU A100
profile = "1xa100"
```

## Volumes

Supported volume types: persistent_volume_claim, empty_dir, ephemeral. Each volume requires `volume_type`, `name`, `mount_path` and optionally a `spec`.

### Persistent volume claims (PVC)

Mount a PVC into the container by declaring a `persistent_volume_claim` volume and an optional `spec.size`.

```python
volumes = [{
    "volume_type": "persistent_volume_claim",
    "name": "my-pvc",
    "mount_path": "/data",
    "spec": {"size": "1Gi"}
}]
```

### EmptyDir

Use `empty_dir` for ephemeral in-memory or node-local storage. Provide `spec.size_limit` (optional) and `spec.medium` where supported.

```python
volumes = [{
    "volume_type": "empty_dir",
    "name": "my-empty-dir",
    "mount_path": "/data",
    "spec": {"size_limit": "1Gi"}
}]
```

### Ephemeral volumes

The SDK also supports `ephemeral` volumes (model name: SpecEphemeral). Use this when the runtime exposes ephemeral volume handling; `spec.size` is optional.

```python
volumes = [{
    "volume_type": "ephemeral",
    "name": "tmp-ephemeral",
    "mount_path": "/tmp",
    "spec": {"size": "500Mi"}
}]
```

### Shared volumes

You can mount the same volume in multiple tasks by using the same `name` for the volume in different tasks.

```python
volumes = [{
    "volume_type": "shared_volume",
    "name": "shared-pvc",
    "mount_path": "/shared-data"
}]
```

## Secrets and Envs {#secrets-envs}

Inject secret names into the pod environment via `secrets` (list of strings). It uses existing digitalhub `Secrets` as reference.
Set environment variables as a list of `{name, value}` objects.

```python
secrets = ["my-secret"]
envs = [{"name": "ENV_NAME", "value": "value"}]
```

## Service port and type {#service-port-type}

Expose services using `service_ports` (list of `{port, target_port}`) and `service_type` (`ClusterIP`, `LoadBalancer`, `NodePort`, `ExternalName`).

```python
service_ports = [{"port": 80, "target_port": 80}]
service_type = "NodePort"
```

## Security context {#security-context}

Set `run_as_user` and `run_as_group` (integers) to control the UID/GID the container runs as.
Set `fs_group` (integer) to control the GID for the filesystem.

```python
run_as_user = 1000
run_as_group = 1000
fs_group = 1000
```

## Replicas

Specify the number of replicas for pod/deployment (integer). Some runtimes use this to create a deployment instead of a single pod.

```python
replicas = 3
```
