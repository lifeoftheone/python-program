#1
'''
d1={}
d2={}
x=int(input("enter total no of keys"))
for i in range (x):
    d1[input("enter the keys")]=input("enter the values").split(",")
    print(d1)
for j in range(x+1):
    d2[input("enter the keys")]=input("enter the values").split(",")
    print(d2)
d1={"stname":['takshak','vishwas','puneet','negi','shubham'],"strollno":['1','2','3','4','5'],"staddress":['rajori','dwarka','dwarka mor','nawada','agra']}
d2={"empname":['rohit','pandat','parva','ravi'],"empcode":['1','2','3','4'],"empaddress":['panipat','khojkipur','up','kairana'],"domain":['java','c','python','html']}
y=input("s for student or e for employe")
count=-1
if y=="s" or y=="S":
    z=int(input("enter student roll no"))
    for k in d1["strollno"]:
        count+=1
        if(k==z):
            break
    print(d1["stname"][count])
    print(d1["staddress"][count])

elif y=="e" or y=="E":
    z=int(input("enter employe code"))
    for l in d2["empcode"]:
        count += 1
        if (l == z):
            break
    print(d2["empname"][count])
    print(d2["empaddress"][count])
    print(d2["domain"][count])
else:
    print("enter s or e")'''