# ***** day15 ********
# exercise2: good morning sir
import time
timestamp = time.strftime('%H:%M:%S')
print(timestamp)
timestamp = time.strftime('%H')
print(timestamp)
timestamp = time.strftime('%M')
print(timestamp)
timestamp = time.strftime('%S')
print(timestamp)

# https://docs.python.org/3/library/time.html#time.strftime


# ****** day16 ******
# Match the case statements 
'''
match variable_name:
            case ‘pattern1’ : //statement1
            case ‘pattern2’ : //statement2
            …            
            case ‘pattern n’ : //statement n
'''
x = 4
# x is the variable to match
match x:
    # if x is 0
    case 0:
        print("x is zero")
    # case with if-condition
    case 4 if x % 2 == 0:
        print("x % 2 == 0 and case is 4")
    # Empty case with if-condition
    case _ if x < 10:
        print("x is < 10")
    # default case(will only be matched if the above cases were not matched)
    # so it is basically just an else:
    case _:
        print(x)

# ****** day17 ******
# for loops in python 
# iterating ovar a string 
name = 'Abhishek'
for i in name:
    print(i, end=", ")	
# we can use end=" " to separate characters with space on
print(" ")
# iterating over a list 
colors = ["Red", "Green", "Blue", "Yellow"]
for x in colors:
    print(x)
    for i in x:
    	print(i)

# range():
for k in range(5):
    print(k)

print("num from 4 to 8")
for k in range(4,9):
    print(k)

print("numbers from 1 to 20 with increment of 2")
for f in range(1,20,2):
	print(f)

# ******** day18 ********
# while loops in python 
print("this is written using while loop")
count = 5
while (count > 0):
  print(count)
  count = count - 1

# Else with While Loop
print("new program")
x = 5
while (x > 0):
    print(x)
    x = x - 1
else:
    print('counter is 0')

# emmulate the do-while loop 
# there is no do-while loop in python 
# do {
# 	loop body;
# }while(condition);

# ****** day19 ******
# break and continue in python
print("break statement")
for i in range(1,101,1):
    print(i ,end=" ")
    if(i==50):
        break
    else:
        print("Mississippi")
print("Thank you")

print("continue statement")
for i in [2,3,4,6,8,0]:
    if (i%2!=0):
        continue
    print(i)

# below is the do while emmulation
i=0 
while True:
	print(i)
	i=i+1
	if(i%100 == 0):
		break

 




