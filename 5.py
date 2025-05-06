n, m1, m2 = [int(x) for x in input().split()]
segments = [[int(x) for x in input().split()] for _ in range(n)]

# Time complexity O(n**2)
def solution1(n):
    count = 0
    for i in range(n):
        l = segments[i][0]
        r = segments[i][1]
        for j in range(i, n):
            l = max(l, segments[j][0])
            r = min(r, segments[j][1])
            len_cur = max(r - l, 0)
            if m1 <= len_cur <= m2:
                count += 1
        return count

