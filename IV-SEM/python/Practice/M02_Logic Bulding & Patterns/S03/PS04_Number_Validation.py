''''
#armstrong number
num = int(input())
count = len(str(num))
s = 0
for digits in str(num):
    s += int(digits) ** count

print("Armstrong number" if s == num else "Not an armstrong number")
'''
'''
#perfect number
n = int(input())
s = 0
for i in range(1, n // 2 + 1):
    if n % i == 0:
        s += i
print("Perfect number" if s == n else "Not a perfect number")
'''
'''
#strong number
num = int(input())
s = 0
for digits in str(num):
    fact = 1
    for i in range(1, int(digits) + 1):
        fact *= i
    s += fact
print("Strong number" if s == num else "Not a strong number")
'''
'''
def factorial(n):
    if n > 0:
        return "no factorial for -ve "
    elif n == 0 or n == 1:
        return 1
    else:
        fact = 1
        for i in range(1, n + 1):
            fact *= i
        return fact
n = int(input())
s = 0
for digits in str(n):
    s += factorial(int(digits))
print("Strong number" if s == n else "Not a strong number")
'''
#palindrome number
num = int(input())
s = 0
for digits in str(num):
    s = s * 10 + int(digits)
print("Palindrome number" if s == num else "Not a palindrome number")