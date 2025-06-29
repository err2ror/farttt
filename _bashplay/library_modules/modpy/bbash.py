from os import system as cmd
from sys import argv as args
from os import getcwd,remove
def outsystem(cmd,hdjk=".modpy"):
    sys(f"{cmd} >> {getcwd()}/{hdjk}")
    tmp=open(hdjk).read()
    remove(hdjk)
    return tmp
