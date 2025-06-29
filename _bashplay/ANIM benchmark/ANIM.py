from time import time
a=0
i=int(input("Number of benchmarks (100k): "))
m=0
z=0
tot=0
while i>m:
    t=time()
    x=0
    while x<100000:
        x+=1
    y=-(x/(t-time()))
    if y>a:
        a=y
    print(y)
    m+=1
    tot+=y
    #print(a)
print("Average: "+str(tot/m))
print("Best: "+str(a))
