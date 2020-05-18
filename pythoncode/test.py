a = int(input("enter a number"))
b = 0
for i in range(1, a + 1):
    for j in range(1, i + 1):
        b += 1
        print(b, end=',')
    print()
