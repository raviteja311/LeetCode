'''
Given an array of integers nums and an integer target,
return indices of the two numbers such that they add up to target
'''


def twosum(nums: list[int], target: int):
    n = len(nums)
    for i in range(n - 1):
        for j  in range(i+1, n):
            if nums[i] + nums[j] == target:
                return [i, j]
    return []
    
if __name__ == "__main__":
    nums = [2, 7, 11,15]
    target = 9

result = twosum(nums, target)
print(result)