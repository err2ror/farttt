from os import system as sys
sys('echo x=msgbox("continue setup?",4+0,"[          ]") >> rpopup.vbs && echo x=msgbox("windows 11 setup finished",0,"oobe coming soon") >> agfgz.vbs')
def count(a):
    x=1
    sys("cls")
    while x < 100:
        print(a)
        print(str(x)+"%")
        sys("cls")
        x+=1
sys("cscript ./rpopup.vbs")
sys("cls")
count("downloading")
count("installing")
count("configurating")
sys("cscript ./agfgz.vbs && del agfgz.vbs && del rpopup.vbs")