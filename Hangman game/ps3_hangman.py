# Hangman game
#

# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

import random

WORDLIST_FILENAME = "words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code
# -----------------------------------def hangman(secretWord):

wordlist = loadWords()

def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    test = False
    for letter in secretWord:
        if letter in lettersGuessed:
            test = True
        else:
            test = False
            break;
    return test



def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    guess = ""
    for letter in secretWord:
        if letter in lettersGuessed:
            guess += " " + letter + " "
        else:
            guess += " " + "_" + " "
    return guess



def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    import string
    alpha = string.ascii_lowercase
    left = ''
    for letter in alpha:
        if letter in lettersGuessed:
            left += ''
        else:
            left += letter
    return left
    

def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    length = len(secretWord)
    guesses = 8
    lettersGuessed = []
    availLetters = getAvailableLetters(lettersGuessed)
    print("Welcome to the game, Hangman!")
    print("I am thinking of a word that is " + str(length) +  " letters long. ")
    print("----------")
    while guesses > 0:
        if isWordGuessed(secretWord, lettersGuessed):
            print("Congratulations, you won!")
            break;
        print("You have " + str(guesses) + " guesses left.")
        print("Available letters: " + availLetters)
        testChar = input("Please guess a letter: ")
        testChar = testChar.lower()
        if testChar in lettersGuessed:
            print("Oops! You've already guessed that letter:" + getGuessedWord(secretWord, lettersGuessed))
        elif testChar in secretWord:
            lettersGuessed.append(testChar)
            print("Good guess:" + getGuessedWord(secretWord, lettersGuessed))
        else:
            lettersGuessed.append(testChar)
            print("Oops! That letter is not in my word:" + getGuessedWord(secretWord, lettersGuessed))
            guesses -= 1
        print("--------")
        availLetters = getAvailableLetters(lettersGuessed)
        if guesses < 1:
            print("Sorry, you ran out of guesses. The word was " + secretWord + ".")



# When you've completed your hangman function, uncomment these two lines
# and run this file to test! (hint: you might want to pick your own
# secretWord while you're testing)

secretWord = chooseWord(wordlist).lower()
hangman(secretWord)

# Yipee, Made it !!!!!!!!!!!!!!!!!!!!