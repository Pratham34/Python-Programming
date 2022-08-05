var1 = "Hello world"
var2 = 4
var3 = 35.8
var4 = 7
print(type(var1))
print(type(var2))
print(type(var3))
"""
For type casting,
int()
float()
str()
"""

print(int(var2)+int(var4))

print(10*"Hello world\n")

print(100* str(int(var2)+int(var4)))

print("Enter your number")
inpnum = input()
print("You entered ",int(inpnum)+10)

print("Enter First Number : ")
num1= input()
print("Enter Second Number : ")
num2=input()
print("The Sum is",int(num1)+int(num2)) #It will give output as sum of two numbers.