# Convert to faster-whisper and test

We will convert the model to be compatible with [faster-whisper](https://github.com/SYSTRAN/faster-whisper), a faster re-implementation of the Whisper model.

Download the model:

```python
model = project.get_model("whisper-ft")
model.download("./model/whisper-ft", overwrite=True)
```

Install `faster-whisper`:

```
%pip install faster-whisper transformers torch==2.8.0
```

Convert the model:

```python
from ctranslate2.converters import TransformersConverter

tc = TransformersConverter("./model/whisper-ft", copy_files=['tokenizer.json', 'preprocessor_config.json'])
tc.convert('./model/faster-whisper-ft', quantization="float16")
```

```python
from faster_whisper import WhisperModel

model = WhisperModel('./model/faster-whisper-ft', device="cpu")
```

Download a sample file:

```
!wget -O kubeai.mp4 "https://github.com/user-attachments/assets/711d1279-6af9-4c6c-a052-e59e7730b757"
```

Finally, we run the model on the sample file to test the results:

```python
segments, info = model.transcribe("kubeai.mp4", beam_size=5)

print("Detected language '%s' with probability %f" % (info.language, info.language_probability))

for segment in segments:
    print("[%.2fs -> %.2fs] %s" % (segment.start, segment.end, segment.text))
```