# DBT

Use DBT to run SQL transformations against project data. The `transform` action maps input Dataitems to dbt `ref()` calls and publishes the result as a table Dataitem.

## Prerequisites

- Python >= 3.10, < 3.15.
- Install `digitalhub-runtime-dbt` using the [installation instructions](../../../how-to/installation.md#dbt).

## Actions

<div class="list-cards" markdown>

- [**Transform**](dbt-transform/action.md){ .list-card-link }

    Run a dbt transformation and create a table Dataitem.

</div>

## Examples

<div class="list-cards" markdown>

- [**DBT examples**](examples.md){ .list-card-link }

    Explore complete examples for DBT transformations.

</div>
