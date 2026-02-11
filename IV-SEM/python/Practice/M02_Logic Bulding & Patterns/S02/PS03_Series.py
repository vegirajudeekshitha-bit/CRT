'''
#Fibonacci series
def fib(n):
    if n <= 1:
        return n
    return fib(n - 1) + fib(n - 2)
n = int(input())
for i in range(n):
    print(fib(i), end = " ")
'''
'''
#using list
n = int(input())
fib = [0, 1]
for i in range(2, n):
    fib.append(fib[i - 1] + fib[i - 2])
print(fib[:n])
''' 

# Power of a number using loop

base = int(input("Enter base: "))
exponent = int(input("Enter exponent: "))

result = 1

for i in range(exponent):
    result = result * base

print("Result =", result)

