import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int,input().split())
S,E = 801,802
Total_num = 803
cap = [[0]*Total_num for _ in range(Total_num)]
fl = [[0]*Total_num for _ in range(Total_num)]
d = [[0]*Total_num for _ in range(Total_num)]
adj = [[] for _ in range(Total_num*2+3)]
for i in range(1,N+1):
    adj[S].append(i)
    adj[i].append(S)
    cap[S][i]=1

for i in range(1,M+1):
    adj[i+400].append(E)
    adj[E].append(i+400)
    cap[i+400][E]=1

for i in range(1,N+1):
    row = list(map(int,input().split()))
    for j in range(1,row[0]+1):
        work, cost = row[(j<<1)-1],row[j<<1]
        adj[i].append(work+400)
        adj[work+400].append(i)
        cap[i][work+400]=1
        d[i][work+400]+=cost
        d[work+400][i]-=cost
    
def sol():
    result = 0
    ans = 0
    while True:
        visited = [-1]*(Total_num)
        dist = [1e9]*Total_num
        chk = [False]*Total_num
        q = deque([S])
        dist[S]=0
        while q:
            n = q.popleft()
            chk[n]=False
            for nx in adj[n]:
                if cap[n][nx]>fl[n][nx] and dist[nx]>dist[n]+d[n][nx]:
                    dist[nx]=dist[n]+d[n][nx]
                    visited[nx]=n
                    if not chk[nx]:
                        q.append(nx)
                        chk[nx]=True
        if visited[E]==-1:
            break
        flow = 1e9
        now = E
        while now!=S:
            flow = min(flow,cap[visited[now]][now]-fl[visited[now]][now])
            now = visited[now]
        now = E
        while now!=S:
            result += d[visited[now]][now]*flow
            fl[visited[now]][now]+=flow
            fl[now][visited[now]]-=flow
            now = visited[now]
        ans+=flow
    print(ans)
    print(result)
    return
sol()