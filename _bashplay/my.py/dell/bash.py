from os import system as s
x=open(".bash_history","r")
while input()=="":
    s(x.read())
