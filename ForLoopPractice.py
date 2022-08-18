# For Loop Practice
# Matthew Yacovone

mySum = 0
for i in range(7,10):
	mySum += i
	print(mySum)
print("StartStop =", mySum)	# answer = 0 + 7 + 8 + 9 = 24

x = 0
for a in range(5,11,2):
    x += a
    print(a)
print("StartStopStep =",x) 	# answer = 5 + 7 + 9 = 21

y = 0
for b in range(5,11,2):
	y += b 
	if y == 5:
		break
		y += 1
print("StartStepStopBreak =",y)
