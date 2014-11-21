left = 0
right = 100
user_input = ""

print("Please think of a number between 0 and " + str(right) + "!")

while True:
	guess = (left + right)/2
	print("Is your secret number " + str(guess) + "?")
	user_input = raw_input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. ")
	if user_input == "l":
		left = guess
	elif user_input == "h":
		right = guess
	elif user_input == "c":
		break
	else:
		print("Sorry, I did not understand your input.")

print("Game over. Your secret number was: " + str(guess))
