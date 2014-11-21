import string
from ps6_encryption import *

def main():
	wordList = loadWords()

	#text = applyShift('Hello, world!', 8)
	text = getStoryString()
	
	print "Cipher text:\n------------------------------------------\n" + text
	for shift in range(1, 26):
		print "Shift  " + str(shift) + ": "
		testText = applyShift(text, shift)
		print testText
	
	bestShift = findBestShift(wordList, text)	
	print "\nBest shift found: " + str(bestShift) + "\n------------------------------------------"
	print applyShift(text, bestShift)
		
main()
