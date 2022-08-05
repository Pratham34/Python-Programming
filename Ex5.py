# Health Management System
# 3 clients - Harry, Rohan and Hammad

def getdate():
    import datetime
    return datetime.datetime.now()

# Total 6 files
# write a function that when executed takes as input client name
# One more function to retrieve exercise or food for any client

def func():
    a = input("Enter name ")
    if a=="Harry":
        b=0
        func1(b)
    if a=="Rohan":
        b=1
        func1(b)
    if a=="Hammad":
        b=2
        func1(b)

def func1(b):
  z=int(input("For write enter 1, for retrieving enter 2 "))
  if z==1:
    if b==0:
      c=int(input("Write 1 for exercise,2 for diet "))
      if c==1:
          f=open("ex5_Harry_ex.txt","a")
          print("Write to it")
          value=input()
          f.write(str([str(getdate())])+": "+value+"\n")
          print("Successfully written")
      elif c==2:
          f1=open("ex5_Harry_diet.txt","a")
          print("Write to it")
          value = input()
          f1.write(str([str(getdate())]) + ": " + value + "\n")
          print("Successfully written")
    elif b==1:
        c = int(input("Write 1 for exercise,2 for diet "))
        if c == 1:
            f = open("ex5_Rohan_ex.txt", "a")
            print("Write to it")
            value = input()
            f.write(str([str(getdate())]) + ": " + value + "\n")
            print("Successfully written")
        elif c == 2:
            f1 = open("ex5_Rohan_diet.txt", "a")
            print("Write to it")
            value = input()
            f1.write(str([str(getdate())]) + ": " + value + "\n")
            print("Successfully written")
    elif b==2:
        c = int(input("Write 1 for exercise,2 for diet "))
        if c == 1:
            f = open("ex5_Hammad_ex.txt", "a")
            print("Write to it")
            value = input()
            f.write(str([str(getdate())]) + ": " + value + "\n")
            print("Successfully written")
        elif c == 2:
            f1 = open("ex5_Hammad_diet.txt", "a")
            print("Write to it")
            value = input()
            f1.write(str([str(getdate())]) + ": " + value + "\n")
            print("Successfully written")
  if z==2:
      if b == 0:
          c = int(input("Write 1 for exercise,2 for diet "))
          if c==1:
             f3=open("ex5_Harry_ex.txt")
             for i in f3:
               print(i,end="")
          elif c==2:
              f3 = open("ex5_Harry_diet.txt")
              for i in f3:
                  print(i, end="")

      if b == 1:
          c = int(input("Write 1 for exercise,2 for diet "))
          if c==1:
             f3=open("ex5_Rohan_ex.txt")
             for i in f3:
               print(i,end="")
          elif c==2:
              f3 = open("ex5_Rohan_diet.txt")
              for i in f3:
                  print(i, end="")

      if b == 2:
          c = int(input("Write 1 for exercise,2 for diet "))
          if c==1:
             f3=open("ex5_Hammad_ex.txt")
             for i in f3:
               print(i,end="")
          elif c==2:
              f3 = open("ex5_Hammad_diet.txt")
              for i in f3:
                  print(i, end="")


func()


# Another same type of program possible - check at :
# https://www.codewithharry.com/videos/python-tutorials-for-absolute-beginners-37/