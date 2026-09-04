# Data and artifacts

Use a [Dataitem](../reference/objects/dataitem/entity.md) when the object is a typed dataset that should be understood by data-aware components (e.g. a pandas dataframe). Use an [Artifact](../reference/objects/artifact/entity.md) when you need to store and move a file or another binary object.

```mermaid
flowchart LR
    input["Data or file"] --> decision{"What are you managing?"}
    decision -->|Typed dataset| dataitem["Dataitem"]
    decision -->|File or binary object| artifact["Artifact"]
```

| | Dataitem | Artifact |
| --- | --- | --- |
| Represents | A typed dataset | A file or binary object |
| Choose it when | The data kind and dataset semantics matter | File storage and transfer are the primary concerns |
| Supported kinds | `table`, `croissant`, `dataitem` | `artifact` |
| Typical operations | Load data with kind-specific methods, upload, download, represent as dataframe | Upload, download, and access as a file |
