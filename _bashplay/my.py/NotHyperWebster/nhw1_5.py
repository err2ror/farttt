from time import time
print("NotHyperWebster 1.1")
print("5letter")
print(f"Size: {(26*2)+(26**2*3)+(26**3*4)+(26**4*5)+(26**5*6)}b")
input("Press enter to continue")
x=[]
d=open("1-5lbf.txt","w")
d=open("1-5lbf.txt","a")
w=0
t=time()
ewc=26**5
alphabet="abcdefghijklmnopqrstuvwxyz"
alphabet=list(alphabet)
for i in alphabet:
    d.write(i+"\n")
print("1 letter (0.0002%)")
for i in alphabet:
    for e in alphabet:
        word=i+e
        d.write(word+"\n")
print("2 letter (0.005%)")
for i in alphabet:
    for e in alphabet:
        for f in alphabet:
            word=i+e+f
            d.write(word+"\n")
print("3 letter (0.14%)")
for i in alphabet:
    for e in alphabet:
        for f in alphabet:
            for g in alphabet:
                word=i
                word+=e
                word+=f
                word+=g
                w+=1
                #print(f"W: {w}/{ewc} CW: {word} WPS: {round(w/(time()-t))} ETR: {((time()-t)/w)*(ewc-w)}")
                d.write(word+"\n")
print("4 letter (3.8%)")
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
                    d.write(word+"\n")
print("5 letter")
