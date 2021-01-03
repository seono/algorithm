import sys
from collections import deque

input = sys.stdin.readline
output = sys.stdout.write

V, E = map(int,input().split())
adj = [[] for _ in range(V+1)]

for _ in range(E):
    a,b = map(int,input().split())
    adj[a].append(b)
    adj[b].append(a)
dfn = [None]*(V+1)
low = [sys.maxsize]*(V+1)
ans = [False]*(V+1)
sys.setrecursionlimit(100000)
def dfs(idx, depth):
    dfn[idx]=ret=depth
    child = 0
    for nx in adj[idx]:
        if dfn[nx] is not None:
            ret = min(ret,dfn[nx])
        else:
            child+=1
            subtree = dfs(nx,depth+1)
            if depth!=1 and subtree>=dfn[idx]:
                ans[idx]=True
            ret = min(ret,subtree)
        
    if depth==1 and child>1:
        ans[idx]=True
    return ret
for i in range(1,V+1):
    if dfn[i] is None:
        dfs(i,1)
ans = [i for i,p in enumerate(ans[1:],1) if p]
print(len(ans))
print(*ans)