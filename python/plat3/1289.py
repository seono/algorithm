import sys
input = sys.stdin.readline

M = 1000000007
N = int(input())
sys.setrecursionlimit(100000)
adj = [[] for _ in range(N+1)]
for i in range(N-1):
    a,b,cost = map(int,input().split())
    adj[a].append((b,cost))
    adj[b].append((a,cost))

ans = 0
def dp(idx, p):
    global ans, M
    ret = 1    
    for nx,cost in adj[idx]:
        if nx==p:continue
        tmp = (dp(nx,idx)*cost)%M
        ans=(ans+(ret*tmp)%M)%M
        ret=(ret+tmp)%M
    return ret

dp(1,0)
print(ans)