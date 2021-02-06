import sys
from collections import deque
sys.setrecursionlimit(500000)
input= sys.stdin.readline

N, M = map(int,input().split())
adj = [[] for _ in range(N+1)]
for i in range(M):
    s,t = map(int,input().split())
    adj[s].append(t)
cnt, SN = 0,0
dfsn = [-1]*(N+1)
scc_arr = []
scc_num = [-1]*(N+1)
st = []

def scc(idx):
    global cnt,SN
    dfsn[idx]=cnt+1
    cnt+=1
    st.append(idx)
    result = dfsn[idx]
    for nx in adj[idx]:
        if dfsn[nx]==-1:result = min(result,scc(nx))
        elif scc_num[nx]==-1: result = min(result, dfsn[nx])

    if result==dfsn[idx]:
        curSCC = []
        total_cost = 0
        while True:
            t = st.pop()
            curSCC.append(t)
            scc_num[t]=SN
            total_cost+=atm[t]
            if t==idx:break
        scc_arr.append(curSCC)
        new_atm.append(total_cost)
        SN+=1
    return result

atm = [0]
for i in range(N):
    atm.append(int(input()))
S, resnum = map(int,input().split())
new_atm = []
scc(S)
st = [[] for _ in range(SN)]
indegree = [0]*SN
finished = [0]*SN
S = scc_num[S]
def makenewadj(start):
    visited = [False]*SN
    visited[start] = True
    for n in scc_arr[start]:
        for nx in adj[n]:
            if scc_num[nx]!=-1 and not visited[scc_num[nx]]:
                st[start].append(scc_num[nx])
                indegree[scc_num[nx]]+=1
                visited[scc_num[nx]]=True
for i in range(S,-1,-1):
    makenewadj(i)
del adj,scc_arr,atm,dfsn
def dfs():
    finished[S] = new_atm[S]
    q = deque([S])
    while q:
        n = q.popleft()
        for nx in st[n]:
            finished[nx]=max(finished[nx], finished[n]+new_atm[nx])
            indegree[nx]-=1
            if indegree[nx]==0:
                q.append(nx)
    ret = 0
    for num in list(map(int,input().split())):
        ret = max(ret, finished[scc_num[num]])
    return ret
print(dfs())