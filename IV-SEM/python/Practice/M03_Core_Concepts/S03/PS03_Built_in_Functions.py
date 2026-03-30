'''
1)Find largest number using max() function
2)Check palindrome(using reversed() & join())
3)Count Even numbers (using filter())
4)Removie Duplicates from list (using set())
5)Sum of digits (using sum())
6)Sort words Alphabetically (using sorted())
7)Find common elements (using set())
8)Index with value(using enumerate())
9)Pair two lists (using zip())

'''
# 1)Find largest number using max() function
numbers = [3, 5, 1, 9, 2]
largest = max(numbers)
print("Largest number:", largest)

# 2)Check palindrome(using reversed() & join())
def is_palindrome(s):
    return s == ''.join(reversed(s))
word = "radar"
print(f"{word} is a palindrome: {is_palindrome(word)}")

# 3)Count Even numbers (using filter())
a = [1, 2, 3, 4, 5, 6]
res = list(filter(lambda x: x % 2 == 0, a))
print(res)
print(len(res))

# 4)Removie Duplicates from list (using set())
Arr = [1, 2, 2, 3, 4, 4, 5]
res = list(set(Arr))
print(res)

# 5)Sum of digits (using sum())
num = 12345
res = sum(int(digit) for digit in str(num))
print(res)

# 6)Sort words Alphabetically (using sorted())
a = ["banana", "apple", "cherry"]
print(sorted(a))

# 7)Find common elements (using set())
a = [1, 2, 3, 4, 5]
b = [4, 5, 6, 7, 8]
res = set(a) & set(b)
print(res)
print(tuple(res))

# 8)Index with value(using enumerate())
a = ["apple", "banana", "cherry"]
for index, value in enumerate(a):
    print(f"Index: {index}, Value: {value}")

# 9)Pair two lists (using zip())
a = [1, 2, 3]
b = ['a', 'b', 'c'] 
res = list(zip(a, b))
print(res)