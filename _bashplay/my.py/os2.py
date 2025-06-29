import random
from os import system as ss

username = input("PyShell Login: ")
x=open(".usern.txt")
y=open(".pw.txt")
print(x.read())
print(y.read())
if x.read()!=username:
    input(f"{username} password: ")
    print("uWrong username or password.")
    exit(0)
if y.read()!=input(f"{username} password: "):
    print("pWrong username or password.")
    exit(0)
direcs = {
    "/users": {
        "/user": {
            "/directory": {
                "hello"
            },
            "/mnt": {
                
            }
        },
        "usercache": {
            "/a": """
                Hello!
                (C) orso 2022-2023
                Type help for help.
            """
        }
    }
}
print("""
Hello!
(C) orso 2022
Type help for help.
""")
a = "abcdef"
userid = str(random.randint(0,10)) + a[random.randint(0,5)] + str(random.randint(0,10)) + a[random.randint(0,5)] + str(random.randint(0,10)) + a[random.randint(0,5)]
def user():
    return(userid)
x = user()
direc = direcs["/users"]["/user"]
directs = "/users/user"
def cframe():
    cmd = input(f"{username}@pythonc-" + str(user()) + ":" + directs + " $")
    if cmd == "ls" or cmd == "dir /+":
        print(str(direc))                                                                                                                                                                           
    if cmd == "clear":     
        ss("clear")
    if cmd == "help":
        print("""
        Help for PyShell 0.0.2_0
        ls - List Directories
        clear - Clear
        count - Count
        reboot - Reboot
        help - Show This
        exit - Exit and go back to bash
        help [command] for more
        """)
    if cmd == "python":
        return(input(""))
    if cmd == "reboot":
        print("rebooting")
        print("""
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
        """)
        x = 0
        while x < 100:
            print(str((x / 10) * 10) + "% complete")
            x = x + .1
        print(direcs["/users"]["usercache"]["/a"])
    def counters():
        x = 0
        if cmd == "help count":
            print("""
            (c) ORSO 2024
            Help for count:
            count:
            normal counting to 100
            count -p -launch:
            progressbar counting
            count -p:
            %
            count -err 404:
            throws error midway
                    """)
        if cmd == "count":
            x = 0
            while x < 100:
                print(x)
                x = x + 1
        if cmd == "count -p":
            x = 0
            while x < 100:
                print(str((x / 10) * 10) + "% complete")
                x = x + .1
        if cmd == "count -p -launch":
            x = 0
            while x <= 100:
                bx=round(x-x%1)
                ax=[
                    f"    {bx}%   "
                    ,f"-  {bx}%   "
                    ,f"-- {bx}%   "
                    ,f"---{bx}%   "
                    ,f"---{bx}%   "
                    ,f"---{bx}%   "
                    ,f"---{bx}%   "
                    ,f"---{bx}%   "
                    ,f"---{bx}%-  "
                    ,f"---{bx}%-- "
                    ,f"---{bx}%---"]
                print(ax[round(x/10)])
                x=x+0.001
                
        if cmd == "count -err 404":
            x = 0
            while x < 50:
                print(str((x / 10) * 10) + "% complete")
                x = x + .1
            print("404")
            x = 4
            while x < 100:
                print(str((x / 10) * 10) + "% complete")
                x = x + .1
        if cmd == "install update":
            print("Installing")

        if cmd == "exit":
            exit(0)
        

    counters()
while True:
    cframe()
