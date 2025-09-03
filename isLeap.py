def isLeap(x):
    if(x%4==0):
        if(x%100==0):
            if(x%400==0):
                print("Leap Year")
            else:
                print("Not a Leap year")
        else:
            print("Leap year")
    else:
        print("Not a leap year")
a=int(input("Enter year:"))
isLeap(a)