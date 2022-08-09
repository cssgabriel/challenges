def searchInsert(nums:list[int], target: int) -> int:
    if target not in nums:
        nums.append(target)
        nums.sort()
        return nums.index(target)

    else:
        return nums.index(target)


# TESTES

print(searchInsert([1,3,5,6],5))
print(searchInsert([1,3,5,6],2))
print(searchInsert([1,3,5,6],7))
print(searchInsert([1,3,5,6],0))
print(searchInsert([1,3,5,6],-5))