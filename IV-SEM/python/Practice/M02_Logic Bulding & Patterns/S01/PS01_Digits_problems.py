n = int(input())
count = 0
if(n == 0):
    count = 1
while n > 0:
    count += 1
    n = n // 10
print(count)