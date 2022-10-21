# Matrix Setup Matthew Yacovone
## This code build an augmented matrix ready for row reduction

# Build the A matrix

def buildA(r,x):
	print("\n")
	A = []	# the A matrix
	for i in range(r):
		row = []
		for j in range(x):
			row.append(int(input("[A] Enter element of [{}] [{}] (if a coefficent  "
								 "equals 0 enter 0): ".format(i,j))))
		A.append(row)
	return(A)

# Build the b column vector

def buildB(r,x):
	print("\n")
	b = []	# column vector
	for i in range(r):
		col = []
		col.append(int(input("[b] Enter element [{}]:  ".format(i))))
	b.append(col)
	    print(b[i])

	return(b)
	



# Main

def main():
	print("FORM: Ax = b \n alpha(x1) + beta(x2) + gamma(x3) + delta(x4) = b\n")
	r = int(input("How many equations do you have? ")) # number of rows
	x = int(input("How many unknowns do you have? ")) # number of x variables
	c = x + 1 # number of columns in the augmented matrix
	
	A = buildA(r,x)
	b = buildB(r,x)

	
	
main()
	
	
	
	


   
