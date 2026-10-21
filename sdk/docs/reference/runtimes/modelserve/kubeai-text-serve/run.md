---
render_macros: true
---

# Run a KubeAI Text Function

Call `function.run(action="serve", ...)` to deploy the KubeAI text model. Configure the function and service with the following parameters.

## Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| action | str | ✓ | Action to execute. Must be `serve` |
| [envs](../../../configuration/kubernetes.md#secrets-and-envs) | list[dict] | | Environment variables. |
| [secrets](../../../configuration/kubernetes.md#secrets-and-envs) | list[str] | | List of secret names. |
| [profile](../../../configuration/kubernetes.md#profile) | str | | Profile template. |
| env | dict | | Environment variables for the serving function. |
| args | list[str] | | Arguments. |
| cache_profile | str | | Cache profile. |
| [files](#files) | list[KubeaiFile] | | Files to make available to the model. |
| [scaling](#scaling) | Scaling | | Scaling parameters. |
| processors | int | | Number of processors. |

## Files

Files are a list of dictionaries with `path` and `content` keys:

```python
files = [
    {
        "path": "file-path",
        "content": "file-content"
    }
]
```

## Scaling

`scaling` configures replica counts, autoscaling and load balancing:

```python
scaling = {
    "replicas": int,
    "min_replicas": int,
    "max_replicas": int,
    "autoscaling_disabled": bool,
    "target_request": int,
    "scale_down_delay_seconds": int,
    "load_balancing": {
        "strategy": str,  # "LeastLoad" or "PrefixHash"
        "prefix_hash": {
            "mean_load_factor": int,
            "replication": int,
            "prefix_char_length": int
        }
    }
}
```

## Example

```python
run = function.run(
    action="serve",
    processors=1
)
```

{{ page_navigation(("Create", "create.md"), ("Use", "use.md")) }}
