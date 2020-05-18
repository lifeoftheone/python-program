#Q1
#Q2
''''
a=int(input('enter the no of value you want to enter in a list'))
l=[]
for i in range (a):
    b=int(input('enter the value'))
    l.append(b)
li=[]
print(l)
for j in l:
    b=l.count(j)
    if b>=2:
        li.append(j)
print(len(li)/2)'''
#Q3
""""a=int(input('enter the no of company'))
l=[]
for j in range(a):
    li=[]
    id = int(input('enter the id of the comapny'))
    name = input('enter the name of the company')
    employes = int(input('enter the number of the employe'))
    li.append(id)
    li.append(name)
    li.append(employes)
    l.append(li)
print(li)
print(l)
l3=[]
for i in l:
    a=i[2::]
    if a>=10000:
        l3.append(i[0::])
        print(l3)"""""

''''l=[i for i in range (50,150) if i%2==0 ]
print(l)'''''




