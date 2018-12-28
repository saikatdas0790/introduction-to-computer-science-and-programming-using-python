print("Please think of a number between 0 and 100!")

start = 0
end = 100
middle = int((start + end) / 2)

while True:
    print("Is your secret number " + str(middle) + "?")
    enteredLetter = input(
        "Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. ")
    if (enteredLetter != "h" and enteredLetter != "l" and enteredLetter != "c"):
        print("Invalid input. Try again!")
        continue
    elif enteredLetter == "h":
        start = middle
    elif enteredLetter == "l":
        end = middle
    else:
        print("Game over. Your secret number was: " + str(middle))
        break
    middle = int((start + end) / 2)
