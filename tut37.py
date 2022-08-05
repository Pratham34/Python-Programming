# Lambda functions or anonymous functions

# def add(a, b):
#     return a+b
#

minus = lambda x, y: x-y
# is same as
# def minus(x, y):
#     return x-y
#

print(minus(9, 4))

# def a_first(a):
#     return a[1]

a =[[1, 14], [5, 6], [8,23]]
# a.sort(key=a_first)
a.sort(key=lambda x:x[1])   # means koi bhi list dogee as a paarameter too uska SECOND element return karega YE FUNCTION
print(a)