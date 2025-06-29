#import time
import os
if input("is file here? y/n") == "y":
    os.remove("fibofile.txt")

f=open("fibofile.txt","x")
a=0
num=int(input("num fib"))
b=1
z=1
c=1


while c <= num:
    sumab=b+a
    c+=1
    a=b
    f=open("fibofile.txt","a")
    f.write(str(a) + "+" + str(b) + "=" + str(sumab) + "[fib " + str(c) + " len " + str(len(str(sumab))) + " len/fib " + str((len(str(sumab))/c)*100) + "%]")
    b=sumab
    #1 second delay
    #time.sleep(1)