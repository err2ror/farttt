from time import time
print("NotHyperWebster 1.0")
print("5letter")
print(f"Size: {(26**2)*3}b")
input("Press enter to continue")
x=[]
d=open("NotHyperWebster2l.txt","w")
d=open("NotHyperWebster2l.txt","a")
w=0
t=time()
ewc=26**2
alphabet="abcdefghijklmnopqrstuvwxyz"
alphabet=list(alphabet)
for i in alphabet:
    for e in alphabet:
        word=i
        word+=e
        w+=1
        print(f"W: {w}/{ewc} CW: {word} WPS: {round(w/(time()-t))} ETR: {((time()-t)/w)*(ewc-w)}")
        d.write(word+",")
