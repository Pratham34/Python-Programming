# Problem Statement:-
# Take age or year of birth as an input from the user. Store the input in one variable. Your program should detect whether the entered input is age or year of birth and tell the user when they will turn 100 years old. (5 points).
#
# Here are a few instructions that you must have to follow:
#
# Do not use any type of module like DateTime or date utils. (-5 points)
# Users can optionally provide a year, and your program must tell their age in that particular year. (3points)
# Your code should handle all sorts of errors like :            (2 points)
# You are not yet born
# You seem to be the oldest person alive
# You can also handle any other errors, if possible!

print("Enter age or yob ")
isAge = False
isYear = False
a = int(input())
age = 0

if len(str(a)) == 4:
    isYear = True
    age = 2022 - a

else :
    isAge = True
    age = a
    Yob = 2022 - age

if a<1900 and isYear:
    print("You seem to be the oldest person alive.")
    exit()

if a>2022 and isYear:
    print("You are not yet born")
    exit()


b = 100 - age
print(f"You will turn 100 after {b} years")

interestedYear = int(input("Enter the year in which u want to know ur age "))
print(f"Your age in {interestedYear} will be",interestedYear-Yob)