n = int(input())
nums = [int(x) for x in input().split()]
max_sum = float('-inf')
cur_sum = 0
start_index = 0
best_start = 0
best_end = 0

for i in range(n):
    cur_sum += nums[i]
    if cur_sum > max_sum:
        max_sum = cur_sum
        best_start = start_index
        best_end = i
    if cur_sum < 0:
        cur_sum = 0
        start_index = i + 1

print(best_start + 1, best_end + 1, max_sum)


