# Solution 1 (In-place swap)
arr = list(map(int, input().split()))

for i in range(len(arr) // 2):
    arr[i], arr[len(arr) - 1 - i] = arr[len(arr) - 1 - i], arr[i]

print(arr)


# Solution 2 (Using indexing, no built-in reverse)
li = list(map(int, input().split()))

res1 = [li[i] for i in range(len(li)-1, -1, -1)]
print(res1)


# Solution 3 (Using loop)
li = list(map(int, input().split()))

res2 = []
for ele in li:
    res2 = [ele] + res2

print(res2)

# Check if array is sorted
def check_array_sorted(nums):
    for i in range(len(nums) - 1):
        if nums[i] > nums[i + 1]:
            return False
    return True