import sys
input = sys.stdin.readline

n = int(input())
m = 1
tmp = 1
while tmp<n:
    tmp<<=1
    m+=1
adj = [[] for _ in range(n+1)]
sys.setrecursionlimit(100000)
for i in range(n-1):
    a,b =map(int,input().split())
    adj[a].append(b)
    adj[b].append(a)

dp_arr = [[-1]*(m) for _ in range(n+1)]
visited = [False]*(n+1)

def dp(idx,now,p):
    if dp_arr[idx][now]!=-1:
        return dp_arr[idx][now]
    ret = now
    for nx in adj[idx]:
        if nx==p:continue
        q = 1e9
        for i in range(1,m):
            if i==now:continue
            q = min(q,dp(nx,i,idx))
        ret+=q
    dp_arr[idx][now]=ret
    return ret

visited[1]=True
ans = 1e9
for i in range(1,m):
    ans=min(ans,dp(1,i,0))
print(ans)