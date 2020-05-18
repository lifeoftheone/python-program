a=int(input("enter the age of 1st person"))
b=int(input("enter the age of 2nd person"))
c=int(input("enter the age of 3rd person"))
if(a>b and b>c):
    print("a is oldest and c is youngest")
elif(a>c and a<b):
    print("b is oldest and c is youngest")
elif(a<c and b>c):
    print("b is oldest and a is youngest")
elif(a<c and b<c and a<b):
    print("c is oldest and a is youngest")
elif(a>b and c>b and a>c):
    print("a is oldest and b is youngest")
else:
    print("c is oldest and b is youngest")

    





