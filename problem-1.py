"""
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. 
The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.
"""

def is_multiple(number, multiple):
	return number % multiple == 0

def main():
	i = 1
	j = 0

	while(i < 1000):
		if(is_multiple(i, 3) or is_multiple(i, 5)):
			j += i
		i += 1

	print(f"The sum of all the multiples of 3 or 5 below 1000 is {j}")


if __name__ == '__main__':
	main()