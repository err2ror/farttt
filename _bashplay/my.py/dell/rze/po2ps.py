from modpy.bbash import args
if len(args)==1:
    x=int(input("NumSer"))
    z=int(input("NumDig"))
else:
    x,z=int(args[2]),int(args[3])
y=0
mc=1
l=[]
while y<x:
    y+=1
    mc=(mc*2)%(10**z)
    l.append(mc)
cj=open(str(z),"w")
cj.write(str(l))
print(l)
print(str(len(l)-len(set(l))))
print(x-len(l)-len(set(l))-1)