import random
def getMin():
    while True:
        try:
            num = int(input("Enter the minimum number: "))
            return num
        except ValueError:
            print("Please enter a valid number.")
            continue
def getMax(minimum):
    while True:
        try:
            num = int(input("Enter the maximum number: "))
            if num < minimum:
                print(f"Max must be bigger than minimum! ({minimum})")
                continue
            return num
        except ValueError:
            print("Please enter a valid number.")
            continue
def getUserInput(minimum, maximum, randNum):
    tries = 0
    while True:
        try:
            num = int(input("Enter your guess: "))
            if num < minimum or num > maximum:
                print("Please enter a valid number.")
                continue
            tries += 1
            if num == randNum:
                print(f"You win! Tries:{tries}")
                break
            elif num < randNum:
                print(f"Too low! Tries:{tries}")
            elif num > randNum:
                print(f"Too high! Tries:{tries}")
        except ValueError:
            print("Please enter a valid number.")

def playGame():
    print("Welcome to the number guessing game!")

    # Get Range
    minimum = getMin()
    maximum = getMax(minimum)

    # Generate random number within range
    randNum = random.randint(minimum, maximum)
    
    # Get user guesses
    userNum = getUserInput(minimum, maximum, randNum)
playGame()