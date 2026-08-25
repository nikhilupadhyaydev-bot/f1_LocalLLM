import sys
import time
import subprocess

try:
    import openvino
    import openvino_genai as ov_genai
    from openvino import Core

    core = Core()

except ImportError:
    print("OpenVINO isn't installed!")
    choice = input("Install it now automatically via pip? (y/n): ").strip().lower()

    if choice == "y":
        try:
            subprocess.check_call(
                [sys.executable, "-m", "pip", "install", "openvino", "openvino-genai"]
            )
            # re-import after install so the rest of the script can use them
            import openvino
            import openvino_genai as ov_genai
            from openvino import Core

            core = Core()
            print("\nOpenVINO installed successfully. Continuing...\n")

        except subprocess.CalledProcessError as e:
            print(f"\nAuto-install failed: {e}")
            print("Please run manually: pip install openvino openvino-genai")
            sys.exit(1)
    else:
        print("To install Run CMD:")
        print("pip install openvino openvino-genai")
        sys.exit(1)


# -- Import ends and codebase starts! --
# -- Tried and worked for 2 whole hrs for refactoring this.. --

def banner():
    print("=" * 40)
    print("|" + " " * 38 + "|")
    print("|" + " " * 6 + "Welcome - Lemun Enterprises" + " " * 5 + "|")
    print("=" * 40)
    return


def devices():
    try:
        print("OpenVINO version:", openvino.__version__)
        print("Available devices:", core.available_devices)
    except Exception as e:
        print(f"Couldn't read device info: {e}")
    return


# -- NOTE that this "localmodels" function must be updated - if suppose you add 16Billion parameter model

def localmodels():
    MODELS = {"qwen2.5-coder-3b":
              {"name": "Qwen2.5 Coder 3B",
               "path": "download_model_OpenVINO/models/Qwen2.5-Coder-3B-Instruct-int4-ov",
               "supports": "CPU,GPU"
               # yes all supports of models were tested beforehand on ASUS VIVOBOOK S14 S5406SA Intel Core Ultra 5 226v w/ 130V ARC IGPU + 40 TOPS NPU
               },
              "qwen3-8b":
              {"name": "Qwen3 8B",
               "path": "download_model_OpenVINO/models/Qwen3-8B-int4-cw-ov",
               "supports": "CPU,GPU,NPU"
               }
              # IF ADDED YOU ADD MODEL HERE MANUALLY!! yeah pls no shit do some hardwork man... - its your flagship project - im lazy will update in v2 with automation.
              }
    # returning it now instead of just printing, so main() can actually use it
    return MODELS


def modelchoice(models):
    # user chooses models per session instead of every prompt -
    # so basically they choose model only when they restart the application - no model change allowed until app closed. - for now follow this we will update later

    print("\nAvailable Models:")
    keys = list(models.keys())
    for i, key in enumerate(keys, start=1):
        info = models[key]
        print(f"  {i}. {info['name']}   (supports: {info['supports']})")

    model = None
    while model is None:
        try:
            raw = input("\nPick a model (number): ").strip()
            idx = int(raw)
            if 1 <= idx <= len(keys):
                model = models[keys[idx - 1]]
            else:
                print(f"Enter a number between 1 and {len(keys)}.")
        except ValueError:
            print("That's not a number, try again.")

    # user to pick between cpu,gpu,npu
    supported = [d.strip().upper() for d in model["supports"].split(",")]
    detected = core.available_devices

    device = None
    while device is None:
        raw = input(f"Pick a device ({'/'.join(supported)}): ").strip().upper()
        if raw not in supported:
            print(f"'{model['name']}' only supports: {', '.join(supported)}")
            continue
        if not any(raw in d for d in detected):
            print(f"Heads up: OpenVINO doesn't see a {raw} on this machine ({detected}).")
            confirm = input("Try loading it anyway? (y/n): ").strip().lower()
            if confirm != "y":
                continue
        device = raw

    return model, device


def load_pipeline(model, device):
    print(f"\nLoading {model['name']} on {device}...")
    load_start = time.perf_counter()

    try:
        pipe = ov_genai.LLMPipeline(model["path"], device)
    except Exception as e:
        print(f"\nFailed to load model: {e}")
        print("Check that the model path exists and the device string is valid.")
        sys.exit(1)

    print(f"Model loaded in {time.perf_counter() - load_start:.2f} seconds")
    return pipe


def getresponse(pipe, prompt):
    # reveives input of user from userprompts function()
    # this gets response from the localllm

    # dynamic tokens: we don't force a fixed length, the model stops itself on EOS.
    # max_new_tokens here is just a safety ceiling so one bad turn can't run forever.
    gen_config = ov_genai.GenerationConfig()
    gen_config.max_new_tokens = 2048

    print("Assistant: ", end="", flush=True)
    start = time.perf_counter()

    def streamer(subword):
        print(subword, end="", flush=True)
        return False  # False = keep generating, True would stop early

    try:
        pipe.generate(prompt, gen_config, streamer)
    except Exception as e:
        print(f"\n[Generation error: {e}]")
    finally:
        elapsed = time.perf_counter() - start
        print(f"\n[{elapsed:.2f}s]\n")


def userprompts(pipe):
    # this gets the user prompt - passes it to the getresponse function()
    # user can select the cpu/gpu/npu -> handled earlier in modelchoice(), one time per session

    print("\nChat session started. Type 'exit' or 'quit' to end.\n")

    # start_chat() makes the pipeline remember turns for this session only,
    # which covers the "remember chat history for the session" requirement
    pipe.start_chat()

    try:
        while True:
            try:
                prompt = input("You: ").strip()
            except (EOFError, KeyboardInterrupt):
                print("\nInterrupted.")
                break

            if prompt.lower() in ("exit", "quit"):
                break
            if not prompt:
                continue

            getresponse(pipe, prompt)
    finally:
        pipe.finish_chat()


def footer():
    print("Session ended. Thanks for using the assistant.")
    # print("Copyright Product : Shouldnt be used without permission of the Admin")
    # yeah write some crap here lol
    return


def main():
    banner()
    devices()

    models = localmodels()
    model, device = modelchoice(models)

    pipe = load_pipeline(model, device)

    userprompts(pipe)

    footer()
    return

# NOTE - RESPONSE IS GIVEN TOKEN BY TOKEN!! - just like other llm's

if __name__ == "__main__":
    main()


# TO refactor the entire codebase. -- DONE for this pass.
# exception handling to be done for the bellow codebase ideas for future. -- DONE (import, model load, generation, ctrl-c/EOF on input)
# use subprocess to identify whether openvino is installed in the system or not - if not installed then install it via the command -- DONE
# user to pick up the model -- DONE
# user to pick between cpu,gpu,npu -- DONE
# user gives the prompt - the model should remember the chat history for the session only for now. -- DONE via pipe.start_chat()/finish_chat()
# the model should use dynamic tokens for response as much as it sees fit. -- DONE, model self-stops on EOS, max_new_tokens is just a safety ceiling
# do something to make sure that the model updates accoringly by the internet.
# fetches whatever it doeesnt know from the internet - always internet since always is connected that should be the priority - fallback patch the offline works as much as it knows to provide without the internet - dont implement api's yet - for now local models are enough
# ^ still not implemented on purpose per the note above - no APIs yet, local-only for this pass
