# TO refactor the entire codebase.
# exception handling to be done for the bellow codebase ideas for future.
# use subprocess to identify whether openvino is installed in the system or not - if not installed then install it via the command
# user to pick up the model
# user to pick between cpu,gpu,npu
# user gives the prompt - the model should remember the chat history for the session only for now.
# the model should use dynamic tokens for response as much as it sees fit.
# do something to make sure that the model updates accoringly by the internet.
# fetches whatever it doeesnt know from the internet - always internet since always is connected that should be the priority - fallback patch the offline works as much as it knows to provide without the internet

import time
import openvino
import openvino_genai as ov_genai
from openvino import Core
core = Core()


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


# PROMPT = """
# Explain what a CPU, GPU and NPU are.

# Compare their purpose in modern AI inference.

# Give the explanation in approximately 300 words.
# """
PROMPT = """
Write a Python function called fibonacci(n) that returns
a list containing the first n Fibonacci numbers.

Requirements:
1. Use a loop, not recursion.
2. Return the result as a Python list.
3. Include a short example using n = 10.
4. Return only the code and a brief explanation.
"""



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
    if(openvino==False):
        print("Please install openvino application! (cmd link to install the stuff to be needed to run the program)")
        return


# ============================================================
# MODEL BENCHMARK
# ============================================================

def benchmark(model, device="GPU"):

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
        max_new_tokens=500
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

    # banner()
    devices()

    benchmark(
        MODELS["qwen3-8b"],
        "GPU"
    )


if __name__ == "__main__":
    main()