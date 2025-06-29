from time import time, sleep, perf_counter
import signal
import sys
import psutil
from modpy.bbash import cmd
# aka from os import system as cmd
def signal_handler(sig, frame):
    print("\nExiting gracefully...")
    sys.exit(0)

# Handle interrupt signal for graceful exit
signal.signal(signal.SIGINT, signal_handler)
mfps=0
f=0
s=perf_counter()
while True:
    f += 1
    elapsed_time = perf_counter() - s
    
    if elapsed_time > 0:
        current_fps = f / elapsed_time
        if current_fps > mfps:
            mfps = current_fps
        
        print(f"FPS: {current_fps:.2f} (mFPS: {mfps:.2f})")
        print(f"RAM: {psutil.virtual_memory().used}")
        cmd("clear")
