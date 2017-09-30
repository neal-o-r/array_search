import numpy as np
import timeit
import matplotlib.pyplot as plt

plt.style.use('ggplot')

def linear_search(arr):
	c = 0
	prec = -np.inf
	for a in arr:
		if a < prec:
			return c
		c += 1
		prec = a


def binary_search(arr, i=0):

	pivot = arr[len(arr)//2]
	if pivot == arr[0]:
		return i + 1

	if pivot < arr[0]:
		return binary_search(arr[:len(arr)//2], i)
	else:
		i += len(arr)//2
		return binary_search(arr[len(arr)//2:], i)

def time_wrapper(func, *args, **kwargs):
	def wrapped():
		return func(*args, **kwargs)
	return wrapped


if __name__ == '__main__':

	bins = []
	lins = []
	ns = [10, 50, 100, 200, 500, 1000, 5000, 10000]
	for n in ns:

		b_all = 0
		l_all = 0
		for i in range(100):
			arr = np.roll(np.arange(n), np.random.randint(n))
		
			t_lin = time_wrapper(linear_search, arr)
			t_bin = time_wrapper(binary_search, arr)
			num = 10

			b_all += timeit.timeit(t_bin, number=num)
			l_all += timeit.timeit(t_lin, number=num)

		bins.append(b_all / 100)
		lins.append(l_all / 100)

	plt.plot(ns, np.array(lins)/max(lins), '-o', label='Linear Search')
	plt.plot(ns, np.array(bins)/max(lins), '-o', label='Binary Search')
	plt.plot(ns, np.array(ns)/max(ns), '--k', label='Linear')
	plt.plot(ns, np.log2(np.array(ns))/max(ns), '--k', label='Log')
	plt.legend()
	plt.show()
