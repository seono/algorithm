import sys
from collections import deque
input = sys.stdin.readline

T = int(input())
sys.setrecursionlimit(100000)

def dfs(now):
    visited[now]=True
    for nx in adj_f[now]:
        if visited[nx]:continue
        dfs(nx)
    global cur_time
    finish_time.append(now)
    return
def dfs_b(now,idx):
    visited[now]=True
    scc[idx].append(now)
    scc_dict[now]=idx
    for nx in adj_b[now]:
        if visited[nx]:continue
        dfs_b(nx,idx)


while T:
    T-=1

    N, M = map(int,input().split())
    ans = 0
    adj_f = [[] for _ in range(N+1)]
    adj_b = [[] for _ in range(N+1)]
    finish_time = [0]*(N+1)
    scc = []
    cur_time = 0
    for _ in range(M):
        x,y = map(int,input().split())
        adj_f[x].append(y)
        adj_b[y].append(x)
    visited = [False]*(N+1)
    for num in range(1,N+1):
        if visited[num]:continue
        dfs(num)
    visited = [False]*(N+1)
    i=0
    scc_dict = [0]*(N+1)
    for num in finish_time[::-1]:
        if visited[num]:continue
        scc.append([])
        dfs_b(num,i)
        i+=1
    indegree = [0]*(len(scc)+1)
    adj = [[] for _ in range(len(scc)+1)]
    visited = [False]*(N+1)
    scc.pop()
    for idx,sc in enumerate(scc):
        for num in sc:
            for nx in adj_f[num]:
                if nx in sc:continue
                adj[idx].append(scc_dict[nx])
                indegree[scc_dict[nx]]+=1
    q = deque()
    for num in range(len(scc)):
        if indegree[num]==0:
            ans+=1
    print(ans)