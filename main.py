nums = [int(x) for x in input().split()]
k = int(input())
n = len(nums)


def solution1(nums, k, n):
    a = []
    b = []
    if k > n:
        k -= n
    for i in range(n):
        if i + k < n:
            a.append(nums[i])
        else:
            b.append(nums[i])
    return b + a


def solution2(nums, k, n):
    a = []
    b = []
    if abs(k) > n:
        k += n
    for i in range(n):
        if i + k < 0:
            a.append(nums[i])
        else:
            b.append(nums[i])
    return b + a


if k >= 0:
    print(*solution1(nums, k, n))
else:
    print(*solution2(nums, k, n))
