# Hugging Face paths

Hugging Face paths point to model repositories on the Hugging Face Hub. The SDK downloads the repository to a local directory when the consuming operation needs local files.

## Format

- `hf://owner/repository`
- `huggingface://owner/repository`
- Add `?revision=...` to select a branch, tag or commit.

## Behavior

- The path is parsed as a Hugging Face repository ID; URL-encoded segments are decoded.
- The destination must be a directory. Existing non-empty destinations are rejected unless the store is explicitly asked to overwrite them.
- The Hugging Face store supports downloads only. Uploads, SQL queries and DataFrame reads/writes are not supported.

## Examples

```python
model_path = "hf://microsoft/DialoGPT-medium"
revisioned_model_path = "hf://openai/whisper-tiny?revision=main"
```

## Requirements

Install the optional Hugging Face dependency in the environment that performs the download:

```bash
pip install "digitalhub[huggingface]"
```

Private or gated repositories also require the Hugging Face credentials expected by `huggingface_hub`.
