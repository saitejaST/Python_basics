#basics of python
print("hello world")

a=5
b=7
print(a+b)
#drawing a shape just simple shape using printf
print("The below figure is triangle(isoceles triangle")
print("    /|")
print("   / |")
print("  /  |")
print(" /   |")
print("/____|")

#assigining variables 
char_name="saiteja"
char_age="18"
ismale=False
print("there was a man called as "+char_name+" this was her name",)
print("his age was "+char_age+" this was her age")
#converting the given statement into upper case capital letters and into lower case smaller letters
phrase="girrafe academy is best"
print(phrase)
print(phrase+" and it is cool")
print(phrase.upper())
print(phrase.lower())
print(phrase.isupper())
print(phrase.islower())
print(phrase.upper().isupper())
print(phrase.lower().islower())
print(phrase.upper().islower())
print(phrase.lower().isupper())
print(len(phrase))

#to know the length of string and plotting variables and knowing the position of variables
phrase="Giraffe academy"
print(phrase)
print(len(phrase))
print(phrase[4])
print(phrase.index("a"))
print(phrase.index("academ"))
print(phrase.index("Giraffe"))