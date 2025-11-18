# Fine-tuning

Next, we create and run the function for fine-tuning.

Create the function:

```python
func = project.new_function(
    name="train-whisper", 
    kind="python", 
    python_version="PYTHON3_10", 
    code_src="src/fine_tuning_seq2seq.py",  
    handler="train_and_log_model",
    requirements=["datasets[audio]==3.6.0", "transformers==4.52.0", "torch==2.8.0", "accelerate==1.10.1", "evaluate==0.4.5", "jiwer==4.0.0"]
)
```

Run the function. This may take even longer than the previous one.

```python
train_run = func.run(action="job",
                     parameters={
                         "model_id": "openai/whisper-small",
                         "model_name": "whisper-ft",
                         "dataset_name": "fsicoli/common_voice_17_0",
                         "language": "Italian",
                         "language_code": "it",
                         "max_train_samples": 100,
                         "max_eval_samples": 100,
                         "eval_steps": 100,
                         "save_steps": 100,
                         "max_steps": 500,
                         "warmup_steps": 50
                     },
                     profile="1xa100",
                     secrets=["HF_TOKEN"],
                     envs=[
                        {"name": "HF_HOME", "value": "/local/data/huggingface"},
                        {"name": "TRANSFORMERS_CACHE", "value":  "/local/data/huggingface"}
                     ],
                     volumes=[{
                        "volume_type": "persistent_volume_claim",
                        "name": "volume-llmpa",
                        "mount_path": "/local/data",
                        "spec": { "size": "100Gi" }}]
					)
```