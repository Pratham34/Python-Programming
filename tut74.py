# ls = []
# for i in range(100):
#     if i%3 == 0:
#         ls.append(i)

# List comprehensions
# ls = [i for i in range(100)]
ls = [i for i in range(100) if i%3==0]
print(ls)


# Dictionary comprehensions
# dict2 = {i:f"item{i}" for i in range(1,10001) if i%100==0}
# print(dict2)

dict1 = {i:f"item{i}" for i in range(5)}
# print(dict1)
dict3 = {value:key for key,value in dict1.items()}
print(dict1,"\n",dict3)


# Set comprehensions  ( for making set comprehensions we use curly braces )
# dresses = {dress for dress in ['dress1','dress2','dress1','dress1','dress2']}
# print(dresses)
# print(type(dresses))


# Generator comprehensions ( for making generator comprehensions we use paranthesis )
evens = (i for i in range(100) if i%2==0)
print(evens)
# print(evens.__next__())
# print(evens.__next__())

for item in evens:
    print(item)



# no_of_list = int(input("How many items add in a list: "))
# input_string = input("Enter a list element separated by space ")
# list = input_string.split(" ")
# t = int(input("Which type of comprehension you use 1. List Comprehension 2.Dictionary Comprehension 3. Set Comprehension "))
# if t==1:
#     ls = [i for i in list]
#     print(ls)
#     print(type(ls))
# elif t==2:
#     dict1 = {f'item{i}': i for i in list}
#     print(dict1)
#     print(type(dict1))
# elif t==3:
#     s ={i for i in list}
#     print(s)
#     print(type(s))





# Another way
# n = int(input("How many items do you want to add to your inventory: "))
# i = 0
# l = []
# while(i<n):
#     a = input("Enter the item: ")
#     l.append(a)
#     i += 1
#
# choice = int(input("Press '1' for generating a list comprehension\nPress '2' for generating a set comprehension\nPress '3' for generating a generator comprehension: "))
#
# if choice == 1:
#     list = [item for item in l]
#     print(list)
#
# elif choice == 2:
#     set = {item for item in l}
#     print(set)
#
# elif choice == 3:
#     gen = (item for item in l)
#     for c in gen:
#         print(c)