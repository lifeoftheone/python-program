#spcl case
'''a=int(input ("enter a value"))
b=int(input("enter a value"))
def sub(func):
    def inner(p,q):
         c=p-q
         return c
    return inner
@sub
def add(a,b):
    print("hi")
    return(a+b)
print (add(a,b))'''

#2
'''a=int(input("enter total number of names"))
l=[]
for i in range (a):
    b=input("enter the names")
    l.append(b)
def rev(func):
    def inner(x):
        l1=[]
        for j in x:
            f=j[::-1]
            l1.append(f)

        return func(l1)
    return inner
@rev
def prin(l):
    return l
print(prin(l))'''