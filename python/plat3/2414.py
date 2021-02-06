import sys
input = sys.stdin.readline

N, M = map(int,input().split())
arr = [list(input().strip()) for _ in range(N)]
arr1 = [[0]*M for _ in range(N)]
arr2 = [[0]*M for _ in range(N)]
w,h = 1,1
for y in range(N):
    fl = False
    for x in range(M):
        if arr[y][x]=='*':
            if fl:
                w+=1
                fl=False
            arr1[y][x]=w
        else:
            fl=True
    w+=1
for x in range(M):
    fl = False
    for y in range(N):
        if arr[y][x]=='*':
            if fl:
                h+=1
                fl=False
            arr2[y][x]=h
        else:
            fl=True
    h+=1

adj = [[] for _ in range(h)]
for y in range(N):
    for x in range(M):
        if arr[y][x]=='*':
            adj[arr2[y][x]].append(arr1[y][x])

p = [-1]*w
   
def dfs(idx):
    if visited[idx]:return False
    visited[idx]=True
    for nx in adj[idx]:
        if p[nx]==-1 or dfs(p[nx]):
            p[nx]=idx
            return True
    return False
ans = 0
for i in range(1,h):
    visited = [False]*h
    if dfs(i):
        ans+=1
print(ans)