mport random
username = input("PyShell Signup: ")
input(f"{username} password: ")
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
                (C) orso 2022
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
    cmd = input("user@pythonc-" + str(user()) + ":" + directs + " $")
    if cmd == "ls" or cmd == "dir /+":
        print(str(direc))                                                                                                                                                                           
    if cmd == "clear":                                                                                                                                                                              
        print("""                                                                                                                                                                                   
                                                                                                                                                                                                    
                                                                                                                                                                                                    
                                                                                                                                                                                                    
                                                                                                                                                                                                    
                                                                                                                                                                                                    
                                                                                                                                                                                                    
                                                                                                                                                                                                    
                                                                                                                                                                                                                                 
                                                                                                                                                                                                                                 
                                                                                                                                                                                                                                 
                                                                                                                                                                                                                                 
                                                                                                                                                                                                                                 
                                                                                                                                                                                                                                 
                                                                                                                                                                                                                                 
                                                                                                                                                                                                                                                                      
                                                                                                                                                                                                                                                                      
                                                                                                                                                                                                                                                                      
                                                                                                                                                                                                                                                                      
                                                                                                                                                                                                                                                                                                                           
                                                                                                                                                                                                                                                                                                                           
                                                                                                                                                                                                                                                                                                                           
                                                                                                                                                                                                                                                                                                                           
                                                                                                                                                                                                                                                                                                                           
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
        """)
    if cmd == "help":
        print("""
        Help for PyShell 0.0.1_0
        ls - List Directories
        clear - Clear
        count - Count
        count -p - Complete screen
        count -err 404 - count -p With 404 error
        help - Show This
        exit - Exit and go back to bash
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
        if cmd == "exit":
            exit(0)
    counters()
while True:
    cframe()
