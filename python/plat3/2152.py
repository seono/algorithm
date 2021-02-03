import sys
from collections import deque
sys.setrecursionlimit(100000)
input = sys.stdin.readline

N, M, S, T = map(int,input().split())
adj = [[] for _ in range(N+1)]
for i in range(M):
    s,t = map(int,input().split())
    adj[s].append(t)
cnt,SN = 0,0
dfsn = [0]*(N+1)
scc_arr = []
scc_num = [0]*(N+1)
finished = [False]*(N+1)
st = []

def scc(idx):
    global cnt,SN
    dfsn[idx] = cnt+1
    cnt+=1
    st.append(idx)
    result = dfsn[idx]
    for nx in adj[idx]:
        if dfsn[nx]==0:result = min(result,scc(nx))
        elif not finished[nx]: result = min(result, dfsn[nx])

    if result == dfsn[idx]:
        curSCC = []
        while True:
            t = st.pop()
            curSCC.append(t)
            finished[t]=True
            scc_num[t]=SN
            if t==idx:break
        scc_arr.append(curSCC)
        SN+=1
    return result

for i in range(1,N+1):
    if dfsn[i]==0:scc(i)
new_adj = [[] for _ in range(SN)]
indgree = [0]*SN
finished = [0]*SN
new_s,new_t = scc_num[S],scc_num[T]
for i,tmp in enumerate(scc_arr):
    for n in tmp:
        for nx in adj[n]:
            if scc_num[nx]==i:continue
            new_adj[i].append(scc_num[nx])
            indgree[scc_num[nx]]+=1
def dfs():
    st = deque([new_s])
    can = [False]*SN
    can[new_s]=True
    finished[new_s]=len(scc_arr[new_s])
    q = deque([])
    for i in range(SN):
        if not indgree[i]: q.append(i)
    while q:
        n = q.popleft()
        for nx in new_adj[n]:
            if can[n]:
                finished[nx]=max(finished[nx],finished[n]+len(scc_arr[nx]))
                can[nx]=True
            indgree[nx]-=1
            if indgree[nx]==0:
                q.append(nx)
    return finished[new_t]
print(dfs())