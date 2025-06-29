def printvar(listvars,vtp):
    print(listvars[vtp])
def mkvar(lv,cl):
    clm = cl.replace(" = "," ")
    zlist=clm.split(" ")
    blv=lv
    blv[zlist[0]]=zlist[1]
    return blv
