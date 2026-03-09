'''input :  4
output : 
*      *
**    **
***  ***
********
********
***  ***
**    **
*      *'''
n = int(input())
for i in range(n):
    print("*" * (i + 1) + " " * (2 * (n - i - 1)) + "*" * (i + 1))
for i in range(n):
    print("*" * (n - i) + " " * (2 * i) + "*" * (n - i))

    