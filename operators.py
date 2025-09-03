def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def mul(a,b):
    return a*b
def div(a,b):
    return a/b
def mod(a,b):
    return a%b
x,y=map(int,input("Enter x and y values").split())
print(add(x,y))
print(sub(x,y))
print(mul(x,y))
print(div(x,y))
print(mod(x,y))