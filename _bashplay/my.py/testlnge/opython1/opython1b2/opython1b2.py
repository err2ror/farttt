import os
import vgest
f=open(input("loc: "))
x=1
try:
    var=open(".varsys.opyche","x")
except:
    os.remove(".varsys.opyche")
var=open(".varsys.opyche","w")
rvar=open(".varsys.opyche")
def rdline():
    global z
    z=f.readline()
    if z[0:6] == "print ":
        try:
            vgest.printvar(rvar.read(), z.replace("print ", ""))
            #print(var[7:len(z)-1])
        except:
            print(z[6:len(z)-1])
    if " = " in z:
        no=str(vgest.mkvar(rvar.read(), z))
        var.write(no)
while True:
    rdline()
    if input() != "":
        exit()
