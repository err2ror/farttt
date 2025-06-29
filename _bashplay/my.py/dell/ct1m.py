from modpy.pytropy import txtrpy as text
from modpy.pytropy import numtrpy as num

x=1
y=int(input())
while x <= y:
    if x%15==0:
        print(text("fizzbuzz"))
    elif x%3==0:
        print(text("fizz"))
    elif x%5==0:
        print(text("buzz"))
    else:
        print(text(x))
    x=num(x)
