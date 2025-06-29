import os
folder=input("folder: ")
efile=open(input("end file: "),"a")
fls=os.listdir(folder)
for fl in fls:
    efile.write(f"""{folder}/{fl}
""")
