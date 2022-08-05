
import time
from functools import lru_cache

# Jaise ham maxsize = 3 daalte h to kya hoga ki vo sirf recent 3 calls ki return values ko hi save karega cache me !! .... to some_work(3) vaali return value cache me save nahi hogi agar maxsize = 3 daale ham

@lru_cache(maxsize=32)
def some_work(n):
    #Some task taking n seconds
    time.sleep(n)
    return n

if __name__ == '__main__':
    print("Now running some work")
    some_work(3)
    some_work(1)
    some_work(6)
    some_work(2)
    print("Done... Calling again")
    input()
    some_work(3)
    print("Called again")

# Agar mai ye lru_cache decorator use naa karta to input ke baad waale some_work(3) ko bhi utna hi time lagta jitna pehle waale ko laga tha