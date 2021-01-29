import sys
input = sys.stdin.readline

n, k = map(int,input().split())

adj = [[] for _ in range(n)]
for _ in range(k):
    y,x = map(int,input().split())
    adj[y-1].append(x-1)

p = [-1]*(n)

def bfs(idx):
    visited[idx]=True
    for nx in adj[idx]:
        if p[nx]==-1 or (not visited[p[nx]] and bfs(p[nx])):
            p[nx]=idx
            return True

    return False
ans = 0
for i in range(n):
    visited=[False]*n
    if bfs(i):ans+=1
print(ans)