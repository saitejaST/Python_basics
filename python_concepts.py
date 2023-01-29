#first programme of python
from argparse import BooleanOptionalAction
from gettext import install
from operator import truediv
from pickletools import int4
from re import T
from selectors import EpollSelector
import this


print("Hello world")

if(5>2):
    print("FIve is greater than two")
else:
    print("Five is less than two")

"""this is a comment """
print("Hello world")

x=4
y="Hello"
print(x)
print(y)

#specification of data types
x=str(3)
print(x)
y=int(3)
print(y)
z=float(3)
print(z)

x=5
y="hello world"
z=4.57
print(type(x))
print(type(y))
print(type(z))

fruits=["apple","bananna","orange"]
x,y,z=fruits
print(x)
print(y)
print(z)

x="python is awesome and its easy to write"
print(x)

x="python is"
y="awsome"
z="easy to write"
print(x+y+z)

x=5
y=10
print(x+y)
#to assign multiple variables we have to keep comma
x=5
y="string"
print(x,y)
#global variables
x="awesome and it is very easy to write compared to c and c++"
def myfunc():
    print( "python is " + x)
myfunc()
#local variables
x="awesome"
def myfunc():
    x="easy"
    print("Pyhton is "+ x)  #x=easy is a local variable so it can be accessed only inside the function
myfunc()
print("pyhton is "+ x)      #x=awesome is a global variable so it can be accessed anywhere outside the function

def myfunc():
    global x
    x="fantastic"
myfunc()
print("python is "+ x)

x="awesome"
def myfunc():
    global x    #it can overwrite the global variable by writing as global
    x="fantastic"
myfunc()
print("Python is "+x)

x="awesome"
def myfunc():
    global x
    x="fantastic"
    print("Python is "+x)  #two times python is fantastic
myfunc()
print("Pyhton is "+x)

x=("apple","bananan","orange")
print(type(x))

x=1
y=44.4
z=3+5j
a=float(x)
print(a)
print(type(a))
b=int(y)
print(b)
print(type(b))
c=complex(z)
print(c)
print(type(c))

#random module
import random
print(random.randrange(1,1000))

#assinging strings and arrays and finding lengths
a='''Hello world welcome to the python programming and i am your tutotor hence i am gonna teach you the basics'''
print(a)
print(a[4])
b="Hello world welcome to the python programming"
print(b[1])
c="Hello user"
print(len(c))

#checking a paticular name in the string
text="hello world this is python programming which is famously known as one of the easiest and famous language"
print("python" in text)

text="Hello world welcome to the python programming which is famously known as one of the easiest an famous language"
if("python" in text):
    print("Yes","Python is present in the text")

text="hello world welcome to the python programming language which is famously known as one of the easiest and famous language"
print("expensive" in text)

text="hello world welcome to the python programming language which is famously known as one of the easiest and famous language"
if("expensive" not in text):
    print("expensive is not present in the given text")
#assigning the for loops
for x in "banana":
    print(x)
#slice (specify the start character and the end character for slicing the character)
a="hello world"
print(a[2:5])
a="hello world"
print(a[:5])
#giving negative sign indicates to start the character from the end
a="hello world"
print(a[-5:-2])
#modify the strings
a="hello world"
print(a.upper())
print(a.lower())
a="HELLO WORLD"
print(a.lower())
print(a.upper())

#combination of numbers and strings
age=36
text="i am john and my age is {}"
print(text.format(age))

quantity=100
itemno=567
price=49.95
myorder="i have given a quantity of {} and the item no is {} the price for the given myorder is {}"
print(myorder.format(quantity,itemno,price))

text="we are so called \"viking\" are present here long ago"

text="hello world welcome to the c++ programmee"
print(text.find("welcome"))

a=33
b=100
if(a>b):
    print("b is greater than a")
else:
    print("B is less than a")

print(bool("Hello"))  
print(bool("15"))
print(["apple","banana","orange"])

class myclass():
    def _len_(self):
        return 0
myobj=myclass()
print(bool(myobj))

def myfunction():
    return True
print(myfunction())

def myfucntion():
    return True
if(myfucntion()):
    print("Yes it is true")
else:
    print("no It is false")
#defining true or false using instance value

x=2000
print(isinstance(x,int))     #it return true value coz it is int data type variable
print(isinstance(x,float))   #it returns false value coz it is float value data tyep
 
#Lists concepts
list=["apples","bananas","oranges","apples","grapes"]
print(list)
print(len(list))   #defines the number of items in the list
fruitlist=["apples","banans","oranges","strawberry"]   #list can be any type of data
numberlist=[10,20,30,40]
booleanlist=[True,False,True]
combinedlist=["apples",20,True,"bananas"]
print(combinedlist)
print(type(combinedlist))

thislist=list(("apples","bananas","oranges"))
print(thislist)
print(thislist[2])   #accesing the list
print(thislist[-1])

thislist=["apples","banana","oranges","grapes"]
if("apples"in thislist):
    print("Yes apples are present in the list")
thislist[0]="nicee"
print(thislist)

thislist=["apples","grapes","magoes","kiwi","hello"]
thislist[2:4]=["blackmamba","blackmangoes"]     #2= it starts from 0 and 4 starts from 1
print(thislist)

thislist=["apples","bannas",'cherry']
thislist[1:3]=["blackgrapes","magoes"]
print(thislist)

thislist=["apples","bannas",'cherry']
thislist[1:3]=["watermelon"]
print(thislist)

#inserting the thing without changing anything
thislist=["apples","grapes","banana"]
thislist.insert(2,"watermelon")
print(thislist)

#to add the item at the end of the list is
thislist=["apples","oranges","hello"]
thislist.append("watermelon")
print(thislist)
#merging of two lists
thislist1=["apple","oranges","grapes","magoe"]
thislist2=["helllo","blackgrapes","watermelon"]
thislist1.extend(thislist2)
print(thislist1)

list1=["apples","oranges"]
tuple1=("black grapes","grapes")
list1.extend(tuple1)
print(list1)

thislist=["apples","oranges","grapes","mangoes"]
thistuple=("hallow","black grapes","grapes")
thislist.extend(thistuple)
print(thislist)
#removing a item
thislist=["apples","grapes","banana"]
thislist.remove("banana")
print(thislist)
thislist=["apples","grapes","banana"]
thislist.pop(1)   #it starts like 0,1,2,3,4
print(thislist)
thislist=["apples","bannaa","oranges"]
thislist.pop()    #if we dont specify anything pop removes the last word
print(thislist)

#del is similar to the pop word
thislist=["apples","grapes","bannana","oranges"]
del thislist[0]
print(thislist)

thislist=["apples","grapes","banana"]
thislist.clear()
print(thislist)


thisline=["hello","world","my","name","is","python"]
del thisline[0]
print(thisline)

x=4
x**=2
print(x)
print(x<5&x>10)

list1=["apples","bananas","oranges","grapes","kiwi","papaya"]
print(list1[:4])
print(list1[-4:-1])

print(type(list1))

mylist1=["apples",12,True,33.33]
print(type(mylist1))
list1.extend(mylist1)
print(list1)

checklist=["apples","oranges","mangoes"]
if "bananas" in  checklist:
    print("Yes, bananas is present in the list")
else:
    print("bananas are not present in the given list")

#list comperhension

fruits=["apples","bananas","oranges","mangoes"]
newlist=[]
for x in fruits:
    if "a" in x:
        newlist.append(x)
print(newlist)