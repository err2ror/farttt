#!/usr/bin/python3
from os import getcwd as getpath
from sys import argv as args
from os.path import isfile
if len(args)==1:
    print("""Help for lnh:
    Creates hard links with desktop files.
    usage: lnh [link path] [original file path] -a=[app (optional)
    for terminal apps, use -ta instead of -a
    or
    lnh --set-default-app-folder=[app command]
    or
    lnh --set-default-app-file=[app command]""")
    exit(0)
z=args[1]
if not "--set-default-app-" in z:
    w=args[2]
    if len(args)>=4:
        tmp=args[3]
        if "-a=" in tmp:
            of=tmp.replace("-a=","")
            term="false"
        else:
            term="true"
            of=tmp.replace("-ta=","")
    else:
        of=open("/home/orso/.config/lnh.config")
    x=open(f"{z}.desktop","a")
    x.write(f"""[Desktop Entry]
Name={z}
Comment=Link to {w}
Exec={of} {getpath()}/{w}
Icon=beta
Terminal={term}
Type=Application
""")
else:
    y=open("/home/orso/.config/lnh.config")
    x=open("/home/orso/.config/lnh.config","w")
    if "folder" in z:
        tmp=y.readline()
        tmp2=z.replace("--set-default-app-folder=","")
    else:
        tmp
    x.write()
