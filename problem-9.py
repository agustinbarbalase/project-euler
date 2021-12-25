"""
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

a² + b² = c²
For example, 32 + 42 = 9 + 16 = 25 = 52.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
"""

"""
-----------------------------------------------------
a² + b² = c²
a + b + c = 1000 => a + b + sqrt(a² + b²) = 1000

a + b + sqrt(a² + b²) = 1000
sqrt(a² + b²) = 1000 - a - b
a² + b² = (1000 - a - b)²

D = 1000 - a 

a² + b² = (D - b)²
a² + b² = D² - 2Db + b²
a² = D² - 2Db 
- 2Db = a² - D²
b = -(a² - D²)/(2D)
b = -((a - D)(a + D))/2D
b = -((a - 1000 + a)(a + 1000 - a))/(2(1000 - a))
b = -((2a - 1000)(1000))/(2000 - 2a)
b = -(2000a - 1000²)/(2000 - 2a)
b = (1000² - 2000a)/(2000 - 2a)

b(a) = (1000² - 2000a)/(2000 - 2a)
c(a, b) = sqrt(a² + b²)
-----------------------------------------------------
if a = b then

a + b + sqrt(a² + b²) = 1000 => 2a + sqrt(2a²) = 1000
2a + sqrt(2a²) = 1000
2a + sqrt(2)a = 1000
a(2 + sqrt(2)) = 1000
a = 1000/(2 + sqrt(2)) = 292.89
-----------------------------------------------------
if a < b then a < 292.89 or a <= 292
-----------------------------------------------------
"""
def function_b(a):
	return (1000 ** 2 - 2000 * a)/(2000 - 2 * a)

def main():
	a = 292.0
	b = 0

	while a > 0:
		if function_b(a) % 1 == 0:
			b = function_b(a)
			break
		a -= 1

	c = (a ** 2 + b ** 2) ** (1/2)
	print(f"a = {a}, b = {b}, c = {c}")
	print(f"The product abc is {a*b*c}")

if __name__ == '__main__':
	main()