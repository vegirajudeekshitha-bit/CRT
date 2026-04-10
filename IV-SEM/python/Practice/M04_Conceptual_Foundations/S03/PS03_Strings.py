s = "python programming"

print(s.capitalize())
print(s.title())

s = s.title()
print(s)

print(s.replace("on", " ON"))
print(s)  \

# reverse a string without using built-in functions and slicing
def reverse_string(s):
    res = ""
    for i in range(len(s)-1, -1, -1):
        res += s[i]
    return res  

print(reverse_string(s))


def reverse_string(S):
    res = ""
    for ch in s:
        res = ch + res
    return res
print(reverse_string(s))

#palindrome check
def is_palindrome(s):
    s = s.replace(" ", "").lower()  
    return s == reverse_string(s)

print(is_palindrome("A man a plan a canal Panama")) 