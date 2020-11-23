import sys
import heapq
from collections import defaultdict
input = sys.stdin.readline

N, M = map(int, input().split())
indgree = [0 for _ in range(N+1)]
arr = defaultdict(list)
l_set = set(range(1,N+1))
for _ in range(M):
    l, r = map(int, input().split())
    indgree[r]+=1
    arr[l].append(r)
    if r in l_set:
        l_set.remove(r)
h = list(l_set)
heapq.heapify(h)
result = []
while h:
    l = heapq.heappop(h)
    result.append(l)
    for r in arr[l]:
        indgree[r]-=1
        if indgree[r]==0:
            heapq.heappush(h, r)

print(' '.join(map(str,result)))