---
name: dh-deploy-container-service
description: Package and execute custom container batch jobs (container+job) or long-running HTTP services/web apps (container+serve) on Kubernetes using dhcli.
---

# Skill: Deploying Custom Container Jobs & Services (`kind: container`)

Use this procedural workflow to run any Docker/OCI container image as a one-off Kubernetes Job (`container+job:run`), build an image from a Dockerfile (`container+build:run`), or expose a long-running HTTP microservice/UI (`container+serve:run`).

## Reference Knowledge
- [specs-functions-and-runtimes.md](../../knowledge/cli/specs-functions-and-runtimes.md)
- [kubernetes-resources.md](../../knowledge/management/kubernetes-resources.md)
- [storage-and-services.md](../../knowledge/cli/storage-and-services.md)

---

## Step-by-Step Procedure

### Step 1: Create the `kind: container` Function
Create `container-fn.yaml` defining the container image, default command/args, and environment variables:
```yaml
project: <project-name>
kind: container
name: <function-name>
metadata:
  description: "Custom container workload"
spec:
  image: "<registry>/<repo>:<tag>"
  command: "python"
  args:
    - "-m"
    - "http.server"
    - "8080"
  envs:
    - name: LOG_LEVEL
      value: "INFO"
```
Apply the Function and capture its `id` (`<func-uuid>`):
```bash
dhcli create -f container-fn.yaml -p <project-name>
dhcli get function <function-name> -p <project-name> -o yaml
```

---

### Step 2A: Execute as a Batch Job (`kind: container+job:run`)
If running a batch process that exits upon completion, create `container-job-run.yaml`:
```yaml
project: <project-name>
kind: container+job:run
spec:
  function: "container://<project-name>/<function-name>:<func-uuid>"
  resources:
    cpu:
      requests: "500m"
      limits: "2"
    mem:
      requests: "1Gi"
      limits: "2Gi"
```
Execute and monitor:
```bash
dhcli execute -f container-job-run.yaml -p <project-name>
dhcli get run <run-uuid> -p <project-name> -o yaml
dhcli log <run-uuid> -p <project-name>
```

---

### Step 2B: Deploy as a Long-Running HTTP Service (`kind: container+serve:run`)
If exposing an HTTP API or web application (FastAPI, Streamlit, Gradio, NGINX), create `container-serve-run.yaml` with `service_ports`:
```yaml
project: <project-name>
kind: container+serve:run
spec:
  function: "container://<project-name>/<function-name>:<func-uuid>"
  replicas: 1
  service_type: "ClusterIP"
  service_ports:
    - port: 8000
      target_port: 8080
  resources:
    cpu:
      requests: "500m"
      limits: "1"
    mem:
      requests: "1Gi"
      limits: "2Gi"
```
Execute the deployment:
```bash
dhcli execute -f container-serve-run.yaml -p <project-name>
```

### Step 3: Verify Service Endpoint & Test Locally
1. Poll the Run until `status.state` is `RUNNING` and `status.service.url` is populated:
   ```bash
   dhcli get run <serve-run-uuid> -p <project-name> -o yaml
   ```
2. Open a local port-forward tunnel to test the service from your machine:
   ```bash
   dhcli http <serve-run-uuid> -p <project-name> --port 9000
   ```

