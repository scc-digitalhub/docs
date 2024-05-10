# Using Kubernetes Resources for Runs

With Digitalhub SDK you can manage Kubernetes resources for your tasks. When you run a function you can require some Kubernetes resources for the task.

## Resources available and data injection

With Digitalhub SDK you request mainly these Kubernetes resources:

- **Volumes** (pvc, configmap, secret)
- **Hardware resources** (cpu, memory, gpu)

In addition you can inject into the task's container:

- **Secrets**
- **Environment variables**

## Volumes

With SDK you can request four types of volumes:

- **Persistent volume claims (pvc)**
- **ConfigMap**
- **Secret**

### Persistent volume claims (PVC)

You can ask for a persistent volume claim (pvc) to be mounted on the container being launched by the task.
You need to declare the volume type as `persistent_volume_claim`, a name for the PVC for the user (e.g., `my-pvc`), the mount path on the container and a spec with the name of the PVC on Kubernetes (e.g., `pvc-name-on-k8s`).

```python
volumes = [{
        "volume_type": "persistent_volume_claim",
        "name": "my-pvc",
        "mount_path": "/data",
        "spec": {
            "claim_name": "pvc-name-on-k8s",
            }
}]

function.run(volumes=volumes)
```

### ConfigMap

You can ask for a configmap to be mounted on the container being launched by the task.
You need to declare the volume type as `config_map`, a name for the ConfigMap for the user (e.g., `my-config-map`), the mount path on the container and a spec with the name of the ConfigMap on Kubernetes (e.g., `config-map-name-on-k8s`).

```python
volumes = [{
        "volume_type": "config_map",
        "name": "my-config-map",
        "mount_path": "/data",
        "spec": {
            "name": "config-map-name-on-k8s"
        }
}]

function.run(volumes=volumes)
```

### Secret

You can ask for a secret to be mounted on the container being launched by the task.
You need to declare the volume type as `secret`, a name for the Secret for the user (e.g., `my-secret`), the mount path on the container and a spec with the name of the Secret on Kubernetes (e.g., `secret-name-on-k8s`).

```python
volumes = [{
        "volume_type": "secret",
        "name": "my-secret",
        "mount_path": "/data",
        "spec": {
            "secret_name": "secret-name-on-k8s"
        }
}]

function.run(volumes=volumes)
```

## Hardware resources

You can request a specific amount of hardware resources (cpu, memory, gpu) for the task, declared thorugh the `resources` task parameter; `resources` must be a map of Resource objects represented as a dictionary.
At the moment Digitalhub SDK supports:

- **CPU**
- **RAM memory**
- **GPU**

### CPU

You can request a specific amount of CPU for the task.
You need to declare the resource type as `cpu`, request and/or limit specifications.

```python

resources = {
    "cpu": {
        "requests": "12",
        "limits": "16"
    }
}

function.run(resources=resources)
```

### RAM memory

You can request a specific amount of RAM memory for the task.
You need to declare the resource type as `mem`, request and/or limit specifications.

```python
resources = {
    "mem"{
        "requests": "64Gi",
    }
}
function.run(resources=resources)
```

### GPU

You can request a specific amount of GPU for the task.
You need to declare the resource type as `gpu`, request and/or limit specifications. There could be administation-specific requirements for requesting a GPU. You may need to use `tolerations` or `affinity` parameters to request the GPU. Both of these parameters are described in the [Kubernetes documentation](https://kubernetes.io/docs/home/).
Other times you may need to specify a list of labels with the `labels` parameter.

Here is an example for the digitahub in FBK that uses the `tolerations` parameter:

```python

resources = {
    "gpu": {
        "limits": "1"
    }
}
toleration = [{
    "key": "nvidia.com/gpu",
    "operator": "Equal",
    "value": "v100",
    "effect": "NoSchedule"
}]
function.run(resources=resources, tolerations=toleration)
```

## Values injection

You can ask the backend to inject values into the container being launched by the task.
You can inject:

- **Secrets**
- **Environment variables**

### Secrets

You can request a secret injection into the container being launched by the task by passing the reference to the backend with the `secrets` task parameters.

```python
secrets = ["my-secret"]
function.run(secrets=secrets)
```

### Environment variables

You can request an environment variable injection into the container being launched by the task by passing the reference to the backend with the `env` task parameters.

```python
env = [{
    "name": "env-name",
    "value": "value"
}]
function.run(env=env)
```
