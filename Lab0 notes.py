import numpy as np

#Write a complete Python script that does the following:
#•	Prompts the user to enter values (either 0 or 1) for each of the inputs A, B, C, and D.
#o	Add code to validate each input value. If the entered value is not a 0, then set the value to 1.
#•	Determines and displays the output value out.
#o	Use the appropriate logical operators and selection statements to do this task.
#o	The logic test could be done in a single line, but you may break it up into multiple tests, if desired.
"""
logical_and(x1, x2, /[, out, where, ...])
	

Compute the truth value of x1 AND x2 element-wise.

logical_or(x1, x2, /[, out, where, casting, ...])
	

Compute the truth value of x1 OR x2 element-wise.

logical_not(x, /[, out, where, casting, ...])
	

Compute the truth value of NOT x element-wise.

logical_xor(x1, x2, /[, out, where, ...])
	

Compute the truth value of x1 XOR x2, element-wise.
"""

"""A = int(input("Enter a value between 0-1: ")) #A[0]
B = int(input("Enter a value between 0-1: ")) #B[1]
C = int(input("Enter a value between 0-1: ")) #C[2]
D = int(input("Enter a value between 0-1: ")) #D[3]

inputs = np.array([A,B,C,D])
inputs = np.clip(inputs,0,1)
print(inputs)"""
A = 0
B = 0
C = 1
D = 1
print(A,B,C,D)

out1 = not(A or B) 
out2 = not(out1 and C) #AB NAND C
D = not D
out3 = C and D #C AND D

out = out2 or out3
print(out)
    











x = np.array([1,4,-2,5,8,-3])
#print(x)
y = np.flip(x)
#print(y)

z = np.transpose(np.array([x,y]))
#print(z)
#z = np.transpose(z)
#print()
#print(z)
#print()
#print(sum(z)[0:1])
#print(np.add(z))
#print(sum(z)[0])
#print(sum(z[0:,0]))
#e)	Create a 1-D NumPy array named m that holds the integer numbers from 1 to 99 in steps of 1.

#m = np.full((1,99),0)
m = np.array(np.arange(1,100))
#print(m)

n = (m[m % 4 == 0])

#print(n)

p = np.concatenate([m[0:4],n,m[4:100]])
#print(p)
#g)	Finally, create new 1-D NumPy array named p that contains the first four elements of  m,
#all the elements of n, and the remaining elements of m from the fifth element onwards, in that order.
