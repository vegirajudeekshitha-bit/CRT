'''
#factors of a number

n = int(input())
for i in range(1, n//2 + 1):
    if n % i == 0:
        print(i, end = " ")
print(n)
'''
'''
#count no.of factors for a given number

n = int(input())
count = 0
for i in range(1, n//2 + 1):
    if n % i == 0:
        count += 1
print(count + 1)
'''
'''
#check if a number is prime or not

n = int(input())
count = 0
for i in range(2, n//2 + 1):
    if n % i == 0:
        count += 1
print("prime" if count == 0 else "not prime")
'''
'''
#display all prime numbers in a given range
start = int(input())
end = int(input())
if start == 1:
    start = 2

for i in range(start, end + 1):
    count = 0
    for j in range(2, i//2 + 1):
        if i % j == 0:
            count += 1
    if count == 0:
        print(i, end = " ")
'''
'''
#factorial of anumber
n = int(input())
if n < 0:
    print(" no factorial for -ve numbers")
elif n == 0 or n == 1:
    print(1)
else:
    fact = 1
    for i in range(2, n + 1):
        fact *= i
    print(fact)
'''
#GCD of two numbers
a = int(input())    
b = int(input())
while b:
    a, b = b, a % b
print(a)
import math
print(math.gcd(a,b))