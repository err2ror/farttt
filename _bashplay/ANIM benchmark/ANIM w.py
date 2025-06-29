import os
from time import time
try:
    os.remove("tf.mem.test")
except:
    z=open("tf.mem.test","x")
f=input("read or write?")
g=int(input("secs: "))
h=0
bits=0
ctime=time()
z=open("tf.mem.test","w")
if f == "w":
    while g>time()-ctime:
        z.write("a")
        bits+=1
print(f"""Written {bits} bytes in {g} seconds.
{bits/g} Bytes per second
{bits/(g*1000)} KBps
{bits/(g*1000000)} MBps""")
