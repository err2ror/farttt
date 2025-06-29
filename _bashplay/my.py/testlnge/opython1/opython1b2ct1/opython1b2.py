import vgor
import os
import vgest
f=open(input("loc: "))
x=1
cft=open(input("filename: "),"a")
cft.write("try:")
cft.write('    var=open(".varsys.opyche","x")')
cft.write("except:")
cft.write('    os.remove(".varsys.opyche")')
cft.write('var=open(".varsys.opyche","w")')
cft.write('rvar=open(".varsys.opyche")')
def rdline():
    global z
    z=f.readline()
    if z[0:6] == "print ":
        try:
            vgor.printvar()
            cft.write(vgest.printvar())
        except:
            cft.write(f"print({z[6:len(z)-1]})")
    if " = " in z:
        cft.write(f'clm = {z.replace(" = "," ")}')
        cft.write('zlist=clm.split(" ")')
        cft.write('blv=rvar.read()')
        cft.write('blv[zlist[0]]=zlist[1]')
        cft.write('var.write(blv)')
while True:
     rdline()



