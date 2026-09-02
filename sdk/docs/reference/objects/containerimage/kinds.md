# Container image kinds

The SDK supports the following container image kinds:

- **`container-image`**: A container image reference with image metadata.
- **`generic`**: A generic container image entity that preserves additional payload fields.

## Container image

The concrete `container-image` kind requires an `image` value, such as a registry URI:

```python
image = dh.new_containerimage(
    project="my-project",
    name="my-image",
    kind="container-image",
    image="registry.example.com/my-image:latest",
)
```

The backend may populate additional status fields, including digest, size, tags and manifest data.
