def printvar(listvars,vtp):
    print(listvars[vtp])
def mkvar(lv,cl,stru):
    if stru == "set":
        clm = cl.replace(" = "," ")
        zlist=clm.split(" ")
        blv=lv
        blv[zlist[0]]=zlist[1]
        return blv
    if stru == "add":
        clm = cl
        zlist=clm.split(" += ")
        blv=lv
        blv[zlist[0]]+=zlist[1]
