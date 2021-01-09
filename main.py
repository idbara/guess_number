from random import randint


def play():
    print("This game only guessing number. You can guessing number range 1 - 100.")
    print("you can type 0 for exit.")
    NUMBER = randint(1, 100)
    while True:
        try:
            GUESS = int(input("Guess Number : "))
            if NUMBER == GUESS:
                print(GUESS, "Correct!")
                break
            elif NUMBER < GUESS:
                print(GUESS, "too high")
            elif NUMBER > GUESS:
                print(GUESS, "too low")
            elif GUESS == 0:
                print("Thank you for playing :)")
                break
        except Exception:
            print("Input number only!")


while True:
    play()
    AGAIN = input("type y to play again : ")
    if AGAIN != "y":
        break
    else:
        print(20 * "=")
