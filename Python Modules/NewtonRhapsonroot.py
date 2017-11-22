epsilon = 0.01
square = 10000000       #square here
guess = square/2.0
numGuesses = 0

while abs(guess**2 - square) >= epsilon:
    numGuesses += 1
    guess = guess - ((guess**2 - square)/(2*guess))    #Newton-Rhapson formula

print('No. of guesses : ' + str(numGuesses))
print('Square root of ' + str(square) + ' is about ' + str(guess))



# Newton Rhapson => g = g - f(g)/f'(g)