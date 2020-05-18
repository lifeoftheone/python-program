'''a= int(input('enter a number'))
for i in range(1,a+1):
    k=i
    for j in range(1,i+1):
        print(k,end=" ")
        k=k+(a-j)
    print("")
'''

# a=[1,4,5,2,3]
# a.sort(reverse=True)
# print(a)

'''
def sortSecond(val):
    return val[1]


# list1 to demonstrate the use of sorting
# using using second key
list1 = [(1, 2), (3, 3), (1, 1)]

# sorts the array in ascending according to
# second element
list1.sort(key=sortSecond)
print(list1)

# sorts the array in descending according to
# second element
list1.sort(key=sortSecond, reverse=True)
print(list1)

'''

'''
def check(b):
    count = 0
    for i in range(2, a):
        if a % i == 0:
            count += 1
    if count == 0:
        print("no is prime")
    else:
        print("no is not prime")
    return count


a = int(input("enter a number "))
print(check(a))
'''

'''n = int(input("enter a no"))
su = 0
for i in range(1, n ):
    if i % 2 != 0:

        su = su+i
print("sum is ", su)
'''
'''
a = int(input("enter a no"))


def triangle(b):
   
    k = b + 1
    for i in range(1, b + 1):
        for j in range(1, i):
            print(end=" ")
        k = k - 1
        for j in range(1, k):
            if i == 1:
                print("*", end=" ")
            else:
                if 1 < j < k - 1:
                    print(" ", end=" ")
                else:
                    print("*", end=" ")
        print("")
    return ''


print(triangle(a))
'''

a = int(input("enter a no"))


def reverse(b):
    k = b + 1
    for i in range(1, b+1):
        for j in range(1, i):
            print("", end=" ")
        k = k - 1
        for j in range(1, k+1):
            if i == 1:
                print("*", end=" ")
            else:
                if 1 < j < k :
                    print(" ", end=" ")
                else:
                    print("*", end=" ")
        print("")
    return ""


print(reverse(a))







