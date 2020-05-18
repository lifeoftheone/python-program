st = input("enter the string")
li = []
for i in range(len(st)):
    if(st[i-1] == " "):
        li.append("$")
    else:
        li.append(st[i])
print(li)
for i in li:
    print(i, end=" ")

