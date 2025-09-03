def bigof3(a,b,c):
    if(a>b):
        if(a>c):
            print(a,"is big")
        else:
            print(c,"is big")
    else:
        if(b>c):
            print(b,"is big")
        else:
            print(c,"is big")
bigof3(2,3,4)