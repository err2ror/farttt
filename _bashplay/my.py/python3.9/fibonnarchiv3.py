#import time

a=0

b=1
z=""
c=1
saveinput=input("do you want file? y/n")

while z == "":
    
    
    sumab=b+a
    z=input(str(a) + "+" + str(b) + "=" + str(sumab) + "[fib " + str(c) + " len " + str(len(str(sumab))) + " len/fib " + str((len(str(sumab))/c)*100) + "%]")
    c+=1
    a=b
    
    b=sumab
    #1 second delay
    #time.sleep(1)