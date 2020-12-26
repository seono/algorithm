import sys
input = sys.stdin.readline

N = int(input())

cost = list(map(int,input().split()))
arr = [[] for _ in range(N+1)]
for i in range(N-1):
    a,b = map(int,input().split())
    arr[a-1].append(b-1)
    arr[b-1].append(a-1)
dp = [[0,0] for _ in range(N+1)]
visited = [False]*(N+1)
def dfs(cur):
    if visited[cur]: return
    visited[cur]=True
    dp[cur][0] = 0
    dp[cur][1] = cost[cur]

    for nx in arr[cur]:
        if visited[nx]:continue
        
        dfs(nx)

        dp[cur][0] = dp[cur][0] + max(dp[nx][0], dp[nx][1])

        dp[cur][1] = dp[cur][1] + dp[nx][0]
    
    return max(dp[cur])
sys.setrecursionlimit(10001)
print(dfs(0))