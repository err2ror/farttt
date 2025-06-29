import time
x=1
y=1000000
z=time.time()
while x<y:
    x+=1
    print(x)
print(time.time()-z)
