a=int(input("enter value seperated by ,"))
data_list=[]
new_list = []
for i in range (a):
    b=int(input("enter the values"))
    data_list.append(b)
while data_list:
    minimum = data_list[0]  # arbitrary number in list
    for x in data_list:
        if x < minimum:
            minimum = x
    new_list.append(minimum)
    data_list.remove(minimum)
print (new_list)