'''
a=int(input("enter total no of values"))
l=[]
for i in range(a):
    s=0
    li=[]
    while(s==0):
        li.append(input("enter the value"))
        p=input("do u wish to enter more Y or N")
        if (p=='N' or p=='n'):
            s=1
    l.append(li)
print(l) '''

a=int(input("enter total no of values"))
l=[]
for i in range(a):
    li=[]
    b=int(input("enter no of values of sub list"))
    for j in range(b):
        li.append(int(input('enter value')))
    l.append(li)
    print (l)
lii=[]
for o in range(len(l)):
    for t in range(len(li)):
        for k in range (a):
            liii=[]
            liii.append(l[t][o])
        lii.append(liii)
    print(liii)
    print(lii)