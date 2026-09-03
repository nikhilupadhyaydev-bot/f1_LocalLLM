from huggingface_hub import snapshot_download

model_id = "llmware/llama-3.2-1b-instruct-ov"

snapshot_download(
    repo_id=model_id,
    local_dir="models/Llama-3.2-1B-Instruct-int4-ov"
)

print("Llama-3.2-1B-Instruct OpenVINO model downloaded.")