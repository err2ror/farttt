from random import random as rand
import random
def numtrpy(a):
    flvl=random.randint(1,50)
    tmv=1
    num=a
    while tmv < flvl:
        x=float(rand())
        if rand() <= 0.7:
            num = x + num
        else:
            num = num - x
        tmv+=1
def txtrpy(a):
    flvl=random.randint(1,50)
    tmv=1
    b=str(a)    
    while tmv < flvl:
        b=str(b.replace(random.choice(b), chr(random.randint(1,10000))))
        tmv+=1
    flvl+=1
    return b
def eprint(a):
    print(txtrpy(a))
def bib(a, b):
    return numtrpy(a) < numtrpy(b)
