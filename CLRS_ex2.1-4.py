#! /usr/bin/env python3
# CLRS ex 2.1-4 solution
# Note: This program only works for adding 2 numbers with the same number of bits in their binary representations.
# i.e both A and B have to be less than the same value of 2**k, where k is any positive integer >=0.

from subprocess import run

def add_bin(A,B):
	carry=0
	C=[0 for i in range(len(A))]
	for i in range(len(A)-1,-1,-1):
		C[i]=(A[i]+B[i]+carry)%2
		if((A[i]+B[i]+carry)>=2):
			carry=1
		else:
			carry=0

	C.insert(0,carry)
	return C

run("clear",shell=True)
A=list(map(int,bin(int(input("Enter first number : ")))[2:]))
B=list(map(int,bin(int(input("Enter second number : ")))[2:]))
if(len(A)!=len(B)):
	print("Not possible.")
	exit()
C='0b'+''.join(list(map(str,add_bin(A,B))))
print("Sum = "+C+' '+str(int(C,base=2)))
input("Press Enter")
subprocess.run("cls",shell=True)