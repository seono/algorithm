import sys
input = sys.stdin.readline
import heapq


K, N = map(int, input().split())

num_list = list(map(int, input().split()))
hq = []
for num in num_list:
    heapq.heappush(hq, num)

n = 0
N-=1
while N:
    N-=1
    n = heapq.heappop(hq)
    for num in num_list:
        new_n = n * num
        heapq.heappush(hq, new_n)
        if n % num == 0:
            break
print(heapq.heappop(hq))