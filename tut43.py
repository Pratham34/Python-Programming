import time

initial = time.time()

k = 0
while (k < 5):
    print("This is harry bhai")
    time.sleep(2)
    k += 1
print("While loop ran in", time.time() - initial, "Seconds")

initial2 = time.time()
for i in range(5):
    print("This is harry bhai")
print("For loop ran in", time.time() - initial2, "Seconds")

# localtime = time.asctime(time.localtime(time.time()))
# print(localtime)

# SHAYAD aisa hota h ki time.time() jo h vo ek particular date time se no.of ms passed return karta h....time.localtime() usko as a tuple ke roop me return karta h islie time.asctime() use kiya taaki vo us tuple ko hatake presentable format me date time return kar de !!!