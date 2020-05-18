a=int(input("enter the number to be checked"))
reverse=0
original=a
rem=0
while(a!=0):
    rem=a%10
    reverse=(reverse*10)+rem
    a=int(a/10)
print(reverse)
if(original==reverse):
        print("integer is pallandrom")
else:
      print("integer is not pallandrom")