# For Loop Practice
# Matthew Yacovone

x = 0
for a in range(7,10):
	x += a
	print(x)
print("StartStop =", x)    # answer = 0 + 7 + 8 + 9 = 24

y = 0
for b in range(5,11,2):
    y += b
    print(y)
print("StartStopStep =",y)    # answer = 0 + 5 + 7 + 9 = 21

z = 0
for c in range(5,11,2):
	y += c 
	if z == 5:
		break
		z += 1
print("StartStepStopBreak =",z)    # answer = 5
