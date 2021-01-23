import sys
sys.setrecursionlimit(100000)
input = sys.stdin.readline

N, M = map(int,input().split())
dfsn = [0]*(N*2+1)
cnt = 0
SN = 0
st = []
sccNum = [0]*(N*2+1)
finished = [False]*(N*2+1)
def scc(curr):
    global cnt,SN
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
    
    return result
def oppo(n):return n-1 if n%2 else n+1

adj = [[] for _ in range(2*N+1)]
for _ in range(M):
    a,b=map(int,input().split())
    a = -(a+1)*2 if a<0 else 2*a-1
    b = -(b+1)*2 if b<0 else 2*b-1
    adj[oppo(a)].append(b)
    adj[oppo(b)].append(a)

for i in range(2*N):
    if dfsn[i]==0:scc(i)

def sol():
    for i in range(N):
        if sccNum[i*2] == sccNum[i*2+1]:
            print(0)
            return
    print(1)
sol()