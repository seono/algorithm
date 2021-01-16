import sys
input = sys.stdin.readline

N, M, K = map(int,input().split())
arr = [[]]

def bfs(idx):
    visited[idx]=True
    for nx in arr[idx]:
        if p[nx]==-1 or (not visited[p[nx]] and bfs(p[nx])):
            p[nx]=idx
            return True
    return False

p = [-1]*(M+1)
for _ in range(N):
    arr.append(list(map(int,input().split()))[1:])
ans = 0
for idx in range(1,N+1):
    visited = [False]*(N+1)
    if bfs(idx):ans+=1
for idx in range(1,N+1):
    visited = [False]*(N+1)
    if bfs(idx):
        ans+=1
        K-=1
        if K==0:
            break
print(ans)