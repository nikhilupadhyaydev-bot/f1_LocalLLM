import sys
import time
try:
    import openvino
    import openvino_genai as ov_genai
    from openvino import Core

    core = Core()

except ImportError:
    print("OpenVINO isn't installed!\nProgram is Exiting...")
    print("To install Run CMD:")
    print("pip install openvino openvino-genai")
    sys.exit(1)


# -- Import ends and codebase starts! --
# -- Tried and worked for 2 whole hrs for refactoring this.. --

def banner():
    print("=" * 40)
    print("|" + " " * 38 + "|")
    print("|" + " " * 10 + "Welcome - Admin" + " " * 13 + "|")
    print("=" * 40)
    return

def devices():
    print("OpenVINO version:", openvino.__version__)
    print("Available devices:", core.available_devices)
    return

# -- NOTE that this "localmodels" function must be updated - if suppose you add 16Billion parameter model
 
def localmodels():
    MODELS = {"qwen2.5-coder-3b": 
              {"name": "Qwen2.5 Coder 3B",
               "path": "download_model_OpenVINO/models/Qwen2.5-Coder-3B-Instruct-int4-ov",
               "supports":"CPU,GPU"
            #    yes all supports of models were tested beforehand on ASUS VIVOBOOK S14 S5406SA Intel Core Ultra 5 226v w/ 130V ARC IGPU + 40 TOPS NPU
               },
               "qwen3-8b":
               {"name": "Qwen3 8B",
                "path": "download_model_OpenVINO/models/Qwen3-8B-int4-cw-ov",
                "supports":"CPU,GPU,NPU"
                }
                # IF ADDED YOU ADD MODEL HERE MANUALLY!! yeah pls no shit do some hardwork man... - its your flagship project - im lazy will update in v2 with automation.
    }
    print("Availble Models : MODELS.items()")
    return

def modelchoice():
    # user chooses models per session instead of every prompt - 
    # so basically they choose model only when they restart the application - no model change allowed until app closed. - for now follow this we will update later
    return

def getresponse():
    # reveives input of user from userprompts function()
    # this gets response from the localllm
    return

def userprompts():
    # this gets the user prompt - passes it to the getresponse function()
    # user can select the cpu/gpu/npu
    input("Enter your prompts/Ask me anything : ")
    return

def footer():
    # print("Copyright Product : Shouldnt be used without permission of the Admin")
    # yeah write some crap here lol
    return

def main():
    banner()
    devices()
    return


# TO refactor the entire codebase. -- ongoing.
# exception handling to be done for the bellow codebase ideas for future. -- INPROGRESS!!
# use subprocess to identify whether openvino is installed in the system or not - if not installed then install it via the command
# user to pick up the model
# user to pick between cpu,gpu,npu
# user gives the prompt - the model should remember the chat history for the session only for now.
# the model should use dynamic tokens for response as much as it sees fit.
# do something to make sure that the model updates accoringly by the internet.
# fetches whatever it doeesnt know from the internet - always internet since always is connected that should be the priority - fallback patch the offline works as much as it knows to provide without the internet - dont implement api's yet - for now local models are enough
