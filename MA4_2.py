#!/usr/bin/env python3.9
from tracemalloc import start
from numba import njit
from person import Person
import time as time
import matplotlib.pyplot as plt
import numpy as np

def fib_py(n):
	if n <= 1:
		return n
	else:
		return fib_py(n-1) + fib_py(n-2)

@njit
def fib_numba(n):
	if n <= 1:
		return n
	else:
		return fib_numba(n-1) + fib_numba(n-2)

def main():
	f = Person(5)
	# print(f.get())
	# f.set(7)
	# print(f.fib())
	# print(fib_py(5))
	# print(fib_numba(5))
	
	n1_array = list(range(0, 45))
	n2_array = list(range(20, 30))
	n3 = 47
	timep1 = []
	timep2 = []
	timenjit1 = []
	timenjit2 = []
	timecpp1 = []
	timecpp2 = []

 	#Time calculation for pure Python [0, 45]

	for i in n1_array:
 		start = time.perf_counter()
 		fib_py(i)
 		end = time.perf_counter()
 		timep1 = np.append(timep1, end - start) 
    
#     #Time calculation for Numba [0, 45]

 	for i in n1_array:
 		start = time.perf_counter()
 		fib_numba(i)
 		end = time.perf_counter()
 		timenjit1 = np.append(timenjit1, end - start)

 	#Time calculation for C++ [0, 45]

 	for i in n1_array:
 		f.set(i)
 		start = time.perf_counter()
 		f.fib()
 		end = time.perf_counter()
 		timecpp1 = np.append(timecpp1, end - start)

 	plt.plot()
 	plt.plot(timep1, label = 'Python', color='red')
 	plt.plot(timenjit1, label = 'Numba', color='green')
 	plt.plot(timecpp1, label = 'C++', color='blue')
 	plt.xlabel("n")
 	plt.ylabel("sec")
 	plt.savefig('figure')
 	plt.show()
# #------------------------------------------------------------------------------------------------
	#Time calculation for pure Python [20, 30]

	 for i in n2_array:
	 	start = time.perf_counter()
	 	fib_py(i)
	 	end = time.perf_counter()
	 	timep2 = np.append(timep2, end - start)
    
    #Time calculation for Numba [20, 30]

	 for i in n2_array:
	 	start = time.perf_counter()
	 	fib_numba(i)
	 	end = time.perf_counter()
	 	timenjit2 = np.append(timenjit2, end - start)
	
	 plt.plot()
	 plt.plot(timep2, label = 'Python', color='red')
	 plt.plot(timenjit2, label = 'Numba', color='green')
	 plt.xlabel("n")
	 plt.ylabel("sec")
	 plt.savefig('figure1')
	 plt.show()
#------------------------------------------------------------------------------------------------

    #Time calculation for C++ fib(47)

	f.set(n3)
	start = time.perf_counter()
	print("Fibonucci 47 for C++:" + str(f.fib()))
	end = time.perf_counter()
	print("Execution time for C++:" + str(end - start))

    #Time calculation for Numba fib(47)

	start = time.perf_counter()
	print("Fibonucci 47 for Numba:" + str(fib_numba(n3)))
	end = time.perf_counter()
	print("Execution time for Numba:" + str(end - start))

# Fibonucci 47 for C++:-1323752223
# Execution time for C++:47.37431290396489
# Fibonucci 47 for Numba:2971215073
# Execution time for Numba:47.43430274887942  

# Real price: 1836311903

if __name__ == '__main__':
	main()

