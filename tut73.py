"""
Iterable - __iter__() or __getitem__()
Iterator - __next__()
Iteration -

"""

# Any function that contains a yield keyword is termed a generator. Hence, yield is what makes a generator.
def gen(n):
    for i in range(n):
        yield i

g = gen(3)
print(g)
# print(g.__next__())
# print(g.__next__())
# print(g.__next__())

# print(g.__next__())

for i in g:
    print(i)

h = "harry"
# h = 546546
ier = iter(h)
print(ier.__next__())
print(ier.__next__())
print(ier.__next__())

# for c in h:
#     print(c)

# print([None]*4)
# https://stackoverflow.com/questions/43627405/understanding-getitem-method