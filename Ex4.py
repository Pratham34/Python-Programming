# Exercise 4
# Pattern Printing
# Input = Integer n
# Boolean = True or False
#
# True n=4
# *
# **
# ***
# ****
#
# False n=4
# ****
# ***
# **
# *

# A possible way
# n = int(input())
# a = int(input())
#
# if a==1:
#     for i in range(0,n+1):
#         print(i*"*",end="")
#         print()
# if a==0:
#     for i in range(n,0,-1):
#         print(i*"*",end="")
#         print()


# Another possible way
a = int(input("please add number of line you want to print "))
b = bool(int(input("please add 0 for False ")))


def star(a, b):
    if b == True:
        c = 1
        while c <= a:
            print(c * "*")
            c = c + 1
    else:
        while a > 0:
            print(a * "*")
            a = a - 1


star(a, b)