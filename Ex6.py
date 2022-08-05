# Snake water gun
# Create a snake water gun game in Python! Search Snake water gun game in google if you need help on rules and how to play the game!

import random


b=["S","W","G"]

i=1
score_user=0
score_comp=0
chance = 10
no_of_chance = 0

while i<=10:
    c = random.choice(b)
    v = input("Select S ,W or G ")
    u = v.capitalize()
    if u=="W" and c=="S":
        print("computer chose ",c)
        print("comp wins")
        score_comp+=1
        print(f"Now, user points - {score_user} and computer points - {score_comp}")
        i += 1
    elif u=="W" and c=="G":
        print("computer chose ", c)
        print("user wins")
        score_user+=1
        print(f"Now, user points - {score_user} and computer points - {score_comp}")
        i += 1
    elif u == "W" and c == "W":
        print("Round tie..play again")
        continue
    elif u=="G" and c=="W":
        print("computer chose ", c)
        print("comp wins")
        score_comp += 1
        print(f"Now, user points - {score_user} and computer points - {score_comp}")
        i += 1
    elif u=="G" and c=="S":
        print("computer chose ", c)
        print("user wins")
        score_user += 1
        print(f"Now, user points - {score_user} and computer points - {score_comp}")
        i += 1
    elif u=="G" and c=="G":
        print("Round tie..play again")
        continue
    elif u=="S" and c=="W":
        print("computer chose ", c)
        print("user wins")
        score_user += 1
        print(f"Now, user points - {score_user} and computer points - {score_comp}")
        i += 1
    elif u=="S" and c=="G":
        print("computer chose ", c)
        print("comp wins")
        score_comp += 1
        print(f"Now, user points - {score_user} and computer points - {score_comp}")
        i += 1
    elif u=="S" and c=="S":
        print("Round tie..play again")
        continue
    else:
        print("you have input wrong \n")
        continue

    no_of_chance = no_of_chance + 1
    print(f"{chance - no_of_chance} chances are left out of {chance} \n")

if score_comp>score_user:
    print("\nComputer wins the game")
elif score_comp==score_user:
    print("\nTie")
else:
    print("\nUser wins the game")
