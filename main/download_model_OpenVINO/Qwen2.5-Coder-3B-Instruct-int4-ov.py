from huggingface_hub import snapshot_download

model_id = "OpenVINO/Qwen2.5-Coder-3B-Instruct-int4-ov"

snapshot_download(
    repo_id=model_id,
    local_dir="models/Qwen2.5-Coder-3B-Instruct-int4-ov"
)

print("Model downloaded successfully.")