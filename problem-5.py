"""
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
"""

def gcd(a, b):
	if b == 0:
		return a
	else:
		return gcd(b, a % b)

def lcm(a, b):
	return (abs(a * b)/gcd(a, b))

def main():
	i = 20
	j = i - 1

	while i > 2:
		j = lcm(j, i)
		i -= 1

	print(f"The smallest positive number that is evenly divisible by all of the numbers from 1 to 20 is {j}")


if __name__ == '__main__':
	main()