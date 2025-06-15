import heapq


score = [5, 4, 3, 2, 1]
heap = []
n = len(score)
for i in range(n):
    heapq.heappush(heap, (-score[i], i))
rank = [0] * n
place = 1
while heap:
    ind = heapq.heappop(heap)[1]
    if place == 1:
        rank[ind] = 'Gold Medal'
    elif place == 2:
        rank[ind] = 'Silver Medal'
    elif place == 3:
        rank[ind] = 'Bronze Medal'
    else:
        rank[ind] = str(place)
    place += 1

print(rank)
