import sys
input = sys.stdin.readline
output = sys.stdout.write
V, E = map(int,input().split())

adj = [[] for _ in range(V+1)]
for _ in range(E):
    a,b = map(int,input().split())
    adj[a].append(b)
    adj[b].append(a)

dfn = [None]*(V+1)
ans = []
depth = 0
sys.setrecursionlimit(100000)

def dfs(idx,p):
    global depth
    depth+=1
    dfn[idx]=depth
    ret = depth
    for nx in adj[idx]:
        if nx==p:continue
        if dfn[nx] is not None:
            ret = min(ret,dfn[nx])
        else:
            subtree = dfs(nx,idx)
            if subtree>dfn[idx]:
                ans.append([nx,idx] if nx<idx else [idx,nx])
            ret = min(ret, subtree)
    return ret

for i in range(1,V+1):
    if dfn[i] is None: dfs(i,1)
output("%d\n"%len(ans))
for a,b in sorted(ans):
    output("%d %d\n"%(a,b))