# Introduction to functions
# Matthew Yacovone

def is_even(x):
	"""
	This function with determine if a number is even or odd
	"""
	remainder = x % 2
	return remainder == 0
	
def main():
	"""
	Main Function
	"""
	print("Printing even/odd for numbers 1-20")
	for x in range(1, 21):
		if is_even(x):	#if return is true (is even)
			print(x, "Even")		
		else:
			print(x, "Odd")

main()
