# DBT Runtime

The DBT runtime lets you run [dbt](https://www.getdbt.com/) transformations against your data. It wraps the DBT CLI and exposes a Function of kind `dbt` and a Task action for transformations.

## Prerequisites

**Supported Python versions:**

- Python ≥ 3.10, < 3.15

**Required packages:**

- `digitalhub-runtime-dbt`

Install from PyPI:

```bash
pip install digitalhub-runtime-dbt
```

For local execution:

```bash
pip install digitalhub-runtime-dbt[local]
```

## Usage overview

To execute dbt transformations on the platform:

1. Implement your dbt project/code.
2. Create a `Function` resource that references your dbt code and declares inputs/outputs.
3. Call `function.run()` to execute the transformation.

See [how to](how-to.md) for detailed instructions on executing dbt transformations.
See [Examples](examples.md) for code samples.
