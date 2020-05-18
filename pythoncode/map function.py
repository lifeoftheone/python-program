a=int(input("enter no of values"))
utemp=[]
ctemp= []
for i in range (a):
    b=float(input("enter the values in celcious"))
    utemp.append(b)
ctemp=list(map(lambda x: x+273.15, utemp))
print("the values are in kelvin" , ctemp)