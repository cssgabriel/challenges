from os import remove


def lengthOfLastWord(s: str) -> int:
    s = s.split()
    return len(s[-1])


# TESTES

print(lengthOfLastWord("Hello World"))
print(lengthOfLastWord("   fly me   to   the moon  "))
print(lengthOfLastWord("luffy is still joyboy"))