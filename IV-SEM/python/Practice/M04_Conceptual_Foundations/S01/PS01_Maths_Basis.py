#1.gcd of two numbers
a = int(input())
b = int(input())
while b != 0:
    a, b = b, a % b
print(a)

#2.lcm of two numbers
a = int(input())
b = int(input())
def gcd(x, y):
    while y != 0:
        x, y = y, x % y
    return x

#3.lcm = (a * b) // gcd(a, b)
lcm = (a * b) // gcd(a, b)
print(lcm)

#4.perfect number
num = int(input())
sum_of_divisors = 0
for i in range(1, num):
    if num % i == 0:
        sum_of_divisors += i
if sum_of_divisors == num:
    print(f"{num} is a perfect number.")
    