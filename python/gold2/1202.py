import sys
import heapq
input = sys.stdin.readline

N, K = map(int, input().split())
arr_N, arr_K = [], []
for _ in range(N):
    w, p = map(int,input().split())
    arr_N.append([w,p])
for _ in range(K):
    arr_K.append(int(input()))
arr_N.sort(key=lambda x: x[0])
arr_K.sort()
result = 0
i = 0
hq = []
for bag in arr_K:
    while i<N and bag>=arr_N[i][0]:
        heapq.heappush(hq,-arr_N[i][1])
        i+=1
    if hq:
        result-=heapq.heappop(hq)
print(result)