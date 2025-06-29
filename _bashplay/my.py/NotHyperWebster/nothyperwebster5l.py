from time import time
print("NotHyperWebster 1.0")
print("5letter")
print(f"Size: {(26**5)*6}b")
input("Press enter to continue")
x=[]
d=open("NotHyperWebster5l.txt","w")
d=open("NotHyperWebster5l.txt","a")
w=0
t=time()
ewc=26**5
alphabet="abcdefghijklmnopqrstuvwxyz"
alphabet=list(alphabet)
for i in alphabet:
    for e in alphabet:
        for f in alphabet:
            for g in alphabet:
                for h in alphabet:
                    word=i
                    word+=e
                    word+=f
                    word+=g
                    word+=h
                    w+=1
                    #print(f"W: {w}/{ewc} CW: {word} WPS: {round(w/(time()-t))} ETR: {((time()-t)/w)*(ewc-w)}")
                    d.write(word+",")
