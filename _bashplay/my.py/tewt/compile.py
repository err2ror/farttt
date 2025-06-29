from math import floor
from os import system
system("mkdir file")
x=1
y=int(input())
w=1
n=open(f"file/{str(w)}","x")
z=open(f"file/{str(w)}","a")
v=open("run.sh","a")
v.write("./file/1;")
system("chmod +x ./file/1")
r=int(input("fragments of "))
while x<y:
    #if crashes modify this
    if x/r==floor(x/r):
        w+=1
        n=open(f"file/{str(w)}","x")
        z=open(f"file/{str(w)}","a")
        v.write(f"./file/{w};")
        system(f"chmod +x ./file/{w}")
    z.write(f'''echo {x}; 
''')
    print(f"Compiled {x} out of {y}")
    x+=1
print("Finished Compiling")
print("file: run.sh")
system("chmod +x ./run.sh")
