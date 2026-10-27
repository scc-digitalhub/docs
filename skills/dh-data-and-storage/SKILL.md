---
name: dh-data-and-storage
description: Upload, register, download, and inspect DigitalHub Dataitems (table, dataitem, croissant), Artifacts, and Models using dhcli and Core JSON Schemas.
---

# Skill: Data, Artifact & Model Storage Management

Use this procedural workflow whenever ingesting local files into DigitalHub S3 storage, registering external `s3://` / `http://` / `sql://` datasets, downloading artifacts/models locally, or retrieving `store://` URIs for downstream Function Runs.

## Reference Knowledge
- [storage-and-services.md](../../knowledge/cli/storage-and-services.md)
- [specs-data-and-storage.md](../../knowledge/cli/specs-data-and-storage.md)
- [keys-and-lifecycle.md](../../knowledge/management/keys-and-lifecycle.md)

---

## Step-by-Step Procedure

### Scenario A: Uploading Local Files or Directories to S3 (`dhcli upload`)
When the file or directory is on the local filesystem and needs to be uploaded to the project's default S3 store:

1. **Choose the Entity Resource and Kind**:
   - Structured CSV/Parquet dataset -> `dataitem` (`-k table`)
   - Unstructured dataset -> `dataitem` (`-k dataitem`)
   - Code archive / report / config -> `artifact` (`-k artifact`)
   - Trained model weights -> `model` (`-k sklearn`, `-k mlflow`, `-k huggingface`, or `-k model`)
2. **Execute `dhcli upload`**:
   ```bash
   # Example: Upload a local Parquet file as a tabular Dataitem
   dhcli upload dataitem <entity-name> -k table -p <project-name> -i ./data/dataset.parquet
   ```
3. **Verify `READY` State and Capture the `store://` Key**:
   ```bash
   dhcli get dataitem <entity-name> -p <project-name> -o yaml
   ```
   Confirm `status.state: READY` and copy the `key` field (`store://<project>/dataitem/table/<entity-name>:<uuid>`) to pass into downstream `spec.inputs`.

---

### Scenario B: Registering an Existing Remote Dataset or Model (`dhcli register`)
When the dataset or model already resides in S3 (`s3://...`), HTTP (`https://...`), HuggingFace (`huggingface://...`), or SQL (`sql://...`) and you want to catalog it without re-uploading bytes:

1. **Author the YAML Manifest (`register-entity.yaml`)**:
   ```yaml
   project: <project-name>
   kind: table
   name: <entity-name>
   metadata:
     description: "External Parquet table registered in DigitalHub"
     labels:
       - tier:bronze
   spec:
     path: "s3://bucket-name/path/to/data.parquet"
     schema:
       fields:
         - name: id
           type: string
         - name: value
           type: number
   ```
2. **Register the Manifest**:
   ```bash
   dhcli register -f register-entity.yaml -p <project-name>
   ```
3. **Verify Registration**:
   ```bash
   dhcli get dataitem <entity-name> -p <project-name> -o yaml
   ```

---

### Scenario C: Downloading a Remote Entity to Local Disk (`dhcli download`)
To inspect or consume an Artifact, Dataitem, or Model on the local machine:

```bash
# Download the latest version
dhcli download dataitem <entity-name> -p <project-name> -d ./local-output/

# Download a specific version by UUID
dhcli download model <model-name> --id <uuid> -p <project-name> -d ./local-model/
```

