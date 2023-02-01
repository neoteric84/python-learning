# **** day14 *****
# if-else statements
'''
if
if-else
if-else-elif
nested if-else-elif.
'''
applePrice = 210
budget = 200
if (applePrice <= budget):
    print("Alexa, add 1 kg Apples to the cart.")
else:
    print("Alexa, do not add Apples to the cart.")

# Conditional operators 
# >, <, >=, <=, ==, != 
a = int(input("Enter your age: "))
print("Your age is: ", a) 	
# check here how string and int is concatenated

if(a>=18): 
	print("You can drive. ")
elif(a>10 and a<18):
	print("You can drive a bicycle. ")
else:
	print("You cannot drive. ")

# nested if-else-elif

num = int(input("Enter an integer: "))
if(num < 0):
	print("Number is negative.")
elif(num > 0):
	if (num <=10):
		print("Number is between 1-10.")
	elif(num >10 and num<=20):
		print("Number is between 11-20.")
	else:
		print("Number is greater than 20.")
else:
	print("Number is zero.")


