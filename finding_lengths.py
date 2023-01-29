x=[1,2,3,4,5]
y=len(x)
print(y)
if(6 in x):
    print("6 is present")
else:
    print("6 is not present")

x=[1,2,3,4,5]
y=len(x)
z=2
if (z in x):
    print("{} is present".format(z))
else:
    print("{} is not present".format(z))


x=[1,2,3,4,5]
y=len(x)
z=8
if (z in x):
    if(z%2!=0):
     print("{} is present and it is a odd number".format(z))
    else:
        print("{} is present and it is a even number".format(z))
else:
    print("{} is not present".format(z))

x=[1,2,3,4,5]
y=x[0]
print(y)
if(y<2):
    print("x is less than 2")
elif(y==3):
    print("x is equal to the number 3")
else:
    print("x is not determined")

x=("Saiteja")
y=len(x)
print(y)
if(y==0):
    print("the lenght of the statement is 0")
else:
    print("The length of the statement is {}".format(y))