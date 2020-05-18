def fabonacci(n):
    if n==1 or n==2:
        return 1
    return fabonacci(n-1) + fabonacci(n-2)
for i in range(1,20):
    print (fabonacci(i))