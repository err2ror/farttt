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
            vgest.printvar(list(rvar.read()), z.replace("print ", ""))
            #print(var[7:len(z)-1])
        except:
            print(z[6:len(z)-1])
    if " = " in z:
        no=str(vgest.mkvar(list(rvar.read()), z, "set"))
        var.write(no)
    if " += " in z:
        plus=str(vgest.mkvar(list(rvar.read()), z, "add"))
while True:
    rdline()
    if input() != "":
        exit()
