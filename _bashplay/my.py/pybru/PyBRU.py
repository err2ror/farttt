from ren import adren
from ren import delren
from os import system
folder=open(input("file: "))
if input("set permissions?")=="y":
    perms=input("perms: ")
s1=input("del file extention? ")
if s1=="y":
    s2=input("new file extension?")
    if s2=="y":
        s3=input("new file extension: ")
else:
    s3=input("additional file extension (default:none): ")
s4=input("delchl: ")
s5=input("delchr: ")
s6=input("prefix: ")
s7=input("suffix: ")
s8=input("add number before file extension?")
s9=input("add number after file extension?")
s10=input("new file name (default: no change): ")
if s8=="y" or s9=="y":
    d=1
else:
    d=""
for fp in folder:
    #adren(fn,lfx,rfx,adnumbffe,adnumaffe,nfn)
    system(f'mv {fp} {adren(delren(fp, s1, s3, s4, s5), s6=="y", s7=="y", d, d, s10)}')
    try:
        d+=1
    except:
        d=""
