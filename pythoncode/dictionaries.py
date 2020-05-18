"""d={"chroma":"campus","python":"ML"}
for i,j in d.items():
    print("the keys are",i)
    print("the values are", j)"""

di={ }
a=int(input("enter the no of values in dictionary"))
for i in range(a):
    di[input("enter the key")]=(input("enter the value")).split(",")
    print(di)
b=(input("enter more values in dictioniries or change the values in dictionaries"))
if b=="y":
    d=input("for update U or add A")
    if d=="U":
        e = input("enter the keys to update")
        for i,j in di.items():
            h=[]
            h=di.get(e)
            h.pop( )
            h.append(input("enter the new value"))

        print(di)
    else:
        c = int(input("how many values to enter"))
        for j in range(c):
         di[input("enter the key")] = (input("enter the value"))
        print(di)
else:
    print(di)


