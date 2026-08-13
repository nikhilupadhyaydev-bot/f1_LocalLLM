import openvino
from openvino import Core

core = Core()

def banner():
    print("=" * 40)
    print("|" + " " * 38 + "|")
    print("|" + " " * 10 + "Welcome - Admin" + " " * 13 + "|")
    print("|" + " " * 38 + "|")
    print("=" * 40)
    return

def devices():
    print("OpenVINO version:", openvino.__version__)
    print("Available devices:", core.available_devices)
    return

def main():
    banner()
    devices()
    return
main()