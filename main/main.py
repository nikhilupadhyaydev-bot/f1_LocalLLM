import time
import openvino
import openvino_genai as ov_genai
from openvino import Core


# ============================================================
# CONFIGURATION
# ============================================================

MODELS = {
    "qwen2.5-coder-3b": {
        "name": "Qwen2.5 Coder 3B",
        "path": "download_model_OpenVINO/models/Qwen2.5-Coder-3B-Instruct-int4-ov"
    },

    "qwen3-8b": {
        "name": "Qwen3 8B",
        "path": "download_model_OpenVINO/models/Qwen3-8B-int4-cw-ov"
    }
}


PROMPT = """
Explain what a CPU, GPU and NPU are.

Compare their purpose in modern AI inference.

Give the explanation in approximately 300 words.
"""


core = Core()


# ============================================================
# SYSTEM INFORMATION
# ============================================================

def banner():
    print("=" * 40)
    print("|" + " " * 38 + "|")
    print("|" + " " * 10 + "Welcome - Admin" + " " * 13 + "|")
    print("=" * 40)


def devices():
    print("OpenVINO version:", openvino.__version__)
    print("Available devices:", core.available_devices)


# ============================================================
# MODEL BENCHMARK
# ============================================================

def benchmark(model, device="CPU"):

    model_name = model["name"]
    model_path = model["path"]

    print("\n" + "=" * 40)
    print(f"Model:  {model_name}")
    print(f"Device: {device}")
    print("=" * 40)

    print("\nLoading model...")

    load_start = time.perf_counter()

    pipe = ov_genai.LLMPipeline(
        model_path,
        device
    )

    load_time = time.perf_counter() - load_start

    print(f"Model loaded in {load_time:.2f} seconds")

    print("\nGenerating...\n")

    generation_start = time.perf_counter()

    response = pipe.generate(
        PROMPT,
        max_new_tokens=300
    )

    generation_time = time.perf_counter() - generation_start

    print(response)

    print("\n" + "=" * 40)
    print("BENCHMARK")
    print("=" * 40)

    print(f"Model:            {model_name}")
    print(f"Device:           {device}")
    print(f"Model load time:  {load_time:.2f} sec")
    print(f"Generation time:  {generation_time:.2f} sec")

    return {
        "model": model_name,
        "device": device,
        "load_time": load_time,
        "generation_time": generation_time
    }


# ============================================================
# MAIN
# ============================================================

def main():

    banner()
    devices()

    benchmark(
        MODELS["qwen3-8b"],
        "CPU"
    )


if __name__ == "__main__":
    main()