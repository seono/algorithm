import sys
input = sys.stdin.readline

N = int(input())
M = int(input())
INF = 101
arr = [[] for _ in range(101)]
dist = [[INF]*(N+1) for _ in range(N+1)]
visited=[False]*(N+1)
for _ in range(M):
    a, b = map(int,input().split())
    arr[a].append(b)
    arr[b].append(a)
    dist[a][b]=1
    dist[b][a]=1
group = []
g_cnt = 0
def bfs(idx):
    global N,g_cnt
    p = [idx]
    group.append([idx])
    visited[idx]=True
    while p:
        temp = p.pop(0)
        for n in arr[temp]:
            if visited[n]:
                continue
            p.append(n)
            visited[n]=True
            group[g_cnt].append(n)

for k in range(1,N+1):
    for i in range(1,N+1):
        for j in range(1,N+1):
            if i==j or j==k or k==i:
                continue
            dist[i][j]=min(dist[i][j],dist[i][k]+dist[k][j])
result = []
for i in range(1,N+1):
    if visited[i]:
        continue
    bfs(i)
    g_cnt+=1
for g in group:
    max_p = 101
    mi = g[0]
    for i in g:
        mx = 0
        for j in dist[i]:
            if j == INF:continue
            mx = max(mx,j)
        if mx<max_p:
            max_p=mx
            mi = i
    result.append(mi)
print(len(result))
print('\n'.join(map(str,sorted(result))))