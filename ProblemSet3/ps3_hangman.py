import random
import string

WORDLIST_FILENAME = "words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print "Loading word list from file..."
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r', 0)
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = string.split(line)
    print "  ", len(wordlist), "words loaded."
    return wordlist

def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

def isWordGuessed(secretWord, lettersGuessed):
	for character in secretWord:
		if character not in lettersGuessed:
			return False
	return True

def getGuessedWord(secretWord, lettersGuessed):
	guessedWord = ""
	for character in secretWord:
		if character not in lettersGuessed:
			guessedWord += "_"
		else:
			guessedWord += character
	return guessedWord

def getAvailableLetters(lettersGuessed):
	availableLetters = ""
	for character in string.ascii_lowercase:
		if character not in lettersGuessed:
			availableLetters += character
	return availableLetters
    
def hangman(secretWord):
	guesses = 8
	guessedWord = ""
	lettersGuessed = []
	progress = getGuessedWord(secretWord, lettersGuessed)

	while(guesses > 0):
		print "------------"
		print "You have " + str(guesses) + " guesses left"
		print "Available Letters: " + getAvailableLetters(lettersGuessed)
		newGuess = str(raw_input("Please guess a letter: ")).lower()
		if newGuess in lettersGuessed:
			print "Oops! You've already guessed that letter: " + progress
			continue
		lettersGuessed += newGuess
		guessedWord = getGuessedWord(secretWord, lettersGuessed)
		if(progress == guessedWord):
			print "Oops! That letter is not in my word: " + progress
			guesses -= 1
		else:
			progress = guessedWord
			print "Good guess: " + progress
			if(progress == secretWord):
				print "------------"
				print "Congratulations, you won!"
				return 

	print "------------"
	print "Sorry, you ran out of guesses. The word was " + secretWord + "."
	return
		
def main():
	wordlist = loadWords()
	secretWord = chooseWord(wordlist).lower()
	print "Welcome to the game Hangman!"
	print "I am thinking of a word that is " + str(len(secretWord)) + " long."
	hangman(secretWord)

main()
