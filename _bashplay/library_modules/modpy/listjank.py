def tolist(st):
    ptl=st[1:len(st)-1].replace("[","é").replace("]","è").split(",")
    tl=[]
    for i in ptl:
        tl.append(i.replace("é","[").replace("è","]"))
    return tl
