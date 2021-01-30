import sys
from collections import deque
input = sys.stdin.readline
print = sys.stdout.write

def dfs():
    #global st,ed,adj,cap,fl,N,K,T
    ans=0
    while True:
        visited = [-1]*(N+1)
        q = [st]
        while q:
            n = q.pop()
            for nx in adj[n]:
                if visited[nx]==-1 and cap[n][nx] > fl[n][nx]:
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

def bfs():
    ans = []
    while True:
        visited = [-1]*(N+1)
        q = deque([st])
        while q:
            n = q.popleft()
            for nx in adj[n]:
                if visited[nx]==-1 and fl[n][nx]:
                    q.append(nx)
                    visited[nx]=n
                    if nx==ed:break
        if visited[ed]==-1:break
        now = ed
        tmp = [ed]
        while now!=st:
            fl[visited[now]][now]=0
            fl[now][visited[now]]=0
            now=visited[now]
            if now%2==0:
                tmp.append(now//2+1)
        ans.append([1]+tmp[::-1])
    print("Case %d:\n"%T)
    if len(ans)>=K:
        for row in ans[:K]:
            print(" ".join(map(str,row))+"\n")
        print("\n")
    else:
        print("Impossible\n\n")

st,ed = 1,2
T = 0
while True:
    T+=1
    K, N = map(int,input().split())
    tmp = N
    if K==0 and N==0:break
    N=N<<1|1
    cap = [[0]*(N) for _ in range(N)]
    fl = [[0]*(N) for _ in range(N)]
    adj = [[] for _ in range(N)]
    for i in range(1,tmp+1):
        row = list(map(int,input().split()))
        in_a = (i<<1)-2
        out_a = (i<<1)-1
        adj[in_a].append(out_a)
        cap[in_a][out_a]=1
        for r in row:
            in_b = (r<<1)-2
            out_b = (r<<1)-1
            adj[out_a].append(in_b)
            adj[in_b].append(out_a)
            cap[out_a][in_b]=1
            adj[out_b].append(in_a)
            adj[in_a].append(out_b)
            cap[out_b][in_a]=1
    dfs()
    bfs()
    #print(adj)