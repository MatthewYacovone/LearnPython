# Turn the given while loop into a for loop
# Matthew Yacovone

# While loop
"""
an_letters = "aefhilmnorsxAEFHILMNORSX"
word = input("I will cheer for you! Enter a word: ")
times = int(input("Enthusiasm level (1-10): "))

i = 0
while i < len(word):
	char = word[i]
	if char in an_letters:
		print("Give me an " + char + "! " + char)
	else:
		print("Give me a  " + char + "! " + char)
	i += 1
print("What does that spell?")
for i in range (times):
	print(word, "!!!")
"""
	
# For loop (my work)
an_letters = "aefhilmnorsxAEFHILMNORSX"
word = input("I will cheer for you! Enter a word: ")
times = int(input("Enthusiasm level (1-10): "))

for char in word:
	if char in an_letters:
		print("Give me an " + char + "! " + char)
	else:
		print("Give me a  " + char + "! " + char)
print("What does that spell?")
i = 0
for i in range (times):
	print(word, "!!!")