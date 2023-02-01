# ****** day9 ******
# Typecasting in python
'''
Explicit Typecasting
It can be achieved with the help of Python’s built-in type 
conversion functions such as 
int(), float(), hex(), oct(), str(), etc .
'''
string = "15"
number = 7
string_number = int(string) #throws an error if the string is not a valid integer
sum= number + string_number
print("The Sum of both the numbers is: ", sum)

"""
Implicit Typecasting
Python converts a smaller data type to a higher data type 
to prevent data loss.
"""
# Python automatically converts a to int
a = 7
print(type(a))
# Python automatically converts b to float
b = 3.0
print(type(b)) 
# Python automatically converts c to float as it is a float addition
c = a + b
print(c)
print(type(c))
print("\n")

# ****** day10 ********
# taking user input in python
'''	
variable=input()
variable=int(input())
variable=float(input())
'''
x = "10"
y = "8"

print("result of concatination " + x+y)
print("result after typecasting: ")
print(int(x) + int(y))

a=input("Enter the name: ")
print(a)

print("hai ki nahi")