def rand(start):
    if start < 0:
        raise ValueError("Value can't be under zero")
        exit(1)
    x=start+3
    y=0
    while x > 0:
        x=x/x-1
        print(x)
        y+=1
    return y
