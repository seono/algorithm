import sys
input = sys.stdin.readline
sys.setrecursionlimit(100000)

N, M = map(int,input().split())
dfsn = [0]*(N<<1|1)
cnt = 0
SN = 0
st = []
sccNum = [0]*(N<<1|1)
finished = [False]*(N<<1|1)
scc_arr = []
def scc(curr):
    global cnt, SN
    dfsn[curr] = cnt+1
    cnt+=1
    st.append(curr)
    result = dfsn[curr]
    for nx in adj[curr]:
        if dfsn[nx]==0:result = min(result,scc(nx))
        elif not finished[nx]: result = min(result,dfsn[nx])
    
    if result==dfsn[curr]:
        curSCC = []
        while True:
            t = st.pop()
            curSCC.append(t)
            finished[t]=True
            sccNum[t]=SN
            if t==curr:break
        SN+=1
        scc_arr.append(curSCC)
    
    return result
def oppo(n):return n-1 if n%2 else n+1

adj = [[] for _ in range(2*N+1)]
for _ in range(M):
    a,b=map(int,input().split())
    a = -(a+1)*2 if a<0 else 2*a-1
    b = -(b+1)*2 if b<0 else 2*b-1
    adj[oppo(a)].append(b)
    adj[oppo(b)].append(a)

for i in range(N*2):
    if dfsn[i]==0:scc(i)

def sol():
    #print(scc_arr)
    for i in range(N):
        if sccNum[i<<1] ==sccNum[i<<1|1]:
            print(0)
            return
    result = [-1]*(N+1)
    p = [(sccNum[i],i) for i in range(N*2)]
    p.sort()
    for num in range(N*2-1,-1,-1):
        var = p[num][1]
        if result[var//2] == -1:
            result[var//2] = 0 if var%2 else 1
    print(1)
    print(' '.join(map(str,result[:-1])))
    return
sol()