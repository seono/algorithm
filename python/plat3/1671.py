import sys
input = sys.stdin.readline
output = sys.stdout.write

N = int(input())
#상어 네트워크 그래프 만들고(먹는놈->먹힐놈)
#이분탐색두번
#N-이분탐색두번결과
adj = [[] for _ in range(N)]
arr = []
def dfs(idx):
    visited[idx]=True
    for nx in adj[idx]:
        if p[nx]==-1 or (not visited[p[nx]] and dfs(p[nx])):
            p[nx]=idx
            return True
    return False

p = [-1]*N
for j in range(N):
    a,b,c = map(int,input().split())
    for i,n in enumerate(arr):
        na,nb,nc = n
        if na<=a and nb<=b and nc<=c:
            adj[j].append(i)
        elif a<=na and b<=nb and c<=nc:
            adj[i].append(j)
    arr.append((a,b,c))
ans = 0
for i in range(N):
    visited = [False]*N
    if dfs(i):ans+=1
for i in range(N):
    visited = [False]*N
    if dfs(i):ans+=1
print(N-ans)