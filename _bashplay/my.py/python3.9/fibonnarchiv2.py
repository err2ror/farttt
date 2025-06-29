#import time

a=0

b=1
z=""

while z == "":
    
    
    sumab=b+a
    z=input(str(a) + "+" + str(b) + "=" + str(sumab))
    a=b
    
    b=sumab
    #1 second delay
    #time.sleep(1)