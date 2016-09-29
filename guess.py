import random
from sys import argv
# script, num_tries = argv
num_tries = 0
#user picks number of tries available when starting
try:
    num_tries = int(argv[1])
except (IndexError, ValueError):
   	num_tries = 3

user_guess = ""
num_range = ""

#lets user set range
def userSetRange ():
	#user picks range of numbers to guess from when starting
	num_range = input("The random number will be between 0 and... \n\tEnter a number. ")

	validate_range(num_range)

	print ("The number is between 0 and {}".format(num_range))


#check for valid input
def validate_range (num_range):

	if num_range.isdigit() and int(num_range) > 1:
		num_range = int(num_range)

		#generate random answer
		answer = random.randint(1, num_range - 1)
		# print ("answer: {}".format(answer))

		guess(num_range, answer)
	else:
		print("{} is not a valid number. Make sure your number is an integer larger than 1.")
		userSetRange()


#check for valid input
def validate_guess (user_guess, num_range, answer):

	if user_guess.isdigit() and int(user_guess) <= num_range:
		user_guess = int(user_guess)
		guessCompare(user_guess, num_range, answer)
	else:
		print("{} is not a valid number. Make sure your guess is an integer between 0 and {}."
			.format(user_guess, num_range))
		guess(num_range, answer)

	 
#gets guess from user
def guess(num_range, answer):
	#tries == 0, user loses
	if num_tries > 0:
		print ("\nGuesses left: {}".format(num_tries))
		#user makes guess
		user_guess = input("\n\tMake a guess! ")
		# user_guess = int(user_guess)
		
		validate_guess(user_guess, num_range, answer)
	else: 
		print ("YOU LOSE! The answer was {}!".format(answer))	


#tell user if guess is high or low
def guessCompare(user_guess, num_range, answer):
	if answer > user_guess:
		print ("Too low. Try a little higher.")
		num_tries =- 1
		guess(num_range, answer)
	elif answer < user_guess:
		print ("Too high. Try a little lower.")
		num_tries =- 1
		guess(num_range, answer)
	#guess == number, user wins
	elif answer == user_guess:
		print ("YOU WIN! The answer was {}!".format(answer))

userSetRange()







