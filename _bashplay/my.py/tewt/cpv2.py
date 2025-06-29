x=1
y=int(input())
w=1
n=open("cnt.txt","x")
z=open("cnt.txt","a")
v=open("run.sh","a")
v.write("cat cnt.txt")
while x<y:
    z.write(f'''{x}
''')
    print(f"Compiled {x} out of {y}")
    x+=1
print("Finished Compiling")
print("file: run.sh")
system("chmod +x ./run.sh")
