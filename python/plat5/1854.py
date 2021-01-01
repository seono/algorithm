import sys
import heapq
from collections import deque
input = sys.stdin.readline
output = sys.stdout.write

n, m, k = map(int,input().split())

adj = [[] for _ in range(n+1)]
for _ in range(m):
    a,b,c = map(int,input().split())
    adj[a].append([b,c])

def bfs(b):
    visited = [False]*(n+1)
    st = deque([])
    for x,_ in adj[1]:
        visited[x]=True
        st.append(x)
    while st:
        p = st.popleft()
        if p==b:
            return True
        for nx,_ in adj[p]:
            if visited[nx]:continue
            visited[nx]=True
            st.append(nx)
    return False

def bfs_cnt(b,c):
    st = [[0,1]]
    visited = [0]*(n+1)
    while st:
        cnt,p = heapq.heappop(st)
        if p==b:
            c-=1
            if c==0:
                return cnt
        visited[p]+=1
        if visited[p]>c:
            continue
        for nx,ncnt in adj[p]:
            heapq.heappush(st,[cnt+ncnt,nx])

for i in range(1,n+1):
    if bfs(i):
        output("%d\n"%bfs_cnt(i,k))
    else:
        output("-1\n")