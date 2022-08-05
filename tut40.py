# String formatting in python
me = "Harry"
a = "this is %s"%me
print(a)

a1 = 3
a2 = "this is %s %s"%(me,a1)
print(a2)

b1="This is {} {}"
b=b1.format(me,a1)
print(b)

# b1="This is {1} {0}"
# b=b1.format(me,a1)
# print(b)

# F-strings
c= f"this is {me} {a1} {4*65}"
print(c)

import math
c1= f"this is {me} {a1} {math.cos(65)}"
print(c1)



