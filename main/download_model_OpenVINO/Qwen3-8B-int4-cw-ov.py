from huggingface_hub import snapshot_download

model_id = "OpenVINO/Qwen3-8B-int4-cw-ov"

snapshot_download(
    repo_id=model_id,
    local_dir="models/Qwen3-8B-int4-cw-ov"
)

print("Qwen3-8B OpenVINO model downloaded.")