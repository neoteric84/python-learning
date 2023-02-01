# ******** day11 ********
# What are strings?

name = "Harry"
print("Hello, " + name)
print('He said, "I want to eat an apple".')

# multiline strings
a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)

# string like an array 
print(name[0])
print(name[1])
# Looping through the string
for x in name:
	print(x)

# ***** day12 ******
# String Slicing & Operations on String
fruit = "Mango"
len1 = len(fruit)
print("Mango is a", len1, "letter word.")

# string as an array
pie = "ApplePie"
print(pie[:5])
print(pie[6])	#returns character at specified index

# slicing examples
pie = "ApplePie"
print(pie[:5])      #Slicing from Start
print(pie[5:])      #Slicing till End
print(pie[2:6])     #Slicing in between
print(pie[-8:])     #Slicing using negative index

# loop through a string 
alphabets = "ABCDE"
for i in alphabets:
    print(i)

# ****** day13 ******    
# string methods
# check more on:
# https://www.codewithharry.com/videos/python-100-days-of-code-13/

str1 = "AbcDEfghIJ"
print(str1.upper())

str1 = "AbcDEfghIJ"
print(str1.lower())

# The strip() method removes any white spaces before and after the string.
str2 = " Silver Spoon "
print(str2.strip)

# the rstrip() removes any trailing characters. 
str3 = "Hello !!!"
print(str3.rstrip("!"))

str2 = "Silver Spoon"
print(str2.replace("Sp", "M"))

# The split() method splits the given string at 
# the specified instance and returns 
# the separated strings as list items
str2 = "Silver Spoon"
print(str2.split(" "))      #Splits the string at the whitespace " ".

# The count() method returns the number of times 
# the given value has occurred within the given string
str2 = "Abracadabra"
countStr = str2.count("a")
print(countStr)

str1 = "Welcome to the Console !!!"
print(str1.endswith("!!!"))

str1 = "He's name is Dan. He is an honest man."
print(str1.find("is"))


