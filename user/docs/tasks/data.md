# Data and transformations

The platform supports data of different type to be stored and operated by the underlying storage subsystems. 

Digital Hub natively supports two types of storages: 

- *persistence* object storage (datalake S3 Minio), which manages immutable data in the form of files. 
-  *operational* relational data storage (PostgreSQL database), which is used for efficient querying of mutable data. *Postgres* 
   is rich with extensions, most notably for geo-spatial and time-series data.

The data is represented in the platform as entities of different types, depending on its usage and format. More specifically, we distinguish

- *data items* which represent immutable tabular datasets resulting from different transformation operations and ready for use in differerent types of analysis. Data items are enriched with metadata (e.g., versions, lineage, stats, profiling, schema) and unique keys and managed and persisted to the datalake directly by the platform in the form of Apache Parquet files.
- *artifacts* which represent arbitrary files stored to the datalake with some extra metadata, but are not limited to tabular formats.

Each data entity may be accessed and manipulated by the platform via UI or using the API, e.g., with SDK.

## Manipulating data via UI
TODO

## Manipulating data via SDK
TODO
