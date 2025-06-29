f=open(input("loc: "))
x=1
def rdline():
    z=f.readline()
    if z[0:6] == "print ":
        print(z[6:len(z)-1])
while True:
    rdline()
    if input() != "":
        exit()
