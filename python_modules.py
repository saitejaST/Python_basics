#math module
import math
from multiprocessing import BufferTooShort           #we use the keyword called import in python to bring up the modules
pi=math.pi
print(pi)
print(math.floor(pi))  #3.5 -------> 3
print(math.ceil(pi))     #3.1 ------> 4

#to find the square root of any number
import math
x = 23802380184022
y=81
print(math.sqrt(y))

#to find the power of the respective number
import math
a=8
b=2
print(math.pow(a,b))

#random module
#to find the number between ints(random numbers)
import random
print(random.randint(1,10))

#choosing between the choices
import random
buffet = ["popcorn","chips","maggie"]
print(random.choice(buffet))

#to get 2 choices
import random
buffest = ["butterchicken","popcorn","cock","maggie","cchips"]
print(random.sample(buffet,k=2))