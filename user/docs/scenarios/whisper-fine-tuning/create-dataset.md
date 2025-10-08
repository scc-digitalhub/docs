# Create and process dataset

In this step, we create a function to pre-process the dataset and store it as an artifact.

Make sure the file specified in the `code_src` parameter is present.

```python
func = project.new_function(
    name="create-dataset", 
    kind="python", 
    python_version="PYTHON3_10", 
    code_src="src/fine_tuning_seq2seq.py",  
    handler="preprocess_dataset",
    requirements=["datasets[audio]==3.6.0", "transformers==4.56.1", "torch==2.8.0", "accelerate==1.10.1", "evaluate==0.4.5", "jiwer==4.0.0"]
)
```

Run the function. It may take over 10 minutes.

```python
train_run = func.run(action="job",
                     parameters={
                         "model_id": "openai/whisper-small",
                         "artifact_name": "audio-dataset",
                         "dataset_name": "mozilla-foundation/common_voice_17_0",
                         "language": "Italian",
                         "language_code": "it",
                         "max_train_samples": 100,
                         "max_eval_samples": 100
                     },
                     secrets=["HF_TOKEN"],
                     envs=[
                        {"name": "HF_HOME", "value": "shared/data/huggingface"},
                        {"name": "TRANSFORMERS_CACHE", "value":  "shared/data/huggingface"}
                     ],
                     volumes=[{
                        "volume_type": "persistent_volume_claim",
                        "name": "volume-llmpa",
                        "mount_path": "/shared/data",
                        "spec": { "size": "300Gi" }}]
					)
```

!!! Warning "If the run fails"
    If the run fails, inspect its logs on the console. If you see mention of the dataset being `a gated dataset on the Hub`, you likely did not enable your HuggingFace account to have access to [this repository](https://huggingface.co/datasets/mozilla-foundation/common_voice_17_0).