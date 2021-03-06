# author: @adqz1995

def fibonacci(n):
	'''
	Generate fibonacci sequence using generator

	Args:
		n (int): Starting number for fibonacci
	'''
	assert isinstance(n, int) and n>=0
	num1, num2 = 1, 1
	counter = 0
	while counter < n:
		if counter == 0:
			counter += 1
			yield num1
		elif counter == 1:
			counter += 1
			yield num2
		else:
			num3 = num2 + num1
			num2, num1 = num3, num2
			counter += 1
			yield num3


if __name__ == '__main__':
	print(list(fibonacci(0)))
	print(list(fibonacci(5)))
	print(list(fibonacci(10)))