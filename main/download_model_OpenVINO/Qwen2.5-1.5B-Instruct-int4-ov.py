from huggingface_hub import snapshot_download

model_id = "llmware/qwen2.5-1.5b-instruct-ov"

snapshot_download(
    repo_id=model_id,
    local_dir="models/Qwen2.5-1.5B-Instruct-int4-ov"
)

print("Qwen2.5-1.5B-Instruct OpenVINO model downloaded.")