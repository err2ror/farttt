from random import random
from time import sleep
x=[0,0,0,0,0]
while True:
    y=max(x)
    x=[y,y+((random()*2)-1),y+((random()*2)-1),y+((random()*2)-1),y+((random()*2)-1)]
    sleep(0.01)
    print(x)
