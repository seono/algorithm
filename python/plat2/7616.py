import sys
from collections import deque
input = sys.stdin.readline
print = sys.stdout.write

def dfs():
    #global st,ed,adj,cap,fl,N,K,T
    ans = []
    chk =  [0]*(N+1)
    while True:
        visited = [-1]*(N+1)
        q = deque([st])
        while q:
            n = q.popleft()
            for nx in adj[n]:
                if chk[nx]==0 and visited[nx]==-1 and cap[n][nx] > fl[n][nx]:
                    q.append(nx)
                    visited[nx]=n
                    if nx==ed:break
        if visited[ed]==-1:break
        
        now = ed
        tmp = [ed]
        while now!=st:
            chk[now]=1
            fl[visited[now]][now]+=1
            fl[now][visited[now]]-=1
            now = visited[now]
            tmp.append(now)
        ans.append(tmp)
        chk[ed]=0
    print("Case %d:\n"%T)
    if len(ans)>=K:
        for row in ans[:K]:
            print(" ".join(map(str,row[::-1])))
            print("\n")
        print("\n")
    else:
        print("Impossible\n\n")


st,ed = 1,2
T = 0
while True:
    T+=1
    K, N = map(int,input().split())
    if K==0 and N==0:break
    cap = [[0]*(N+1) for _ in range(N+1)]
    fl = [[0]*(N+1) for _ in range(N+1)]
    adj = [[] for _ in range(N+1)]
    for i in range(1,N+1):
        row = list(map(int,input().split()))
        for r in row:
            cap[i][r]=1
            cap[r][i]=1
        adj[i]=row[::-1]
    dfs()