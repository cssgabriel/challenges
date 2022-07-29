def climbStairs(n: int) -> int:
    ways = [0, 1]
    for c in range(n):
        value = ways[c] + ways[c+1]
        ways.append(value)
    return ways[-1]
    


print(climbStairs(5))