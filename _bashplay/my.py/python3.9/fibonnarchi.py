#import time

a=1
b=2
print("0 + 1 = 1")
print("1 + 2 = 3")
while True:
    
    
    sumab=b+a
    input(str(a) + "+" + str(b) + "=" + str(sumab))
    a=b
    
    b=sumab
    #1 second delay
    #time.sleep(1)