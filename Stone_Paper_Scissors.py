import random
count = 1
user_win, comp_win, Tied_rounds = 0,0,0
while count <= 10:
    lst = ['Stone', 'Paper', 'Scissors']
    comp_choice = random.choice(lst)
    a = int(input("Enter 1 for Stone, 2 for Paper or 3 for Scissors! "))
    b = {1: 'Stone', 2: 'Paper', 3: 'Scissors'}
    if a not in (1,2,3):
        print("Wrong Input!")
        break
    elif b[a] == comp_choice:
        print("TIE")
        Tied_rounds += 1
    else:
        if (b[a] == 'Stone' and comp_choice == 'Scissors') or (b[a] == 'Paper' and comp_choice == 'Stone') or (b[a] == 'Scissors' and comp_choice == 'Paper'):
            print("User Wins")
            user_win += 1
        else:
            print("Comp wins")
            comp_win += 1
    count += 1
if user_win > comp_win:
    print("User Wins The game")
elif comp_win > user_win:
    print("Comp Wins The game")
else:
    print("Nobody wins the game")
# print("User Wins", user_win)
# print("Comp Wins", comp_win)
print("TIED Rounds", Tied_rounds)