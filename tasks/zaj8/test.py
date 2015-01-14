import quicksort as qs
import numpy as np
import timeit

##bez cytona 146.06
##bez cytona 75.96

def test():
	arr = np.random.rand(1e2)
	qs.quicksort(arr, 0, len(arr)-1)
	# print(arr)
if __name__ == '__main__':
	print(timeit.timeit("test()", setup="from __main__ import test"))
	# test()