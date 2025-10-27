# Managing Speech-to-Text Models with KubeAI Runtime

To support the speech-to-text scenario within the platform it is possible to use the KubeAI runtime when the [KubeAI](https://www.kubeai.org/) operator is
enabled. 

To accomplish this, it is possible to use the KubeAI-supported runtime, namely [FasterWhisper](https://github.com/SYSTRAN/faster-whisper).

For details about the specification, see the corresponding section of [Modelserve](../../runtimes/modelserve.md) reference.

## Exposing Speech-to-Text  Models

To expose the  speech-to-text  model, it is possible to use Core UI or Python SDK. To define the corresponding function, the following parameters should be specified:

- model name
- model URL. Currently the model can be loaded either from HuggingFace (``hf://`` prefix) or from S3 storage of the platform (``s3://``)).

To serve the text speech-to-text model, the function should be run with the ``serve`` action, specifying additional parameters. In particular, it may be necessary to specify the HW profile to use with number of processors or resource specification, and further parameters and arguments accepted by the KubeAI model specification:

- ``args``: command-line arguments to pass to the engine
- ``env``: custom environment values (key-value pair)
- ``secrets``: project secrets to pass the values 
- ``files``: extra file specifications for the deployment
- ``scaling``: scaling specification as of KubeAI documentation
- ``caching_profile``: cache profile as of KubeAI documentation.

For example to deploy a model from HuggingFace, the following procedure may be used:

```python
audio_function = project.new_function("audio",
                                    kind="kubeai-speech",
                                    model_name="audiomodel",
                                    url="hf://Systran/faster-whisper-medium.en")


run = audio_function.run(action="serve")                                    
```

Downloading the model:

```
!wget -O kubeai.mp4 https://github.com/user-attachments/assets/711d1279-6af9-4c6c-a052-e59e7730b757
```

Once deployed, the model is available and it is possible to call the OpenAI-compatible API from within the platform (``/openai/v1/transcriptions`` endpoint):

```python
from openai import OpenAI

client = OpenAI(base_url=f"http://{KUBEAI_ENDPOINT}/openai/v1", api_key="ignore")
audio_file= open("kubeai.mp4", "rb")

transcription = client.audio.transcriptions.create(
    model=f"audiomodel-123zxc", 
    file=audio_file
)

print(transcription.text)
```

By default, the ``KUBEAI_ENDPOINT`` is ``kubeai``.

!!! note "Model name"

    Please note how the model name is defined: it is composed of the name of the model as specified in the function and a random value: ``<model_name>-<run_id>``.
    The name of the generated model as well as the endpoint information can be seen in the run specification (see ``service`` section)

