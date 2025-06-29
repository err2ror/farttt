from time import time, sleep

# Set an interval for measuring FPS BEFORE time starts
# also more user-friendly
interval = int(input())
#sleep_inv=int(input())
f = 0
s = time()
mfps = 0  # Maximum FPS


while True:
    f += 1
    elapsed_time = time() - s
    
    if elapsed_time > interval:  # Update every 'interval' seconds
        current_fps = f / elapsed_time
        if current_fps > mfps:
            mfps = current_fps
        
        print(f"FPS: {current_fps:.2f} (mFPS: {mfps:.2f})")
        
        # Reset counters
        f = 0
        s = time()
    #sleep(sleep_inv) this very line slows down da code
