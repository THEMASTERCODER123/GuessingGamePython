import random as r
def game():
    x = r.randrange(1 , 101)
    print("guess a random number between 1 and 101")
    diff = str(input("Please choose the difficulty of - Easy, Medium or Hard")).lower()
    while diff != "easy"or "medium" or "hard":
        if diff == "easy":
            chances = int(10)
            break
        elif diff == "medium":
            chances = int(7)
            break
        elif diff == "hard":
            chances = int(5)
            break
        else:
            print("You have not selected a option from the above.")
            diff = str(input("Please choose the difficulty of - Easy, Medium or Hard")).lower()

    print("You have got: ",chances," chances")

    while chances != -1 :
        y = int(input("Guess: "))
        if y == x :
            print("That is correct.")
            break
        elif y > x:
            print("your number is too big.Try again.")
            chances -= 1
            print("You have only got: " , chances , " chances")
        else:
            print("Your number is too small.Try again.")
            chances -= 1
            print("You have only got: ", chances , " chances")


while True:
    z = input("Do you want to play a game of guessing ?. Yes or No").lower()
    if z == "yes" :
        game()
    else:
        print("bye")
        break

"""elif y != type(y):
            print("Please enter the right number and not anything else.")
            chances - 2
            print("2 of your chances has been deducted for not following the rules ", chances," chances are left")"""