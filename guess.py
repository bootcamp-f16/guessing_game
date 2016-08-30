#user picks number of tries available when starting
from sys import argv
script, num_tries = argv
import random

#user picks range of numbers to guess from when starting
num_range = input("The random number will be between 0 and... \n\tEnter a number. ")
num_range = int(num_range)
print ("The number is between 0 and {}".format(num_range))

user_guess = ""

#generate random number
answer = random.randint(0, num_range)

# print ("answer: {}".format(answer))


#check for valid input
def validate_guess (user_guess):

	if user_guess.isdigit() and int(user_guess) <= num_range:
		user_guess = int(user_guess)
		guessCompare(user_guess)
	else:
		print("{} is not a valid number. Make sure your guess is an integer between 0 and {}."
			.format(user_guess, num_range))
		guess()
	 
#gets guess from user
def guess():
	#tries == 0, user loses
	if num_tries > 0:
		print ("\nGuesses left: {}".format(num_tries))
		#user makes guess
		user_guess = input("\n\tMake a guess! ")
		# user_guess = int(user_guess)
		
		validate_guess(user_guess)
	else: 
		print ("YOU LOSE! The answer was {}!".format(answer))	

#tell user if guess is high or low
def guessCompare(user_guess):
	if answer > user_guess:
		print ("Too low. Try a little higher.")
		num_tries -= 1
		guess()
	elif answer < user_guess:
		print ("Too high. Try a little lower.")
		num_tries -= 1
		guess()
	#guess == number, user wins
	elif answer == user_guess:
		print ("YOU WIN! The answer was {}!".format(answer))

guess()







