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
	alphabet = "abcdefghijklmnopqrstuvwxyz"
	availableLetters = ""
	for character in alphabet:
		if character not in lettersGuessed:
			availableLetters += character
	return availableLetters

def main():
	secretWord = 'apple'
	lettersGuessed = ['e', 'i', 'k', 'p', 'r', 's']
	
	# print isWordGuessed(secretWord, lettersGuessed)
	print getAvailableLetters(lettersGuessed)

main()
