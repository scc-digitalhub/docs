---
render_macros: true
---

# Python runtime

The Python runtime executes user-defined Python handlers for general-purpose jobs and services.

{{ runtime_prerequisites("digitalhub-runtime-python", "../../../../how-to/installation.md") }}

## Supported Python versions

The package requires Python >= 3.10 and < 3.15. Functions can execute with `PYTHON3_10`, `PYTHON3_11`, `PYTHON3_12`, or `PYTHON3_13`.

{{ runtime_actions([
    ("Job", "python-job/action.md", "Execute a Python handler as a one-off task."),
    ("Serve", "python-serve/action.md", "Deploy a Python handler as an HTTP service."),
    ("Build", "python-build/action.md", "Build a container image for a Python function."),
]) }}

## Local and remote execution

Set `local_execution=True` on a Job run to execute on the local machine; dependencies must already be installed there. By default, jobs run remotely on a server or cluster managed by the platform. Serving functions are available only with remote execution.

## Requirements and automatic builds

The `requirements` function parameter accepts requirement strings or a path to `requirements.txt`, `setup.py`, `pyproject.toml`, `conda.yml`, or `conda.yaml`. The SDK parses and normalizes these files: `requirements.txt` and `setup.py` as pip requirements, `pyproject.toml` from `project.dependencies`, and Conda files from `dependencies.pip`.

If a package has no version, the SDK looks for it in the active local virtual environment, adds the installed version when available, and logs a warning. Use an explicit constraint or pin a version for reproducible builds.

For remote Job and Serve runs, requirements must be installed in the execution image. `auto_build` defaults to `False`; set it to `True` to build automatically when no image is configured, or call `function.build()` explicitly. An existing image is not rebuilt automatically when requirements change.

{{ runtime_examples("Explore examples for Python jobs, services and builds.") }}
