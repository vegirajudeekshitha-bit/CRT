#sum of n natural numbers
def natural_sum(n):
    s = 0
    for i in range(1, n + 1):
        s += i
    return s
print(natural_sum(5))  # Output: 15
print(natural_sum(10)) # Output: 55

#with recursion
def natural_sum(n):
    if n == 1:
        return 1
    return n + natural_sum(n - 1)
print(natural_sum(5))  # Output: 15
print(natural_sum(10)) # Output: 55

#factorial of a number traditional method
def factorial(n):
    f = 1
    for i in range(1, n + 1):
        f *= i
    return f
print(factorial(5))  # Output: 120
print(factorial(10)) # Output: 3628800

#with recursion
def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)
print(factorial(5))  # Output: 120
print(factorial(10)) # Output: 3628800
#another method with error handling
def factorial(n):
    if n < 0:
        return"Factorial is not defined for negative numbers" 
    elif n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)
print(factorial(5)) # Output: Factorial is not defined for negative numbers
print(factorial(4)) # Output: 24

#fibonacci series  nth termtraditional method 
def fibonacci(n):
    if n <= 0:
        return "Input should be a positive integer"
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        a, b = 0, 1
        for _ in range(3, n + 1):
            a, b = b, a + b
        return b
print(fibonacci(10)) # Output: 34

#with recursion
def fibonacci(n):
    if n <= 0:
        return "Input should be a positive integer"
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)  
print(fibonacci(10)) # Output: 34


#GCD of 2 numbers traditional method
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a
print(gcd(48, 18)) # Output: 6

#with recursion
def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)
print(gcd(48, 18)) # Output: 6
