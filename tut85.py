import pickle


# Pickling a python object

# cars = ["Audi", "BMW", "Maruti Suzuki", "Harryti Tuzuki"]
# file = "tut85_mycar.pkl"
# fileobj = open(file, 'wb')
# pickle.dump(cars, fileobj)
# fileobj.close()

file = "tut85_mycar.pkl"
fileobj = open(file, 'rb')
mycar = pickle.load(fileobj)
print(mycar)
print(type(mycar))
fileobj.close()


# pickle.loads = ?
# https://stackoverflow.com/questions/48498929/what-is-file-like-object-what-is-file-pickle-load-and-pickle-loads#:~:text=loads%20is%20used%20to%20load,was%20loaded%20from%20a%20string.&text=.loads(rawdata)-,pickle.,from%20a%20file%2Dlike%20object.