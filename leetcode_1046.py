import heapq

stones = [2, 7, 4, 1, 8, 1]
heap = []
for ind, elem in enumerate(stones):
    heapq.heappush(heap, -elem)

print(heap)
while len(heap) > 1:
    y = -heapq.heappop(heap)
    x = -heapq.heappop(heap)
    if x != y:
        heapq.heappush(heap, -(y - x))

print(-heapq.heappop(heap))
