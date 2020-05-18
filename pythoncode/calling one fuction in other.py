a = int(input("enter first no"))
b = int(input("enter secound no"))


def sum(x, y):
    c = x + y
    return c


def avrage(x, y):
    d = sum(x, y) / 2
    return d


print(sum(a, b))
print(avrage(a, b))
