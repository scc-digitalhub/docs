---
id: cli-storage-and-services
domain: cli
type: operational_guide
version: "0.16"
tags: [cli, dhcli, upload, download, s3, services, port-forward, proxy, artifact, model, dataitem]
commands:
  - dhcli upload
  - dhcli download
  - dhcli services
  - dhcli port-forward
  - dhcli proxy
summary: "Uploading and downloading artifacts, models, and dataitems to/from S3 via `dhcli upload` and `dhcli download`, listing active cluster services (`dhcli services`), and tunneling traffic via `port-forward` and `proxy`."
---

# CLI File Upload/Download & Service Networking (Port-Forward & Proxy)

`dhcli` provides built-in S3 data transfer (`upload` and `download`) as well as authenticated Kubernetes service tunneling (`services`, `port-forward`, and `proxy`) so local applications and browsers can interact with cluster workloads without complex VPN or ingress setups.

---

## 1. Uploading Local Files & Directories to S3 (`dhcli upload`)

`dhcli upload` transfers a local file or folder directly to the project's S3 datalake bucket (`s3://datalake/<project>/<resource>/<name>/<id>/...`) and automatically creates (or updates) the catalog metadata entry in DigitalHub Core.

### 1.1 Command Syntax
```bash
dhcli upload -p <project> -n <name> -f <local_file_or_dir> [-v] <resource> [id]
```

| Parameter / Flag | Required | Description |
| :--- | :---: | :--- |
| `-p, --project <project>` | Yes | Target project name. |
| `-n, --name <name>` | Cond. | Entity name (mandatory when creating a new resource; omit if updating an existing `[id]`). |
| `-f, --file <path>` | Yes | Local path to the file or directory to upload. |
| `-v, --verbose` | No | Show upload progress bar and multipart transfer details. |
| `<resource>` | Yes | Target resource type: `artifact` (`artifacts`), `model` (`models`), or `dataitem` (`dataitems`). |
| `[id]` | No | Optional existing entity UUID to upload payload into an existing version. |

### 1.2 Upload Examples
```bash
# Upload a single CSV file as a new artifact named 'raw-sales'
dhcli upload -p my-project -n raw-sales -f ./data/sales.csv artifact

# Upload an entire directory of model weights as a new model named 'bert-finetuned'
dhcli upload -p my-project -n bert-finetuned -f ./checkpoints/bert_dir model

# Upload a Parquet dataset as a dataitem
dhcli upload -p my-project -n customer-features -f ./features.parquet dataitem
```

---

## 2. Downloading Entities from S3 to Local Disk (`dhcli download`)

`dhcli download` reads the `spec.path` (`s3://...`) from the catalog entry and downloads the file or folder from the S3 datalake to your local filesystem.

### 2.1 Command Syntax
```bash
dhcli download -p <project> (-n <name> | <id>) [-d <destination_path>] [-o short|json|yaml] [-v] <resource>
```

### 2.2 Download Examples
```bash
# Download the latest version of an artifact by name (-n) into ./downloads/
dhcli download -p my-project -n raw-sales -d ./downloads artifact

# Download a specific version of a model by its UUID (<id>)
dhcli download -p my-project -d ./local_model model 4f8a2c10fee5454b98977ee4c19741dd
```

---

## 3. Discovering Active Cluster Services (`dhcli services`)

Functions executed with a `serve` task (`python+serve`, `container+serve`, `sklearnserve+serve`, `vllmserve-text+serve`, `kubeai-text+serve`, etc.) run as Kubernetes Services inside the cluster perimeter. Use `dhcli services` to list them:

```bash
# List all RUNNING services in a project (table view)
dhcli services -p my-project

# List all services in JSON format (includes internal cluster URL under status.service.url)
dhcli services -p my-project -o json

# Filter services by function kind (-k) or state (-s)
dhcli services -p my-project -k "vllmserve-text+serve:run" -s RUNNING -o json
```

---

## 4. Accessing Cluster Services Locally (`port-forward` vs. `proxy`)

Because cluster services are isolated inside the platform network by default, `dhcli` provides two commands to reach them from your local machine:

| Feature | `dhcli port-forward` | `dhcli proxy` |
| :--- | :--- | :--- |
| **Target Use Case** | Programmatic API access (`curl`, Python `requests`, OpenAI SDK, Postman). | Interactive browser UIs (Streamlit, Gradio, Marimo, FastAPI `/docs`, dashboards). |
| **How It Works** | Opens a persistent localhost TCP tunnel (`localhost:<port>`) that forwards all traffic through the platform proxy with automatic auth headers. | Starts a one-shot localhost bootstrap page, opens the default web browser, and authenticates a direct browser session (supports WebSockets, SSE, cookies). |
| **Process Lifecycle** | Long-running foreground process (keep running in background while making API calls). | Exits or stays lightweight once browser session is bootstrapped. |

### 4.1 `dhcli port-forward` Syntax & Examples
You can target the service by **run ID** (`<run-id>`), by **function name** (`-f <fn-name>`, which automatically resolves the newest `RUNNING` serve run of that function), or by **run name** (`-n <run-name>`):

```bash
# Forward local port 8000 to the latest RUNNING service of function 'llama3-instruct'
dhcli port-forward -p my-project -f llama3-instruct -l 8000

# Forward a random available local port to a specific serve run ID
dhcli port-forward -p my-project 7a2f5b50fee5454b98977ee4c19741dd
```
Once `✔ Port-forward listening on localhost:8000` is active, any local client can call `http://localhost:8000/v1/chat/completions` without needing bearer tokens!

### 4.2 `dhcli proxy` Syntax & Examples
```bash
# Open an authenticated browser session to the web UI served by function 'gradio-app'
dhcli proxy -p my-project --function gradio-app
```

