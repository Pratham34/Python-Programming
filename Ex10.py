
# pickle
# Use requests module to download the iris dataset

import pickle

with open("ex10_iris.txt","r") as f:
    data = f.read()

# print(data)

# l1=data.split("\n")
# print(l1)

l2 = [item.split(",") for item in data.split("\n") if len(item)!=0]
# print(l2)

with open("ex10_myiris.pkl", "wb") as f:
    pickle.dump(l2, f)


# To read this pickle file you can use this code
# import pickle
# with open("ex10_myiris.pkl", "rb") as f:
#     print(pickle.load(f))

