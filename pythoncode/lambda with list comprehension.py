x=lambda y: y*y
li=[x(m)for m in range (9) if x(m)%3==0]
print(li)