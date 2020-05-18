l1=input("enter values seperated by ,").split(",")

l2=[]
def element(x):
    l2.append(x[0])
    l2.append(x[-1])
    return l2
l2=element(l1)
print(l2)