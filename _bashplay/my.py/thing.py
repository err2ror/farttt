chars="abcdfghijklmnopqrstuvwxyz013456789.?!,:éè__ ()*+-/.??123456789😀😞'\""
x=input("encode? true/false")
y=input()
def t(x):
    return hex(x).replace("0x","")
if x:
    endstring=""