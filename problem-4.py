"""
A palindromic number reads the same both ways. 
The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""

def reverse(string):
	return string[::-1]

def is_palindromic(number):
	return str(number) == reverse(str(number))

def main():
	i = 999 
	j = 999
	largest_palindrome = 0

	while i >= 100:
		while j >= 100:
			if is_palindromic(i * j) and largest_palindrome < (i * j):
				largest_palindrome = i * j
			j -= 1
		i -= 1
		j = 999

	print(f"The largest palindrome made from the product of two 3-digit numbers is {largest_palindrome}")

if __name__ == '__main__':
	main()