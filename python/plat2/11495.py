import sys
from collections import defaultdict,deque
input = sys.stdin.readline

d = [(0,1),(0,-1),(1,0),(-1,0)]

T = int(input())
while T:
    T-=1
    n, m = map(int,input().split())
    arr = []
    for i in range(n):
        arr+=[*map(int,input().split())]
    max_n = n*m+2
    cap = [[0]*max_n for _ in range(max_n)]
    fl = [[0]*max_n for _ in range(max_n)]
    adj = [[] for _ in range(max_n)]
    S = max_n-2;E = max_n-1
    for y in range(n):
        for x in range(m):
            now = y*m+x
            if (y%2) ^ (x%2):
                adj[now].append(E)
                adj[E].append(now)
                cap[now][E]=arr[now]
            else:
                adj[now].append(S)
                adj[S].append(now)
                cap[S][now]=arr[now]
                for dy,dx in d:
                    ny,nx= y+dy,x+dx
                    if 0<=ny<n and 0<=nx<m:
                        to = ny*m+nx
                        adj[now].append(to)
                        adj[to].append(now)
                        cap[now][to]=arr[now]
    ans = sum(arr)
    while True:
        visited = [-1]*max_n
        q = deque()
        q.append(S)
        while q and visited[E]==-1:
            n = q.popleft()
            for nx in adj[n]:
                if visited[nx]==-1 and cap[n][nx]>fl[n][nx]:
                    visited[nx]=n
                    q.append(nx)
                    if nx==E:break
        if visited[E]==-1:break
        flow = 1e9
        now = E
        while now!=S:
            flow = min(flow,cap[visited[now]][now] - fl[visited[now]][now])
            now = visited[now]
        now = E
        while now!=S:
            fl[visited[now]][now]+=flow
            fl[now][visited[now]]-=flow
            now = visited[now]
        ans-=flow
    print(ans)
    