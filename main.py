n, m = [int(x) for x in input().split()]
nums = [[0] * m for _ in range(n)]

x = 1
a = 0
for i in range(n):
    for j in range(m):
        if nums[i][j] == 0:
            nums[i][j] = a
            a += 1
        x = i
        x += 1
        j -= 1
        while x  < n and j - 1 >= 0:
            nums[x + 1][j - 1] = a
            x += 1
            j -= 1
            a += 1


print(nums)

