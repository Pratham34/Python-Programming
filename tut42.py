# def function_name_print(a, b, c, d, e):
#     print(a, b, c, d, e)

def funargs(*args):
    print(args[0])
    # print(args)

def funargs1(normal,*args,**kwargs):
    print(normal)
    for item in args:
        print(item)

# def funargs1(normal,*argsrohan):
#     print(normal)
#     for item in argsrohan:
#         print(item)

# This below lines wrong
# def funargs1(*args,normal):
#     print(normal)
#     for item in argsrohan:
#         print(item)
# as convention is (normal,*args,**kwargs)

har = ["Harry","rohan","shubam","sarthak","hammad"]
# funargs(*har)

normal = "this is normal"
# funargs1(normal,*har)

kw = {"Rohan":"Monitor", "Harry":"Fitness Instructor",
      "The Programmer": "Coordinator", "Shivam":"Cook"}

# def funargs2(normal,*args,**kwargs):
#     print(normal)
#     for item in args:
#         print(item)
#
#     for key,value in kwargs.items():
#         print(key,value)
#
# funargs2(normal,*har,**kw)


def funargs3(normal,*args,**kwargs):
    print(normal)
    for item in args:
        print(item)
    print("\nNow I would Like to introduce some of our heroes")
    for key, value in kwargs.items():
        print(f"{key} is a {value}")

funargs3(normal,*har,**kw)