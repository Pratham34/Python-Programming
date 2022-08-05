# try me ham chiz try karte h run karne ki agar nahi ho paati try me run aur exception (error) aata h to fir ham except me use handle karte hai !!

# Chahe try run ho ya except lekin fiinally me jo chize h vo to run hoegi hi hoegi hamesha

# Aur else ka matlab h ki except run hoga to else vaala part nahi hoga run.... aur except run nhai hoga agr to else vaala part run ho jaaega !!

# Note : aap ek se zyada except statement bhi use kar sakte h...in case jaise alag alag type ke errors aa sakte h aur probably aap fir alag alag tarike se usey handle karna chahenge islie multiple except statement lag jaaenge us case me !!


f1 = open("ex5_Harry_ex.txt")

try:
    f = open("does2.txt")

except EOFError as e:
    print("Print eof error aa gaya hai", e)

except IOError as e:
    print("Print IO error aa gaya hai", e)

else:
    print("This will run only if except is not running")

finally:
    print("Run this anyway...")
    # f.close()
    f1.close()

print("Important stuff")
