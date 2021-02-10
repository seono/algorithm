import sys
from collections import deque,defaultdict
input = sys.stdin.readline


N, M = map(int,input().split())
MAX_N = (N*M)<<1|1
arr = [input().strip() for _ in range(N)]

adj = [[] for _ in range(MAX_N)]

cap = defaultdict(int)
fl = defaultdict(int)


d = [(0,1),(1,0),(-1,0),(0,-1)]
for i in range(N*M):
    f = i<<1
    t = i<<1|1
    cap[(f,t)]=1
    adj[f].append(t)
    adj[t].append(f)
sy,sx,ey,ex=-1,-1,-1,-1
S, T = -1,-1
for y in range(N):
    for x in range(M):
        if arr[y][x]=='K':
            sy,sx =y,x
            S = (y*M+x)<<1|1
        if arr[y][x]=='H':
            ey,ex = y,x
            T = (y*M+x)<<1
        if arr[y][x]!='#':
            now_out = (y*M+x)<<1|1
            for dy,dx in d:
                ny,nx=y+dy,x+dx
                if 0<=ny<N and 0<=nx<M and arr[ny][nx]!='#':
                    next_in = (ny*M+nx)<<1
                    adj[now_out].append(next_in)
                    cap[(now_out,next_in)]=1
                    adj[next_in].append(now_out)
if (N==1 and M==1) or S==-1 or T==-1 or abs(sy-ey)+abs(sx-ex)==1:
    print(-1)
    exit(0)
ans = 0
while True:
    visited = [-1]*MAX_N
    q = deque()
    q.append(S)
    while q:
        n = q.popleft()
        for nx in adj[n]:
            if visited[nx]==-1 and cap[(n,nx)]>fl[(n,nx)]:
                q.append(nx)
                visited[nx]=n
                if nx==T:break
    if visited[T]==-1:break

    now = T
    while now!=S:
        fl[(visited[now],now)]+=1
        fl[(now,visited[now])]-=1
        now = visited[now]
    
    ans+=1
print(ans)