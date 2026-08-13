import time
import openvino
import openvino_genai as ov_genai
from openvino import Core

MODEL_PATH = "download_model_OpenVINO/models/Qwen2.5-Coder-3B-Instruct-int4-ov"

core = Core()


def banner():
    print("=" * 40)
    print("|" + " " * 38 + "|")
    print("|" + " " * 10 + "Welcome - Admin" + " " * 13 + "|")
    print("|" + " " * 38 + "|")
    print("=" * 40)

def devices():
    print("OpenVINO version:", openvino.__version__)
    print("Available devices:", core.available_devices)

def benchmark(device="CPU"):
    print(f"\nDevice: {device}")
    print("Loading Qwen2.5-Coder 3B...")
    load_start = time.perf_counter()
    pipe = ov_genai.LLMPipeline(
        MODEL_PATH,
        device
    )
    load_time = time.perf_counter() - load_start
    print(f"Model loaded in {load_time:.2f} seconds")
    prompt = """
        Explain what a CPU, GPU and NPU are.
        Compare their purpose in modern AI inference.
        Give the explanation in approximately 300 words.
    """
    print("\nGenerating...\n")
    generation_start = time.perf_counter()
    response = pipe.generate(
        prompt,
        max_new_tokens=300
    )
    generation_time = time.perf_counter() - generation_start
    print(response)
    print("\n" + "=" * 40)
    print("BENCHMARK")
    print("=" * 40)
    print(f"Device:           {device}")
    print(f"Model load time:  {load_time:.2f} sec")
    print(f"Generation time:  {generation_time:.2f} sec")

def main():
    banner()
    devices()
    benchmark("CPU")
    return

main()