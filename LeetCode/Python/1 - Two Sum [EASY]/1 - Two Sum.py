def twoSum(nums, target):
    new_list = list()
    for i, value in enumerate(nums):
        rest = target - value
        if rest in nums:
            check = nums.index(rest)
            if check != i:
                new_list.append(i)
            else:
                if rest in nums[i+1:]:
                    new_list.append(i)
    return new_list


# TESTES

print(twoSum([2,7,11,15], 9))
print(twoSum([3,2,4], 6))
print(twoSum([3,3], 6))
print(twoSum([0,4,3,0], 0))
print(twoSum([-3,4,3,90], 0))