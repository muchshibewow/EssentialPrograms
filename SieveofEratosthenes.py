#! /usr/bin/env python3
# A simple program I wrote to understand the Sieve of Eratosthenes method for generating primes.

import math,sys
def SieveofEratosthenes(n):
	bool_l=[True for i in range(n+1)]
	bool_l[0]=bool_l[1]=False
	for i in range(2,int(math.sqrt(n))+1): # Starts from the first prime, 2.
		if(bool_l[i]):
			for j in range(i*i,n+1,i): # Marking all multiples as non-prime.
				bool_l[j]=False

	return bool_l

#This is just driver extra code
N=int(input("Enter the range of the sieve : "))
sieve=SieveofEratosthenes(N)
for n in range(N+1):
	if(sieve[n]):
		sys.stdout.write(str(n)+' ')
print 

