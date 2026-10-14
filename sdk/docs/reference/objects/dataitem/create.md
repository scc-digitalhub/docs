---
render_macros: true
---

# Create a dataitem

Choose the creation method based on where the source is and whether you want to upload it.

## Choose a creation method

- **Log with `log_<kind>()`** creates an entity and uploads a local source to a dataitem store.
- **Register with `register_<kind>()`** creates an entity for a source that already exists in a store.
- **Create with `new_dataitem()`** creates an entity from an explicit kind and path without uploading a source. Each kind page below includes an example with its corresponding kind.

The creation functions are part of the SDK. Kind-specific features may need optional dependencies: `table` uses `pandas` by default (or `polars`), and `croissant` requires `mlcroissant`. See the [SDK installation guide](../../../how-to/installation.md).

## Choose a dataitem kind

The kind references document the corresponding `log_<kind>()` and `register_<kind>()` functions.

<div class="list-cards" markdown>

- [**Dataitem**](./kind/dataitem.md){ .list-card-link } - Store a generic dataset in an addressable repository - `dataitem`

- [**Table**](./kind/table.md){ .list-card-link } - Work with tabular data as a dataframe - `table`

- [**Croissant**](./kind/croissant.md){ .list-card-link } - Store and load an ML Croissant dataset - `croissant`

</div>

[Back to Dataitems](./entity.md)
