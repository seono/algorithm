import sys
input = sys.stdin.readline
output = sys.stdout.write

sys.setrecursionlimit(1000000)
N, Q = map(int,input().split())
adj = [[] for _ in range(N+1)]
for i in range(2,N+1):
    n = int(input())
    adj[n].append(i)
# 자식의 범위
leaf = [0]*(N+1)
realNum = [-1]*(N+1)
depth = [0]*(N+1)
arr = [[-1]*21 for _ in range(N+1)]
st = 1
while st<=N:
    st<<=1

tree = [0]*(st<<1)
lazy = [0]*(st<<1)
arr = [[-1]*21 for _ in range(N+1)]

def assignID(idx):
    start = 1
    st = [idx]
    while st:
        now = st.pop()
        realNum[now]=start
        start+=1
        for nx in adj[now]:
            st.append(nx)

def dfs(idx):
    ret = realNum[idx]
    for nx in adj[idx]:
        arr[realNum[nx]][0]=realNum[idx]
        depth[realNum[nx]]=depth[realNum[idx]]+1
        ret = max(ret,dfs(nx))
    leaf[realNum[idx]]=ret
    return ret

assignID(1)
dfs(1)

def propagate(s,e,node):
    if not lazy[node]: return
    tree[node] = max(lazy[node],tree[node])
    if s!=e:
        lazy[node<<1] = max(lazy[node<<1],lazy[node])
        lazy[node<<1|1] = max(lazy[node<<1|1], lazy[node])
    lazy[node] = 0


def query(ns,ne,s,e,node):
    propagate(ns,ne,node)
    if ns>e or ne<s: return -sys.maxsize
    if s<=ns and ne<=e: return tree[node]
    mid = (ns+ne)>>1
    return max(query(ns,mid,s,e,node<<1),query(mid+1,ne,s,e,node<<1|1))

def update(ns,ne,s,e,node,val):
    propagate(ns,ne,node)
    if ns>e or ne<s: return tree[node]
    if s<=ns and ne<=e:
        lazy[node] = max(lazy[node],val)
        propagate(ns,ne,node)
        return tree[node]
    mid = (ns+ne)>>1
    tree[node] = max(update(ns,mid,s,e,node<<1,val),update(mid+1,ne,s,e,node<<1|1,val))
    return tree[node]

def LCA(x,y):
    px = depth[x] - query(1,N,x,x,1)
    py = depth[y] - query(1,N,y,y,1)
    for j in range(20,-1,-1):
        if arr[x][j] and px >= (1<<j):
            px -= (1<<j)
            x = arr[x][j]
        if arr[y][j] and py >= (1<<j):
            py -= (1<<j)
            y = arr[y][j]
    return x==y

for i in range(1,21):
    for j in range(1,N+1):
        arr[j][i] = arr[arr[j][i-1]][i-1]



for _ in range(Q):
    b,c,d = map(int,input().split())
    chk = LCA(realNum[b],realNum[c])
    if d:
        if chk:
            update(1,N,realNum[b],leaf[realNum[b]],1,depth[realNum[b]])
        else:
            update(1,N,realNum[c],leaf[realNum[c]],1,depth[realNum[c]])
    if chk:
        output("YES\n")
    else:
        output("NO\n")