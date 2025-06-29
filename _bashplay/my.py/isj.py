from random import choice
alp=list("01")
x=0
s=""
while x<100:
    x+=1
    s+=choice(alp)
print(str(len(s.replace("0","")))+"/"+str(len(s.replace("1","")))+", "+str((len(s.replace("0",""))/1))+"% 0s, "+str((len(s.replace("1",""))/1))+"% 1s")
