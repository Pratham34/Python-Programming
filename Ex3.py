n=18

# no of guesses 9
# print no of guesses
# No of guesses he took to finish
# game over
guess=9
for x in range(9):
    a = int(input())
    if a>18:
        print("Reduce your guess value")

    elif a<18:
        print("Increase your input guess value")
    else :
        print("Correctly guessed....Game over")
        break
    guess -= 1
    print("No. of guesses left", guess)
    if guess == 0:
        print("All ur chances are over.Game over")
