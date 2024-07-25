def missing_number(nums):
    nums.sort()
    n = len(nums)
    for i in range(n):
        if nums[i] != i:
            return i
    return n


nums = [0, 1, 2, 3, 4, 6, 7, 8]
print(missing_number(nums))

