# Dictionary is nothing but key value pairs
d1 = {}
# print(type(d1))
d2 = {"Harry":"Burger",
      "Rohan":"Fish", "SkillF":"Roti",
      "Shubham":{"B":"maggie" , "L":"roti" , "D" : "Chciken"}}
print(d2["Shubham"])
print(d2["Rohan"])
print(d2["Shubham"]["B"])
print(d2)
d2["Ankit"] = "Junk Food"
print(d2)
d2[45] = "Junk"
print(d2)

del d2[45]
print(d2)

d3 = d2
del d3["Harry"]
print(d2)

d3 = d2.copy()
del d3["Rohan"]
print(d2)

print(d2.get("Rohan"))

d2.update({"Leena" : "Muttom"})
print(d2)

print(d2.keys())
print(d2.items())