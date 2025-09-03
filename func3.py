def fun3():
    d=int(input("Enter no of days;"))
    y=d//365
    d=d%365
    m=d//30
    return y,m
print(fun3()) 