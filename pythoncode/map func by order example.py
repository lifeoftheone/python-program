order=[[34587, 'lern python', 'mark lutz', 4, 40.95],[98762,'programming python', 'mark lutz',5, 56.80],
       [77226,'Head first python', 'Paul berry', 3,32.95],[88112,'einfuhrung in python 3','Bernd Klein', 3, 24.99]]
minorder=100
li= list(map(lambda x:( x[0], x[3]* x[4]) ,order))
print(li)
invoice=list(map(lambda x: x if x[1]>=minorder else(x[0],x[1]+10), li))
print(invoice)