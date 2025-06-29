def l(x):
    return x+1
def m(x):
    return x-1
def plus(x,y):
    z=x
    w=y
    while w>0:
        w=m(w)
        z=l(z)
    return z
def times(x,y):
    z=x
    w=y
    while w>0:
        w=m(w)
        z=plus(z,y)
    return z

print(times(5,5))
