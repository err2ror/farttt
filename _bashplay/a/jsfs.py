#!/usr/bin/python3
from os import system as sys
from sys import argv as args
from json import loads,dumps
print(args)
if len(args)==1:
    print("""JSFS:
    jsfs -m [end file] [files]
    *ONLY FILES* or jsfs recursively
    or
    jsfs -x [jsfs file] [-d end dir]""")
elif args[1]=="-m":
    arwfte=args
    del arwfte[0:3]
    listt=[]
    main=dict({})
    for i in arwfte:
        listt.append(open(i))
        cnt=0
    for i in arwfte:
        main[i]=listt[cnt].read()
    x=open(args[2],"w")
    x.write(dumps(str(main)))
elif args[1]=="-x":
    x=open(args[2])
    y=loads(x.read())
    for i in x:
        z=open(x,"w")
        z.write(x[i])
