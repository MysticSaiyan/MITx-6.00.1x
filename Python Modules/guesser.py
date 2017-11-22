
print("Please think of a number between 0 and 100!")
low = 0
high = 100
guess = (high+low)//2
check = ""
while True:
    print("Is your secret number", guess, "?")
    check = input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. ")
    if check == 'h':
        high = guess
        guess = (high+low)//2
    elif check == 'l':
        low = guess
        guess = (high+low)//2
    elif check == 'c':
        print("Game over. Your secret number was: ", guess)
        break;
    else:
        print("Sorry, I did not understand your input.")
