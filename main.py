import heapq

n = int(input())
a = [int(x) for x in input().split()]
b = [int(x) for x in input().split()]
offers = [int(x) for x in input().split()]

heap_a = []
heap_b = []
for ind, elem in enumerate(a):
    heapq.heappush(heap_a, (-elem, ind))

for ind, elem in enumerate(b):
    heapq.heappush(heap_b, (-elem, ind))

seq = [n] * 0
i = 0
while i < n:
    if offers[i] == 0:
        x, ind_a = heapq.heappop(heap_a)
        seq.append(ind_a + 1)
        for pair in heap_b:
            if pair[1] == ind_a:
                heap_b.remove(pair)
                break
    else:
        y, ind_b = heapq.heappop(heap_b)
        seq.append(ind_b + 1)
        for pair in heap_a:
            if pair[1] == ind_b:
                heap_a.remove(pair)
                break
    i += 1

print(seq)
