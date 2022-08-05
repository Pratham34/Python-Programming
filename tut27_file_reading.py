# f = open("tut27_harry.txt","rt")
f = open("tut27_harry.txt")
# print(f.readlines())
print(f.readline())
# print(f.readline())
# print(f.readline())

# content = f.read()
# print(content)
# for char in content:
#     print(char)

# for line in f:
#     print(line,end="")

# content = f.read(34455)
# print("1", content)
#
# content = f.read(34455)
# print("2", content)
f.close()