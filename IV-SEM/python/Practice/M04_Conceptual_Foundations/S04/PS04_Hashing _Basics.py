#Hashing ==> set, Dictionary 

def two_sum(nums, target):
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]   
print(two_sum([2, 7, 11, 15], 9))  # Output: [0, 1]

def  two_sum(nums, target):
    num_dict = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in num_dict:
            return [num_dict[complement], i]
        num_dict[num] = i
print(two_sum([2, 7, 11, 15], 9))  # Output: [0, 1]

