# Program to print the number as a product of the powers of its prime factors
# Example: 36 = 2^2 * 3^2, 40 =2^3 * 5^1
# Disclaimer : Gets stuck with larger numbers. I tried it randomly with a number
# of the order of 10^12, and it effectively stopped my pc.
# I guess this program works normally if the number is of the order of 10^7.
import math
def SieveofEratosthenes(n):
	bool_l=[True for i in range(n+1)]
	bool_l[0]=bool_l[1]=False
	for i in range(2,int(math.sqrt(n))+1): # Starts from the first prime, 2.
		if(bool_l[i]):
			for j in range(i*i,n+1,i): # Marking all multiples as non-prime.
				bool_l[j]=False

	return bool_l

N=int(input("Enter number : "))
primes=SieveofEratosthenes(N//2)
prime_factors=[i for i in range(2,(N//2)+1) if N%i==0 and primes[i]==True]
print(prime_factors)
prime_dct={}
for factor in prime_factors:
	prime_dct[factor]=0
N_copy=N
for factor in prime_factors:
	while(True):
		if(N_copy%factor==0):
			prime_dct[factor]+=1
			N_copy=int(N_copy/factor)
		else:
			break

for factor in prime_dct.keys():
	print(factor,' : ',prime_dct[factor])