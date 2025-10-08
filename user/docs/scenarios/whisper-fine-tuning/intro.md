# Fine-tuning speech-to-text

In this scenario, we fine-tune [Whisper](https://huggingface.co/openai/whisper-small), a model for speech-to-text recognition.

## Requirements

You'll need a HuggingFace token that has access to the voice library we will use. Enable your token to access [this repository](https://huggingface.co/datasets/mozilla-foundation/common_voice_17_0).

Create a workspace on Coder for Jupyter, with GPU enabled. When the workspace is up, access Jupyter and create a new notebook.

## Set-up

Import the platform's library and create a project:

```python
import digitalhub as dh

project = dh.get_or_create_project("whisper-fine-tuning")
```

Create a secret as follows, make sure you replace the value with the token that has access to the aforementioned repository:

```python
project.new_secret(name="HF_TOKEN", secret_value="my-token")
```

The functions we will run use code from a Python file. Due to the many lines this file has, instead of presenting it in this documentation, we invite you to download it from [the subfolder related to this scenario](https://github.com/scc-digitalhub/digitalhub-tutorials/tree/main/s8-whisper-fine-tuning). Copy the `src` directory and paste it at the same level of the notebook you're using. It should contain a `.py` file. 