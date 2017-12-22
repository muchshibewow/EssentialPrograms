// Sieve of Eratosthenes implementation in C++.

#include<iostream>

using namespace std;

int main()
{
	long n,i,j;
	cout<<"Enter number : ";
	cin>>n;
	bool primes[n+1];

	// Initialising the primes array, assuming every number is a prime.

	for(auto &x:primes)
	{
		x=true;
	}

	// Changing the multiples of prime factors to be non-prime.
	// Also, 0 and 1 are not considered prime numbers.

	primes[0]=false;
	primes[1]=false;

	for(i=2;i*i<=n;i++)
	{
		for(j=i*i;j<=n;j+=i)
		{
			primes[j]=false;
		}
	}

	for(i=2;i<=n;i++)
	{
		if(primes[i])
		{
			cout<<i<<" ";
		}
	}
	cout<<"\n";
	return 0;
}
