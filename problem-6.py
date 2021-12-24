"""
The sum of the squares of the first ten natural numbers is,

1²+2²+ ... + 10² = 385

The square of the sum of the first ten natural numbers is,

(1+2+ ... +10)² = 55² = 3025

Hence the difference between the sum of the squares of the first ten natural numbers 
and the square of the sum is 3025-385 = 2640.

Find the difference between the sum of the squares of the first one hundred natural 
numbers and the square of the sum.
"""

def sum_of_the_squares(n):
	return (n * (n + 1) * (2 * n + 1))/6

def sum_of_the_first_n_natural(n):
	return (n * (n + 1))/2

def main():
	i = 100
	result = sum_of_the_first_n_natural(i) ** 2 - sum_of_the_squares(i) 

	print("The difference between the sum of the squares of the first one hundred natural numbers")
	print(f"and the square of the sum is {result}")

if __name__ == '__main__':
	main()