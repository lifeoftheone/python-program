str = input("enter a string")
a = input("enter char to be found")
for i in range(len(str)):
    if(str[i]==a):
        print(i+1)
        break
count = 0
for i in range(len(str)):
    if(str[i]==a):
        count = i
print(count+1)

