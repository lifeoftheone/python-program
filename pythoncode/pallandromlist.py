L=int(input("enter the length of list seperated by ,"))
Li=[]
for i in range(L):
    a=int(input("enter value"))
    Li.append(a)
print(Li)
L2=Li[: :-1]
print(L2)
if(Li==L2):
    print("palandram list")
else:
    print("non palandram list")
