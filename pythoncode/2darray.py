x = int(input("enter the number of row"))
y = int(input("enter the number of col"))
z = [[0 for j in range (0,y)]for i in range (0,x)]
for i in range(0,x):
     for j in range(0,y):
         z[i][j]= i*j
print(z)
