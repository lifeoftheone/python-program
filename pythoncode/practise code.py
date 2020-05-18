# write a program to print a triangle of numbers by creating a function
"""
a = int(input("enter a no"))

def reverse(b):
    for i in range(1, b + 1):
        for j in range(0, b - i):
            print(end=" ")
        for j in range(1, i + 1):
            if i == b:
                print("*", end=" ")
            else:
                if 1 < j < i:
                    print(" ", end=" ")
                else:
                    print("*", end=" ")
        print()
    return ""


print(reverse(a))
"""

# bubble sort example

l = [56,45,24,98,75,42,15,35,68,42,95]


def bubblesort(l):
    for i in range(len(l) - 1, 0, -1):
        for j in range(i):
            if l[j] > l[j + 1]:
                temp = l[j]
                l[j] = l[j + 1]
                l[j + 1] = temp
    print(l)
    return""

print(bubblesort(l))