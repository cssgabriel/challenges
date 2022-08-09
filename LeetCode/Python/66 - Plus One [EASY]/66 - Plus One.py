def plusOne(digits: list[int]) -> list[int]:
    value = int("".join(str(x) for x in digits)) + 1
    new_value = [int(x) for x in str(value)]
    return new_value


# TESTES

print(plusOne([1,2,3]))
print(plusOne([4,3,2,1]))
print(plusOne([9]))
print(plusOne([9,9,9]))
