

# == - value equality - Two objects have the same value
# is - reference equality - Two references refer to the same object


# Task:
a =[6, 4 , "34"]
b = [6, 4 , "34"]
print(b==a)
print(b is a)

c=[0,1,2]
d=c
print(c==d)
print(c is d)

e=[0,1,2]
f=e[:]
print(e==f)
print(e is f)

