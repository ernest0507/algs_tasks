import math

piles = []
h = 0


def f(arr, k):
    return sum([math.ceil(x / k) for x in arr])


l, r = 0, max(piles)
while l + 1 != r:
    c = (l + r) // 2
    if f(piles, c) > h:
        l = c
    else:
        r = c
print(r)
