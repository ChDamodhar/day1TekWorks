sno,name=map(str,input("Enter student number and name").split())
marks=[95,56,76]
total=0
for i in marks:
    total+=i
average=total/3
print("total marks and average of student",sno,name,"is\n",total,"\n",average)

