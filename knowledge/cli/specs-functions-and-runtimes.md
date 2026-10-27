---
id: cli-specs-functions-and-runtimes
domain: cli
type: runtime_specification
version: "0.16"
tags:
  [
    cli,
    dhcli,
    yaml,
    schema,
    function,
    run,
    task,
    python,
    container,
    modelserve,
    sklearnserve,
    mlflowserve,
    huggingfaceserve,
    vllmserve,
    kubeai,
    dbt,
    guardrail,
    openinference,
    flower,
  ]
commands:
  - dhcli create
  - dhcli run
  - dhcli get
  - dhcli list
  - dhcli log
schemas:
  - function/python.json
  - function/container.json
  - function/sklearnserve.json
  - function/mlflowserve.json
  - function/huggingfaceserve.json
  - function/vllmserve-text.json
  - function/vllmserve-speech.json
  - function/vllmserve-pooling.json
  - function/kubeai-text.json
  - function/kubeai-speech.json
  - function/dbt.json
  - function/guardrail.json
  - function/openinference.json
  - function/flower-app.json
  - function/flower-server.json
  - function/flower-client.json
  - run/python+job:run.json
  - run/python+serve:run.json
  - run/python+build:run.json
  - run/container+job:run.json
  - run/container+serve:run.json
  - run/container+build:run.json
summary: "Authoritative CLI YAML specifications (aligned with Core JSON Schemas) for creating and executing Functions across Python, Container, ModelServe (Sklearn, MLflow, HuggingFace, vLLM, KubeAI), DBT, Guardrail, OpenInference, and Flower runtimes."
---

# CLI YAML Specifications: Functions & Runtimes

This guide provides the exact **Core JSON Schema-aligned YAML structures** required by `dhcli create -f <function.yaml> functions` and `dhcli run -p <project> -n <fn-name> -f <run.yaml> <task>`.

> **CRITICAL SCHEMA RULE FOR AGENTS**:
> The YAML `spec` accepted by `dhcli create -f` follows the **DigitalHub Core REST Schema**, which differs from the flattened kwargs of the Python SDK (`dh.new_function`). For example, in `kind: python`, source code fields (`handler`, `base64`, `source`, `lang`, `init_function`) MUST be nested inside **`spec.source`**, NOT placed at the top level of `spec`.

---

## 1. Master Matrix of Function Kinds & CLI Run Tasks

When executing a function via `dhcli run -p <project> -n <fn-name> [-f <run.yaml>] <task>`, the `<task>` argument is always formatted as **`<kind>+<action>`**:

| Runtime Family | Function `kind` | Supported `<task>` Values for `dhcli run` | Primary Purpose |
| :--- | :--- | :--- | :--- |
| **Python** | `python` | `python+build`, `python+job`, `python+serve` | General-purpose Python batch jobs and Nuclio serverless HTTP endpoints. |
| **Container** | `container` | `container+build`, `container+job`, `container+serve`, `container+deploy` | Arbitrary Docker image execution (batch jobs, custom web UIs, microservices). |
| **ModelServe (Classical/ML)** | `sklearnserve` | `sklearnserve+serve` | Serve `.pkl`/`.joblib` Scikit-Learn models via KServe OpenInference v2. |
| **ModelServe (MLflow)** | `mlflowserve` | `mlflowserve+build`, `mlflowserve+serve` | Serve MLflow-logged models via KServe OpenInference v2. |
| **ModelServe (HuggingFace)** | `huggingfaceserve` | `huggingfaceserve+serve` | Serve HuggingFace Transformer/PyTorch models via KServe. |
| **ModelServe (vLLM)** | `vllmserve-text`<br>`vllmserve-speech`<br>`vllmserve-pooling` | `vllmserve-text+serve`<br>`vllmserve-speech+serve`<br>`vllmserve-pooling+serve` | High-throughput GPU serving for LLMs, ASR/speech, and embeddings via vLLM (OpenAI-compatible API). |
| **ModelServe (KubeAI)** | `kubeai-text`<br>`kubeai-speech` | `kubeai-text+serve`<br>`kubeai-speech+serve` | Autoscaled LLM and speech model serving on KubeAI (OpenAI-compatible API). |
| **DBT** | `dbt` | `dbt+transform` | SQL data transformation over tabular DataItems stored in PostgreSQL/Dremio. |
| **Guardrail** | `guardrail` | `guardrail+build`, `guardrail+serve` | LLM input/output safety guardrail validation service. |
| **OpenInference** | `openinference` | `openinference+build`, `openinference+serve` | Custom Python inference handler implementing the OpenInference v2 protocol. |
| **Flower (Federated Learning)**| `flower-app`<br>`flower-server`<br>`flower-client` | `flower-app+train`<br>`flower-server+build`, `flower-server+deploy`<br>`flower-client+build`, `flower-client+deploy` | Federated learning training apps, SuperLink servers, and SuperNode clients. |

---

## 2. Python Runtime (`kind: python`)

### 2.1 Function YAML Specification (`schemas/specs/function/python.json`)

**Required `spec` fields**: `python_version`, `source`.

| Field Path | Type | Required | Allowed Values / Description |
| :--- | :--- | :---: | :--- |
| `spec.python_version` | `string` (enum) | Yes | `PYTHON3_10`, `PYTHON3_11`, `PYTHON3_12`, `PYTHON3_13` |
| `spec.source` | `object` | Yes | Container for handler code configuration (`PythonSourceCode`). |
| `spec.source.handler` | `string` | Yes | Entrypoint function name (e.g. `main` for inline/local, or `pkg.mod:fn` for git/zip). |
| `spec.source.lang` | `string` (enum) | No | Default: `"python"`. |
| `spec.source.base64` | `string` | Cond. | Base64-encoded Python script (`base64 -i handler.py \| tr -d '\n'`). Required if `source` URI is not set. |
| `spec.source.source` | `string` | Cond. | Remote source URI (`git+https://...`, `s3://...`, `zip+s3://...`, `https://...`). |
| `spec.source.init_function` | `string` | No | Optional initialization function name (e.g. `init`) called once on remote container startup. |
| `spec.requirements` | `array[string]` | No | List of pip requirement specifiers (e.g. `["pandas>=2.0", "scikit-learn==1.3.0"]`). |
| `spec.image` | `string` | No | Pre-built container image (`repo/image:tag`). Populated automatically after `python+build`. |
| `spec.base_image` | `string` | No | Custom base container image used when building. |

**Example `function-python.yaml`**:
```yaml
kind: python
name: iris-classifier
project: my-project
metadata:
  name: iris-classifier
  description: "Trains a classifier on the Iris dataset"
  labels:
    - ml
    - python
spec:
  python_version: PYTHON3_10
  requirements:
    - "pandas"
    - "scikit-learn"
  source:
    lang: python
    handler: train_model
    base64: "ZGVmIHRyYWluX21vZGVsKHByb2plY3QsIHJ1biwgZGF0YWl0ZW0sIHRocmVzaG9sZD0wLjUpOgogICAgZGYgPSBkYXRhaXRlbS5hc19kZigpCiAgICBydW4ubG9nX21ldHJpYygiYWNjdXJhY3kiLCAwLjk1KQogICAgcmV0dXJuIHsic3RhdHVzIjogIm9rIn0K"
```

```bash
dhcli create -p my-project -f function-python.yaml functions
```

### 2.2 Python Run YAML Specifications (`python+build`, `python+job`, `python+serve`)

When calling `dhcli run -p <project> -n <fn-name> -f <run.yaml> <task>`, `dhcli` reads the `spec` block from `<run.yaml>` and automatically injects `spec.task` and `spec.function`.

| Field Path in `run.yaml` | Applies To | Type | Description |
| :--- | :--- | :--- | :--- |
| `spec.inputs` | `job`, `serve` | `map[string, string]` | Map of handler argument names to platform entity keys (`store://<project>/<entity>/<kind>/<name>:<id>`). |
| `spec.parameters` | `job`, `serve` | `map[string, any]` | Map of handler argument names to primitive JSON values (numbers, strings, booleans, lists, dicts). |
| `spec.init_parameters` | `job`, `serve` | `map[string, any]` | Parameters passed to `init_function` on startup. |
| `spec.local_execution` | `job` | `boolean` | Default `false`. Set `false` for Kubernetes execution. |
| `spec.instructions` | `build` | `array[string]` | Additional Dockerfile `RUN` shell commands (e.g. `["apt-get update && apt-get install -y git"]`). |
| `spec.replicas` | `serve` | `integer` | Number of Nuclio HTTP pod replicas (e.g. `1` or `2`). |
| `spec.service_type` | `serve` | `string` (enum) | `ClusterIP` (default), `NodePort`, `LoadBalancer`, `ExternalName`. |
| `spec.service_ports` | `serve` | `array[object]` | List of `{"port": 8080, "target_port": 8080}`. |
| `spec.resources` | all | `object` | Hardware requests: `{"cpu": "2", "mem": "4Gi", "gpu": "1", "disk": "10Gi"}`. |
| `spec.profile` | all | `string` | Hardware profile template name (e.g. `"1xa100"`). |
| `spec.envs` | all | `array[object]` | Environment variables: `[{"name": "MY_VAR", "value": "val"}]`. |
| `spec.secrets` | all | `array[string]` | List of project Secret names to mount: `["my-db-secret"]`. |
| `spec.volumes` | all | `array[object]` | List of `CoreVolume` mounts (`volume_type`, `name`, `mount_path`, `spec`). |

**Example: Build Run (`run-build.yaml`) & Execution**:
```yaml
kind: python+build:run
project: my-project
spec:
  instructions:
    - "apt-get update && apt-get install -y libgomp1"
```
```bash
dhcli run -p my-project -n iris-classifier -f run-build.yaml python+build
```

**Example: Job Run (`run-job.yaml`) & Execution**:
```yaml
kind: python+job:run
project: my-project
spec:
  inputs:
    dataitem: "store://my-project/dataitem/table/iris-data:latest"
  parameters:
    threshold: 0.5
  resources:
    cpu: "1"
    mem: "2Gi"
```
```bash
dhcli run -p my-project -n iris-classifier -f run-job.yaml python+job
```

---

## 3. Container Runtime (`kind: container`)

### 3.1 Function YAML Specification (`schemas/specs/function/container.json`)

**Required `spec` fields**: `image`.

| Field Path | Type | Required | Description |
| :--- | :--- | :---: | :--- |
| `spec.image` | `string` | Yes | Target container image (`nginx:latest`, `python:3.11-slim`, or target tag to be built). |
| `spec.base_image` | `string` | No | Base image for `container+build` when building from a source archive/Dockerfile. |
| `spec.command` | `string` | No | Container entrypoint command (e.g. `"/bin/sh"` or `"python"`). |
| `spec.args` | `array[string]` | No | Command-line arguments (e.g. `["-c", "python app.py --port 8080"]`). |
| `spec.image_pull_policy` | `string` (enum) | No | `IfNotPresent`, `Always`, `Never`. |
| `spec.source` | `object` | No | Source archive/repo (`source`, `base64`, `lang`) mounted or built into the container. |

**Example `function-container.yaml` & `run-container-serve.yaml`**:
```yaml
# function-container.yaml
kind: container
name: streamlit-dashboard
project: my-project
spec:
  image: "python:3.11-slim"
  command: "/bin/sh"
  args:
    - "-c"
    - "pip install streamlit && streamlit run app.py --server.port 8501"
```
```yaml
# run-container-serve.yaml
kind: container+serve:run
project: my-project
spec:
  replicas: 1
  service_type: ClusterIP
  service_ports:
    - port: 8501
      target_port: 8501
  resources:
    cpu: "1"
    mem: "2Gi"
```
```bash
dhcli create -p my-project -f function-container.yaml functions
dhcli run -p my-project -n streamlit-dashboard -f run-container-serve.yaml container+serve
```

---

## 4. ModelServe & LLM Runtimes (`vllmserve-*`, `kubeai-*`, `sklearnserve`, `mlflowserve`, `huggingfaceserve`)

### 4.1 Classical & Transformer Model Serving (`sklearnserve`, `mlflowserve`, `huggingfaceserve`)

| Kind | Required `spec` Fields | Key Optional `spec` Fields | Run Task |
| :--- | :--- | :--- | :--- |
| **`sklearnserve`** | *(none required at fn level; `path` set in fn or run)* | `path` (`store://.../model/sklearn/...` or `s3://...`), `image`, `model_name` | `sklearnserve+serve` |
| **`mlflowserve`** | *(none required at fn level)* | `path` (`store://.../model/mlflow/...`), `image`, `model_name`, `requirements` | `mlflowserve+build`<br>`mlflowserve+serve` |
| **`huggingfaceserve`** | `path` | `path` (`huggingface://...` or `store://.../model/huggingface/...`), `model_name`, `adapters`, `args`, `backend`, `dtype`, `max_length`, ` huggingface_token` (secret ref) | `huggingfaceserve+serve` |

**Example `function-sklearnserve.yaml`**:
```yaml
kind: sklearnserve
name: churn-predictor
project: my-project
spec:
  model_name: churn-model
  path: "store://my-project/model/sklearn/churn-model:latest"
```
```bash
dhcli create -p my-project -f function-sklearnserve.yaml functions
dhcli run -p my-project -n churn-predictor sklearnserve+serve
```

### 4.2 LLM & Speech Serving (`vllmserve-*` and `kubeai-*`)

| Kind | Schema `spec` Fields | Run Task |
| :--- | :--- | :--- |
| **`vllmserve-text`**<br>**`vllmserve-speech`**<br>**`vllmserve-pooling`** | • `model_name` (`string`): Model alias exposed in OpenAI API<br>• `path` (`string`): `huggingface://org/model` or `store://...` or `s3://...`<br>• `image` (`string`, optional): Custom vLLM image<br>• `adapters` (`array[object]`, optional): LoRA adapters | `vllmserve-text+serve`<br>`vllmserve-speech+serve`<br>`vllmserve-pooling+serve` |
| **`kubeai-text`**<br>**`kubeai-speech`** | • `model_name` (`string`): Exposed model name<br>• `url` (`string`): `hf://org/model` or `ollama://...` or `store://...`<br>• `engine` (`string` enum): `VLLM`, `OLlama`, `FasterWhisper`, `Infinity`<br>• `features` (`array[string]`): `["TextGeneration"]`, `["TextEmbedding"]`, `["SpeechToText"]`<br>• `adapters`, `files` (optional) | `kubeai-text+serve`<br>`kubeai-speech+serve` |

**Example `function-vllm.yaml` + GPU Serve Run (`run-vllm.yaml`)**:
```yaml
# function-vllm.yaml
kind: vllmserve-text
name: llama3-instruct
project: my-project
spec:
  model_name: llama3
  path: "huggingface://meta-llama/Meta-Llama-3-8B-Instruct"
```
```yaml
# run-vllm.yaml
kind: vllmserve-text+serve:run
project: my-project
spec:
  args:
    - "--max-model-len=4096"
    - "--gpu-memory-utilization=0.9"
  resources:
    cpu: "4"
    mem: "16Gi"
    gpu: "1"
```
```bash
dhcli create -p my-project -f function-vllm.yaml functions
dhcli run -p my-project -n llama3-instruct -f run-vllm.yaml vllmserve-text+serve
```

---

## 5. DBT Transformation Runtime (`kind: dbt`)

### 5.1 Function & Run YAML Specification (`schemas/specs/function/dbt.json` & `run/dbt+transform:run.json`)

- **Function `spec` (`kind: dbt`)**:
  - `spec.sql` (`string`, **required**): The SQL `SELECT` transformation query (can reference input tables via Jinja `{{ ref('input_tab') }}`).
- **Run `spec` (`task: dbt+transform`)**:
  - `spec.inputs` (`map[string, string]`, **required**): Map of table aliases referenced in `{{ ref(...) }}` to tabular DataItem keys (`store://.../dataitem/table/...`).
  - `spec.outputs` (`map[string, string]`, **required**): Map defining output table names to persist as new `table` DataItems.

```yaml
# function-dbt.yaml
kind: dbt
name: filter-active-users
project: my-project
spec:
  sql: "SELECT user_id, email FROM {{ ref('raw_users') }} WHERE active = true"
```
```yaml
# run-dbt.yaml
kind: dbt+transform:run
project: my-project
spec:
  inputs:
    raw_users: "store://my-project/dataitem/table/users-raw:latest"
  outputs:
    output_table: "users-active"
```
```bash
dhcli create -p my-project -f function-dbt.yaml functions
dhcli run -p my-project -n filter-active-users -f run-dbt.yaml dbt+transform
```
