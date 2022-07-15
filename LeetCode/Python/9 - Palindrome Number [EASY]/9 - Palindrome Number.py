def isPalindrome(x: int) -> bool:
    if x >= 0:
        v = str(x)
    else:
        return False
    if v[::-1] == v:
        return True


# TESTES

print(isPalindrome(10101))
print(isPalindrome(121))
print(isPalindrome(-121))
print(isPalindrome(10))
