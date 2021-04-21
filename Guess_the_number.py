Hidden_number = 24
print("Welcome to the Guess The Number Game!!")
for i in range(1, 6):
    print("Enter Guess", int(i), ": ")
    userInput = int(input())
    if userInput == Hidden_number:
        print("Voila! you've guessed it right,", userInput, "is the hidden number!")
        print("Congratulations!!!!! You took", i, "guesses to win the game!")
        break
    elif 0 < userInput < 24:
        if 20 < userInput < 24:
            print("You are very close to get it right! Guess a higher number now!")
        else:
            print("You've guessed it very less buddy!")
    else:
        if 24 < userInput < 28:
            print("You are very close to get it right! Guess a lower number now!")
        else:
            print("You've gone too far away!")
    print("You are left with ", (5-i), "guesses")
print("GAME OVER!")
print("The Hidden_number was: ", Hidden_number)