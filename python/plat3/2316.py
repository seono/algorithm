import sys
from collections import deque
input = sys.stdin.readline

N, P = map(int,input().split())
mN = N<<1|1
arr = [[] for _ in range(mN)]
cap = [[0]*mN for _ in range(mN)]
fl = [[0]*mN for _ in range(mN)]

def dfs(st,ed):
    ans = 0
    while True:
        visited = [-1]*mN
        q = deque([st])
        visited[0]=0
        while q:
            #print(q)
            n = q.popleft()
            for nx in arr[n]:
                if visited[nx]==-1 and cap[n][nx]>fl[n][nx]:
                    q.append(nx)
                    visited[nx]=n
                    if nx==ed:break
        if visited[ed]==-1:break
        now = ed
        while now!=st:
            fl[visited[now]][now]+=1
            fl[now][visited[now]]-=1
            now = visited[now]
        ans+=1
    return ans

for i in range(1,N+1):
    in_a = (i<<1)-2
    out_a = (i<<1)-1
    arr[in_a].append(out_a)
    cap[in_a][out_a]=1

for i in range(P):
    a,b = map(int,input().split())
    in_a = (a<<1)-2
    out_a = (a<<1)-1
    in_b = (b<<1)-2
    out_b = (b<<1)-1
    arr[out_a].append(in_b)
    arr[in_b].append(out_a)
    cap[out_a][in_b]=1
    arr[out_b].append(in_a)
    arr[in_a].append(out_b)
    cap[out_b][in_a]=1
print(dfs(1,2))