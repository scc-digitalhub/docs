---
id: mgmt-kubernetes-resources
domain: management
type: reference
version: "0.16"
tags: [kubernetes, k8s, resources, cpu, mem, gpu, profile, volumes, pvc, empty_dir, ephemeral, envs, secrets, service_ports, replicas, node_selector, tolerations]
schemas:
  - function/container.json
  - run/container+job:run.json
  - run/container+serve:run.json
  - run/python+job:run.json
  - run/python+serve:run.json
summary: Comprehensive reference for Kubernetes compute resources (CPU, memory, GPU, profiles), persistent/ephemeral volume mounts, environment variables, secrets, and service networking in DigitalHub YAML specs.
---

# Kubernetes Compute Resources, Volumes, Secrets & Networking

Every executable DigitalHub Function (`python`, `container`, `*serve`, `kubeai-*`) and its corresponding Task/Run specifications accept a common set of Kubernetes infrastructure properties (`resources`, `profile`, `volumes`, `envs`, `secrets`, `node_selector`, `affinity`, `tolerations`, `replicas`, `service_type`, `service_ports`).

> **Inheritance Rule**: Infrastructure settings declared on a **Function** (`kind: python`, `kind: container`) act as defaults. Any setting declared on a **Run** (`kind: python+job:run`, `kind: container+serve:run`) overrides the Function's default for that specific execution.

---

## 1. Compute Resources (`spec.resources` & `spec.profile`)

### 1.1 Explicit Resource Requests & Limits (`spec.resources`)
`spec.resources` follows the `CoreResource` JSON Schema (`cpu`, `mem`, `gpu`, `disk`). Notice that **`cpu`, `mem`, and `gpu` take an object with `requests` and/or `limits`**, whereas **`disk` (`ephemeral-storage`) takes a direct string or `requests`/`limits` depending on runtime**:

```yaml
spec:
  resources:
    cpu:
      requests: "500m"     # 0.5 vCPU guaranteed
      limits: "2"          # Burst up to 2 vCPUs
    mem:
      requests: "2Gi"      # 2 GiB RAM guaranteed
      limits: "4Gi"        # Hard OOM limit at 4 GiB RAM
    gpu:
      requests: "1"        # Request 1 NVIDIA GPU (nvidia.com/gpu)
      limits: "1"
```

#### Kubernetes Unit Reference
- **CPU (`cpu`)**: Fractional cores (`"0.5"`, `"1"`, `"4"`) or millicores (`"100m"`, `"500m"`, `"2500m"`).
- **Memory (`mem`)**: Binary GiB/MiB (`"512Mi"`, `"2Gi"`, `"16Gi"`, `"64Gi"`). Always prefer binary `Mi`/`Gi` over decimal `M`/`G`.
- **GPU (`gpu`)**: Integer string (`"1"`, `"2"`, `"4"`). Note that Kubernetes does not allow fractional GPU requests without MIG/time-slicing; `requests` and `limits` must be equal.

### 1.2 Hardware Resource Profiles (`spec.profile`)
Many enterprise DigitalHub clusters define pre-configured hardware profiles (e.g., `"1xa100"`, `"2xa100"`, `"cpu-small"`, `"cpu-large"`) that automatically set CPU, memory, GPU limits, `node_selector`, and GPU `tolerations`.

```yaml
spec:
  profile: "1xa100"
```
*(When `spec.profile` is set, the platform controller populates the underlying Kubernetes pod resources and GPU node selectors automatically).*

---

## 2. Storage Volumes (`spec.volumes`)

`spec.volumes` accepts an array of `CoreVolume` objects (`volume_type`, `name`, `mount_path`, `spec`). DigitalHub supports four `volume_type` values:

### 2.1 Persistent Volume Claim (`volume_type: persistent_volume_claim`)
Provisions or mounts a Kubernetes PVC backed by the cluster's block/file storage class (e.g., CephFS, EBS, NFS) that persists across pod restarts.

```yaml
spec:
  volumes:
    - volume_type: persistent_volume_claim
      name: model-cache-pvc
      mount_path: "/mnt/cache"
      spec:
        size: "50Gi"
        access_mode: "ReadWriteOnce"   # Or "ReadWriteMany" if supported by storage class
        storage_class: "standard-rwx"  # Optional: omit to use cluster default StorageClass
```

### 2.2 In-Memory or Scratch EmptyDir (`volume_type: empty_dir`)
Mounts a temporary directory tied to the pod's lifecycle. Crucial for increasing `/dev/shm` shared memory in PyTorch/vLLM/HuggingFace workloads (`medium: "Memory"`):

```yaml
spec:
  volumes:
    - volume_type: empty_dir
      name: dshm
      mount_path: "/dev/shm"
      spec:
        medium: "Memory"
        size_limit: "8Gi"
```

### 2.3 Generic Ephemeral Volume (`volume_type: ephemeral`)
Provisions a CSI-backed volume with dedicated disk capacity that is automatically destroyed when the pod terminates:

```yaml
spec:
  volumes:
    - volume_type: ephemeral
      name: scratch-disk
      mount_path: "/tmp/scratch"
      spec:
        size: "100Gi"
```

### 2.4 Pre-Existing Shared Volume (`volume_type: shared_volume`)
Mounts an administrator-provisioned shared filesystem volume already registered in the project namespace:

```yaml
spec:
  volumes:
    - volume_type: shared_volume
      name: corp-shared-datasets
      mount_path: "/mnt/shared"
```

---

## 3. Environment Variables (`spec.envs`) & Secrets (`spec.secrets`)

### 3.1 Environment Variables (`spec.envs`)
`spec.envs` is a list of `{"name": "<KEY>", "value": "<STRING_VALUE>"}` objects. **Both `name` and `value` must be strings** (wrap numbers or booleans in quotes):

```yaml
spec:
  envs:
    - name: LOG_LEVEL
      value: "INFO"
    - name: MAX_WORKERS
      value: "4"
    - name: OMP_NUM_THREADS
      value: "2"
```

### 3.2 Secrets Injection (`spec.secrets`)
`spec.secrets` is a list of Secret entity names registered in the same project. DigitalHub mounts each secret as an environment variable inside the container with the exact same name:

```yaml
spec:
  secrets:
    - HF_TOKEN
    - POSTGRES_URI
```
*(Never place plaintext passwords, API keys, or tokens inside `spec.envs`; always reference them via `spec.secrets`).*

---

## 4. Service Networking & Scaling (`serve` Actions)

When executing any `serve` Run (`container+serve:run`, `python+serve:run`, `sklearnserve+serve:run`, `mlflowserve+serve:run`, `huggingfaceserve+serve:run`, `kubeai-text+serve:run`), you can configure Kubernetes Service exposure and horizontal scaling:

```yaml
spec:
  replicas: 2
  service_type: "ClusterIP"   # Options: "ClusterIP" (default), "NodePort", "LoadBalancer"
  service_ports:
    - port: 8000              # Port exposed on the Kubernetes Service
      target_port: 8080       # Port the container process listens on internally
```

### Default Internal Target Ports by Runtime
| Runtime Kind | Default Internal Container Port (`target_port`) | Default Service Port (`port`) |
| :--- | :--- | :--- |
| `python` (`python+serve`) | `8080` (Nuclio / DigitalHub HTTP wrapper) | `8080` (or custom via `service_ports`) |
| `sklearnserve`, `mlflowserve`, `huggingfaceserve` | `8080` (KServe / Seldon V2 Open Inference Protocol) | `8080` |
| `kubeai-text`, `kubeai-speech` | `8000` (OpenAI-compatible `/v1/...` API) | `8000` |
| `container` (`container+serve`) | Defined by the container image (e.g., `80`, `8000`, `8501`) | Must match `service_ports` |

---

## 5. Advanced Pod Scheduling (`node_selector`, `tolerations`, `service_account`)

For workloads requiring specific node pools or Kubernetes ServiceAccounts:

```yaml
spec:
  node_selector:
    accelerator: "nvidia-tesla-a100"
  tolerations:
    - key: "nvidia.com/gpu"
      operator: "Exists"
      effect: "NoSchedule"
  runtime_class: "nvidia"
```

