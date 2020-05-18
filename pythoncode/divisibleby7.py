a=2000
b=3200
c=0
for i in range(a,b,1):
    d=i%7
    e=i%5
    if(d==c and e!=c):
        print(i)

