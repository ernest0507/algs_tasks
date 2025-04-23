def max_subarray(N, array):
    start, end, best_start = 0, 0, 0
    current_sum, max_sum = 0, -float('inf')
    for i in range(N):
        if current_sum + array[i] > array[i]:
            current_sum += array[i]
        else:
            current_sum = array[i]
            start = i
        if current_sum > max_sum:
            max_sum = current_sum
            best_start = start
            end = i
    return best_start + 1, end + 1, max_sum


N = int(input())
array = [int(x) for x in input().split()]
print(*max_subarray(N, array))