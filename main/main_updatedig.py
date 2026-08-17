import sys
import time
import openvino
import openvino_genai as ov_genai
from openvino import Core
core = Core()

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
    if(openvino==False):
        print("Please install openvino application! (cmd link to install the stuff to be needed to run the program)")
        return

# -- NOTE that this "localmodels" function must be updated - if suppose you add 16Billion parameter model
 
def localmodels():
    MODELS = {"qwen2.5-coder-3b": 
              {"name": "Qwen2.5 Coder 3B",
               "path": "download_model_OpenVINO/models/Qwen2.5-Coder-3B-Instruct-int4-ov",
               "supports":"CPU,GPU"
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

def getresponse():
    # this gets response from the localllm
    return

def userprompts():
    input("Enter your prompts/Ask me anything : ")
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
# fetches whatever it doeesnt know from the internet - always internet since always is connected that should be the priority - fallback patch the offline works as much as it knows to provide without the internet
