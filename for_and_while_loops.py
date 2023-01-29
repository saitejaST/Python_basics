for i in range(1,10):
    print(i)

#printing odd numbers
for numbers in range(1,25,2):
    print(numbers)

#priniting even numbers
for numbers in range(0,25,2):
    print(numbers)

#while loop(odd)
i=1
while(i<25):   #relational operator
    print(i)
    i+=2     #assignment opearator
#even
i=0
while(i<25):
    print(i)
    i+=2

#break statement
for i in range(1,10):
    if(i==7):
        break
    print(i)

#ex2
for i in range(1,999):
    if(i==555):
        break
    print(i)

#continue statement
for i in range (1,10):
    if(i%2==0):
     continue
    print(i)

#ex2
for i in range(1,10):
    if(i%2!=0):
      continue
    print(i)

#pass statements
def sum():
    return 1+3
def difference():
    pass
print(sum())