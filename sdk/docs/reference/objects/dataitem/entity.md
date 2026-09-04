# Dataitems

Dataitems are data objects which contain a dataset of a given type, stored in an addressable repository and accessible to every component able to understand the type (kind) and the source (path). Do note that data items could be stored in the artifact store as artifacts, but that is not a dependency or a requirement.

## Choose a dataitem kind

Choose the kind that matches the dataitem you want to create. The `kind` to use is shown at the end of the card description.

<div class="list-cards" markdown>

- [**Dataitem**](./kind/dataitem.md){ .list-card-link } - Store a generic dataitem in an addressable repository - `dataitem`

- [**Table**](./kind/table.md){ .list-card-link } - Work with tabular data as a dataframe - `table`

- [**Croissant**](./kind/croissant.md){ .list-card-link } - Store an ML Croissant dataset - `croissant`

</div>

## Dataitem operations

<div class="grid cards" markdown>

- [**Dataitem CRUD**](./crud.md){ .card-link }

	---

	Create, register, read, update, or delete dataitems.

- [**Use the Dataitem entity**](./methods.md){ .card-link }

	---

	Persist dataitems, move data, and use kind-specific operations.

</div>

[Back to Entities](../index.md)
