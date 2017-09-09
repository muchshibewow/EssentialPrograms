# A program that takes an array and a value as input, and searches for it in the array.
# This program makes use of the sorted() function, as well as the bisect_left() function,
# from the bisect package, which is based on binary search.
# I hope that this program has a complexity of no more than O(n lg n).
# I really do hope.

import bisect
l=sorted(list(map(int,input().strip().split())))
srch=int(input())
if(l[bisect.bisect_left(l,srch)]!=srch):
	print("Not present")
else:
	print("Present at index {}".format(bisect.bisect_left(l,srch)))