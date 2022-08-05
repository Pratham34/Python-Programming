f = open("tut31_harry.txt")

# print(f.readlines())
print(f.readline())

f.seek(11)
print(f.tell())
print(f.readline())
# print(f.tell())

print(f.readline())
# print(f.tell())
f.close()