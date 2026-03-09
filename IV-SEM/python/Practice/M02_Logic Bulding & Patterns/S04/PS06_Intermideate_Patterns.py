
# 1️⃣ Square of numbers
li = [1, 2, 3, 4, 5]

res = []
for i in li:
    res.append(i ** 2)
print("Squares using loop:", res)

print("Squares using list comprehension:", [i ** 2 for i in li])


# 2️⃣ Even numbers
li = [1, 2, 3, 4, 5]

res = []
for i in li:
    if i % 2 == 0:
        res.append(i)

print("Even numbers using loop:", res)

print("Even numbers using list comprehension:", [i for i in li if i % 2 == 0])


# 3️⃣ Convert list of characters to string
li1 = ['a', 'b', 'c']

res = ""
for ch in li1:
    res += ch

print("Using loop:", res)
print("Using join:", "".join(li1))


# 4️⃣ Star Pattern (Right aligned triangle)
# Example:
#    *
#   **
#  ***
# ****

n = int(input("Enter number for right triangle: "))
for i in range(1, n + 1):
    print(" " * (n - i) + "*" * i)


# 5️⃣ Inverted Star Pattern
# Example:
# * * * *
#  * * *
#   * *
#    *

n = int(input("Enter number for inverted pattern: "))
for i in range(n):
    print(" " * i + "* " * (n - i))


# 6️⃣ Increasing Star Pattern with spaces
n = int(input("Enter number for increasing spaced pattern: "))
for i in range(n):
    print(" " * (n - i - 1) + "* " * (i + 1))


# 7️⃣ Alphabet Pattern
# Example:
# A
# B C
# D E F
# G H I J

n = int(input("Enter number for alphabet pattern: "))
val = 65  # ASCII value of 'A'

for i in range(n):
    for j in range(i + 1):
        print(chr(val), end=" ")
        val += 1
    print()