a=int(input("enter value seperated by ,"))
data_list=[]
c=0
for i in range (a):
    b=int(input("enter the values"))
    data_list.append(b)
for j in data_list:
   c+=j
print(c)