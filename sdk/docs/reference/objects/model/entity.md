# Models

Models are the representation of machine learning models stored as files in the artifact store.

## Choose a model kind

Choose the kind that matches the model you want to create. The `kind` to use is shown at the end of the card description.

<div class="kind-cards" markdown>

- [**Model**](./kind/model.md){ .kind-card-link } - Store a generic machine learning model - `model`

- [**MLflow**](./kind/mlflow.md){ .kind-card-link } - Store an MLflow model with its metadata - `mlflow`

- [**Scikit-learn**](./kind/sklearn.md){ .kind-card-link } - Store a scikit-learn model - `sklearn`

- [**Hugging Face**](./kind/huggingface.md){ .kind-card-link } - Store a Hugging Face model or repository - `huggingface`

- [**TVM IR**](./kind/tvm-ir.md){ .kind-card-link } - Store a Relax IR model produced by TVM - `tvm-ir`

- [**TVM SO**](./kind/tvm-so.md){ .kind-card-link } - Store a compiled TVM shared-object model - `tvm-so`

</div>

## Managing models with SDK

Models can be created and managed as *entities* with the SDK CRUD methods. This can be done directly from the package or through the `Project` object.

1. In the [CRUD section](./crud.md), we will see how to create, read, update and delete models.
2. In the [methods section](./methods.md), we will see what can be done with the `Model` object.

## Model operations

<div class="grid cards" markdown>

- [**Model CRUD**](./crud.md){ .card-link }

	---

	Create, register, read, update, or delete models.

- [**Use the Model entity**](./methods.md){ .card-link }

	---

	Persist models, move model files, and log metrics.

</div>

[Back to Entities](../index.md)
