import sys

input = sys.stdin.readline
output = sys.stdout.write

N, M = map(int,input().split())

tree = [0]*(4*N)
lazy = [0]*(4*N)

def propagate(node,now_s,now_e):
    if lazy[node]:
        tree[node]=(now_e-now_s+1)-tree[node]
        if now_s!=now_e:
            lazy[node<<1]^=1
            lazy[node<<1|1]^=1
        lazy[node]=0

def update(now_s,now_e,s,e,node):
    propagate(node,now_s,now_e)
    if now_s>e or now_e<s:return
    if s<=now_s and now_e<=e:
        tree[node]=(now_e-now_s+1)-tree[node]
        if now_s!=now_e:
            lazy[node<<1]^=1
            lazy[node<<1|1]^=1
        return
    mid = (now_e+now_s)>>1
    update(now_s,mid,s,e,node<<1)
    update(mid+1,now_e,s,e,node<<1|1)
    tree[node]=tree[node<<1] + tree[node<<1|1]

def query(now_s,now_e,s,e,node):
    propagate(node,now_s,now_e)
    if e<now_s or s>now_e:return 0
    if s<=now_s and now_e<=e:return tree[node]
    mid = (now_e+now_s)>>1
    return query(now_s,mid,s,e,node<<1)+query(mid+1,now_e,s,e,node<<1|1)

for _ in range(M):
    cmd, i, j = map(int,input().split())
    if cmd==0:
        update(1,N,i,j,1)
    else:
        output("%d\n"%query(1,N,i,j,1))
    #print(tree[:2*N])