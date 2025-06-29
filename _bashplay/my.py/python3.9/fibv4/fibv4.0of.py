#import time 
import os 
if os.path.exists("fibofile.txt"): 
    os.remove("fibofile.txt") 
f=open("fibofile.txt","x") 
a=0 
b=1 
z="" 
c=1 
d=int(input("nums"))
saveinput=input("do you want file? y/n") 
while c <= d: 
    sumab=b+a 
    c+=1 
    a=b 
    f=open("fibofile.txt","a") 
    f.write(str(a) + "+" + str(b) + "=" + str(sumab) + "[fib " + str(c) + " len " + str(len(str(sumab))) + " len/fib " + str((len(str(sumab))/c)*100) + "]") 
    b=sumab 
    #1 second delay 
    #time.sleep(1) 
