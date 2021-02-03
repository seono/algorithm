import sys
input = sys.stdin.readline
T = int(input())
d = [(-1,-1),(0,-1),(1,-1),(-1,1),(0,1),(1,1)]
def dfs(idx):
    if visited[idx]:return False
    visited[idx]=True
    for nx in adj[idx]:
        if p[nx]==-1 or dfs(p[nx]):
            p[nx]=idx
            return True
    return False
while T:
    T-=1
    N, M = map(int,input().split())
    arr = [list(input().strip()) for _ in range(N)]
    adj = [[] for _ in range(6401)]
    p = [-1]*6401
    total = 0
    for x in range(M):
        for y in range(N):
            if arr[y][x]=='x':continue
            total+=1
            if x%2:continue
            for dy,dx in d:
                ny,nx = y+dy,x+dx
                if 0<=ny<N and 0<=nx<M and arr[ny][nx]=='.':
                    adj[y*80+x].append(ny*80+nx)
    ans = 0
    for i in range(6401):
        visited = [False]*6401
        if dfs(i):ans+=1
    print(total-ans)