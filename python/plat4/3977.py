import sys
sys.setrecursionlimit(100000)
input = sys.stdin.readline

T = int(input())
def scc(curr):
    global cnt,SN
    dfsn[curr] = cnt+1
    cnt+=1
    st.append(curr)
    res = dfsn[curr]
    for nx in adj[curr]:
        if dfsn[nx]==0:res = min(res, scc(nx))
        elif not finished[nx]: res = min(res,dfsn[nx])
    
    if res == dfsn[curr]:
        curSCC = []
        while True:
            t = st.pop()
            curSCC.append(t)
            finished[t]=True
            sccNum[t]=SN
            if t==curr:break
        SCC.append(curSCC)
        SN+=1
    return res
def sol():
    new_edge = set([num for num in range(len(SCC))])
    for i,sc in enumerate(SCC):
        for n in sc:
            for nx in adj[n]:
                if sccNum[nx]==i:continue
                if sccNum[nx] in new_edge:
                    new_edge.remove(sccNum[nx])
    if len(new_edge)==1:
        idx = list(new_edge)[0]
        return '\n'.join(map(str,sorted(SCC[idx])))
    return "Confused"
while T:
    N, M = map(int,input().split())
    adj = [[] for _ in range(N)]
    for _ in range(M):
        a,b=map(int,input().split())
        adj[a].append(b)
    dfsn=[0]*(N)
    st = []
    finished = [False]*(N)
    cnt = 0
    SN = 0
    sccNum = [0]*(N)
    SCC = []
    for i in range(N):
        if dfsn[i]==0:scc(i)
    print(sol())
    print()
    T-=1
    if T:
        input()