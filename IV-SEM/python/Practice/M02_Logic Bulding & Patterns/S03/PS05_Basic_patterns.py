'''
input: 4
output:
****
****
****
****
'''
'''
n = int(input())
for i in range(n):
    for j in range(n):
        print("*", end = "")
    print()

    '''
'''
input: 4
output:
*
**
***
****
'''
'''
n = int(input())
for i in range(n):
    for j in range(i + 1):
        print("*", end = "")
    print()
'''
'''
inpt: 4
output: 
****
***
**  
*'''

n = int(input())
for i in range(n):      
    for j in range(n - i):
        print("*", end = "")
    print()

