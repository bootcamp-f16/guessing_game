import random

myName = raw_input("What is your name? ")
print "Hello, %s." % myName

guesses = 0

from random import randint



number = random.randint(1, 10)
print("Think, " + myName + ", I am thinking of a number between 1 and 10.")

while guesses < 3:


	
	guess = raw_input ("Select a number between 1-10 ")

	

	guess = int (guess)

	if guess < number:
		print("The Number is too low, guess again.") 

	elif guess > number:         
		print("The Number is too high, guess again.")

	else:
		guess == number
		print ("You won")
		break

	guesses +=1	

else:
	print ("You lose")


    