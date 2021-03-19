import sys
import heapq
input = sys.stdin.readline
output = sys.stdout.write

N = int(input())
left,right = [],[]

ans = []
for i in range(N):
    n = int(input())
    if len(left)==len(right):
        heapq.heappush(left,-n)
    else:
        heapq.heappush(right,n)
    
    if right and -left[0]>right[0]:
        l_v = -heapq.heappop(left)
        r_v = heapq.heappop(right)
        heapq.heappush(left,-r_v)
        heapq.heappush(right,l_v)
    ans.append(-left[0])

output("%s"%'\n'.join(map(str,ans)))