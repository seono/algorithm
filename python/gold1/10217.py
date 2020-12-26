import sys
import heapq
input = sys.stdin.readline

T = int(input())
def sol():
    N, M, K = map(int,input().split())
    INF = sys.maxsize
    arr = [[] for _ in range(N+1)]
    dp = [[INF]*(M+1) for _ in range(N+1)]
    for _ in range(K):
        u, v, c, h = map(int, input().split())
        arr[u].append([v,c,h])
    dp[1][0]=0
    q = [(0,1,0)]
    ans = INF
    while q:
        ndist,nst,ncost = heapq.heappop(q)
        if dp[nst][ncost]<ndist:continue
        if nst==N:
            ans = ndist
            break
        for v,c,h in arr[nst]:
            if c+ncost>M:continue
            h+=ndist
            c+=ncost
            if dp[v][c]<=h:continue
            for t in range(c,M+1):
                dp[v][t]=min(dp[v][t],h)
            heapq.heappush(q,(h,v,c))
    
    if ans==INF:print('Poor KCM')
    else: print(ans)
    return

while T:
    T-=1
    sol()