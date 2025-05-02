n, m = [int(x) for x in input().split()]
nums = [[int(x) for x in input().split()] for _ in range(n)]

max_result = 0
count, sportsmen = 1, []
for i in range(n):
    for j in range(m):
        if max_result < nums[i][j]:
            max_result = nums[i][j]
            sportsmen.clear()
            sportsmen.append(i)
            count = 1
        elif max_result == nums[i][j] and i not in sportsmen:
            count += 1
            sportsmen.append(i)

print(count)
print(*sportsmen, sep='\n')
