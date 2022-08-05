# When we us with to open file as f , then we dont need to write the code for closing file , 'with' will automatically do it.
with open("tut31_harry.txt") as f:
    a = f.readlines()
    print(a)


# Question of the day - Yes or No and why?
f = open("tut31_harry.txt", "rt")
v = f.readline()
print(v)
f.close()


# With open(“file1txt”) as f, open(“file2.txt”) as g