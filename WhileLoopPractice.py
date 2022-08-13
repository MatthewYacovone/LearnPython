# While Loop Practice
# Matthew Yacovone

print("You are in the Lost Forest\n******************\n******************\n   :)\n******************\n******************")
n = input("Go left or right? ")
count = 0
while n == "right":
    count = count + 1
    if count < 3:
	    n = input(("You are in the Lost Forest\n******************\n******************\n   :(\n******************\n******************\nGo left or right? "))
    else:
    	n = input(("You are in the Lost Forest\n******************\n********      ****\n   (J'o')J   _1__1_\n******************\n******************\nGo left or right? "))
print("You got out of the Lost Forest!\n\o/")