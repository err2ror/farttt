#py
# THE LINE OF CODE ABOVE IS VERY IMPORTANT
from time import perf_counter
import sys
import psutil  # For memory usage
import os

# Handle interrupt signal for graceful exit
signal.signal(signal.SIGINT, signal_handler)

# Pre-calculating the total memory in GiB and GB
BYTES_IN_GIB = 1073741824  # 1024^3
BYTES_IN_GB = 1000000000  # 10^9
mem_total_gib = round(psutil.virtual_memory().total / BYTES_IN_GIB, 3)
mem_total_gb = round(psutil.virtual_memory().total / BYTES_IN_GB, 3)

mfps = 0  # Maximum FPS
f = 0  # Frame counter
s = perf_counter()  # Start time

while True:
    f += 1
    elapsed_time = perf_counter() - s
    
    if elapsed_time > 1:  # Update every second
        current_fps = f / elapsed_time
        if current_fps > mfps:
            mfps = current_fps
        
        # Get current memory usage
        memory_usage_b = psutil.virtual_memory().used
        
        # Convert to GiB (1 GiB = 1024^3 bytes)
        memory_usage_gib = memory_usage_b / BYTES_IN_GIB
        
        # Print FPS and RAM usage (in GiB)
        print(f"FPS: {round(current_fps)} (mFPS: {round(mfps)})")
        print(f"DeltaTime: {round(1000000000/current_fps)} ns")
        print(f"RAM Usage: {round(memory_usage_gib, 3)}/{mem_total_gib} GiB")
        
        # Reset counters
        f = 0
        s = perf_counter()
