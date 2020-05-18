a = int(input("enter value for elements in list"))
data_list = []
data_mul = []
data_sumply = []
for i in range(a):
    b = int(input("enter the values"))
    data_list.append(b)
print(data_list)


def multiply(func):
    def sumply(h, n):
        for h in range(a):
            if (h == a - 1):
                n = data_list[h] * 10
            else:
                n = (data_list[h]) + (data_list[h + 1] * 10)
            data_sumply.append(n)


print(data_sumply)

'''
@multiply
def sum(c):
    for j in range(a):
         if (j==a-1):
             m=data_list[j]
             data_mul.append(m)
         else:
          m=data_list[j]+data_list[j+1]
          data_mul.append(m)
sum(data_list)
print(data_mul)'''
