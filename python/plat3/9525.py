import sys
input = sys.stdin.readline

N = int(input())
arr = [list(map(str,input().strip())) for _ in range(N)]

right = [[0]*N for _ in range(N)]
down = [[0]*N for _ in range(N)]
r,d=1,1
for x in range(N):
    flag = False
    for y in range(N):
        if arr[y][x]=='.':
            if flag:
                d+=1
                flag=False
            down[y][x]=d
        else:
            flag=True
    d+=1
for y in range(N):
    flag = False
    for x in range(N):
        if arr[y][x]=='.':
            if flag:
                r+=1
                flag=False
            right[y][x]=r
        else:
            flag=True
    r+=1
adj = [[] for _ in range(r)]
for y in range(N):
    for x in range(N):
        if arr[y][x]=='.':
            adj[right[y][x]].append(down[y][x])
N_max = N*N+1
p = [-1]*(N_max)
b = [-1]*(N_max)
def dfs(idx):
    if visited[idx]:return False
    visited[idx]=True
    for nx in adj[idx]:
        if p[nx]==-1 or dfs(p[nx]):
            p[nx]=idx
            b[idx]=nx
            return True
    return False

ans = 0
for i in range(1,r):
    visited = [False]*r
    if dfs(i):ans+=1
print(ans)
