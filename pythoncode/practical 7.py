a=int(input("enter number of classes attend"))
b=int(input("total number of classes"))
d=str(input("medical case type y or n"))
c=(a/b)*100
if(c>=75 ):
    print(c)
    print("student is allowed to sit in the exam")
elif(c<75 and d=="y"):
    print(c)
    print("student is allowed to sit in the exam on behalf of medical issue")
else:
    print(c)
    print("student is not allowed to sit in the class")