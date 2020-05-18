#1 greater of thrree number
'''a=int(input("enter first no"))
b=int(input("enter second no"))
c=int(input("enter third no"))
def greater(k,l,m):
    if a>b and b>c:
        k=a
        print(k)
    elif a<b and b>c and a<c:
        l=b
        print(l)
    elif a<b and b<c :
        m=c
        print(m)
    return greater

print(greater(a,b,c))'''

#2 sum of all the no in a list
'''a=int(input("enter total no of element in a list"))
list=[]
for i in range (a):
    b=int(input("enter the values"))
    list.append(b)
print(list)
def sum(k):
    c=0
    for j in k:
        c+=j
    print(c)
    return sum
print(sum(list))'''

#3 multiply all the no in the list
#method 1
'''a=int(input("ente total no of element in a list"))
list=[]
for i in range(a):
    b=int(input("enter value"))
    list.append(b)
print(list)
def listmul():
    c=1
    for j in range(len(list)):
        c=c*list[j]
    print(c)
    return listmul
print(listmul())'''

#method 2
'''a=int(input("ente rtotal no of element in a list"))
list=[]
for i in range(a):
    b=int(input("enter value"))
    list.append(b)
print(list)
def listmul(k):
    c=1
    for j in k:
        c*=j
    print(c)
    return listmul
print(listmul(list))'''


#4 reverse a string
'''a=input("enter a string")
print(a)
def rev(x):
    return x[::-1]
print(rev(a))'''

#5 factorial of a given number
'''a=int(input("enter a number"))
def fact(x):
    c=1
    for i in range(1,a+1):
        c=c*i
    print(c)
    return fact
print(fact(a))'''

#6 check  number in a given list
'''a=int(input("ente total no of element in a list"))
list=[]
for i in range(a):
    b=int(input("enter value"))
    list.append(b)
f= int(input("enter a no to be checked"))
def check(x):
    for i in x:
        if f==i:
            print ("the number is in given range")
    return check
print(check(list))'''


#7 count upper case and lower case
'''a=input("enter a string")
def co(x):
    u=0
    l=0
    for i in x:
        if i.isupper()==True:
            u=u+1
            print("number of uppercase: ", u)
        elif i.islower()==True:
            l=l+1
            print("number of lowercase: ", l)
        else:
            pass
    return co
co(a)'''


#8 list with unique element
'''a=int(input("enetr total no of element in a list"))
list=[]
for i in range(a):
    b=int(input("enter value"))
    list.append(b)
print("list which user entered: ",list)
uni_list=[]
def uni(x):
     for i in list:
         if i not in uni_list:
             uni_list.append(i)
     print(" unique list: ",uni_list)
     return uni
uni(list)'''


#9 given number is prime or not
'''a=int(input("enter the number"))
def prime(x):
    count=0
    for i in range(2,a):
        if (a%i==0):
            count=count+1
    if (count==0):
        print("given number is prime")
    else:
        print("given no is not prime")
    return prime
prime(a)'''


#10 print even number in a given list

"""a=int(input("enetr total no of element in a list"))
list=[]
for i in range(a):
    b=int(input("enter value"))
    list.append(b)
print("list which user entered: ",list)
list2=[]
def even( x):
    for i in list:
        if(i%2==0):
            list2.append(i)
    print("even no list: ",list2)
    return even
even(list)"""

#11  given number is not perfect or not
'''a=int(input("enter a number"))
c=0
l=[]
def perfect(x):
    for i in range(x):
        x%i==1
        l.append(i)
        print(l)
    return perfect
perfect(a)
'''

