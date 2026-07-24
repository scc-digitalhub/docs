# Code source — Git repository

Use a Git repository as a code source by prefixing the URL with `git+`.
This points the runtime to a remote repository that will be cloned at execution time.

## Quick checklist

- Prefix the URL with `git+` (required).
- Provide a `handler` that points to the module and callable (e.g. `pkg.module:func`).
- Set [authentication](#credentials) env vars or create secrets before creating the function (token recommended) to access private repos.

## Format

- `git+https://github.com/user/repo(#branch-or-tag-or-commit)`

The `(#branch-or-tag-or-commit)` and will be used to checkout the specific reference after cloning.

## Behavior

- The runtime clones the repository at run/build time.
- After cloning, it imports the module/file indicated by the `handler`.
- The `handler` typically follows `module.submodule:function` or `path.to.file:callable` syntax depending on the runtime.

## Examples

```python
# Git repository (specific branch)
func = dh.new_function(
    name='worker',
    kind='python',
    code_src='git+https://github.com/my/repo#main',
    handler='src.app:handler',
)
```

## Credentials

To read Git private repositories, the runtime needs appropriate permissions.
Check the [Git credential section](../credentials/git.md) for details on configuring access.
