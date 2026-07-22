# Config

The **`config`** parameter can be used to provide a dictionary containing the project configuration like default store where to log artifacts, dataitems and models.

## Default files store

At the moment, the only supported default data store is `s3`. The format of the dictionary must be as this:

```python
{
    "default_files_store": "s3://bucket",
}
```
