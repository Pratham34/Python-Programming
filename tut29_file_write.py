f = open("tut29_harry.txt", "w")
a = f.write("Harry bhai bahut achhe hain\n")
print(a)
f.close()

# f = open("tut29_harry2.txt", "a")
# a = f.write("Harry bhai bahut achhe hain\n")
# print(a)
# f.close()


# Handle read and write both
f = open("tut29_harry2.txt", "r+")
print(f.read())
f.write("thank you")