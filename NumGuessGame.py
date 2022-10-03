# Number Guessing Game
# Matthew Yacovone

import random
import math

# Define Bounds
low = int(input("Input Lower Bound of Range: "))
high = int(input("Input Upper Bound of Range: "))

# Generate random number
x = random.randrange(low,high)

# Initializing Game
print("\nYou have", round(math.log(high - low + 1,2)), " chances to guess the number\n")
guess = int(input("Guess a number: "))
counter = 0


while counter < math.log(high - low + 1,2):
	counter += 1
	
	# Condition Testing
	if guess > x:
		guess = int(input("Your guess is too high! Try again: "))
	elif guess < x:
		guess = int(input("Your guess is too low! Try again: "))
	else:
		print("Congratualtions you guessed %d in %d attempts!" % (x, counter))
		break

if counter >= math.log(high - low + 1,2):
	print("The number is %d" % x)
	print("Better luck next time")
