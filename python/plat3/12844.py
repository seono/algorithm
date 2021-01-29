import sys
input = sys.stdin.readline
output = sys.stdout.write

N = int(input())
st = 1
while st<N:
    st<<=1
tree = [0]*(st*2)
temp = st
tree[st:st+N] = list(map(int,input().split()))
while temp>1:
    ed = temp
    temp = temp>>1
    for i in range(temp,ed):
        tree[i]=tree[i<<1]^tree[i<<1|1]
lazy = [0]*(st*2)

def propagate(node, ns, ne):
    if lazy[node]:
        if (ne-ns+1)%2:
            tree[node]^=lazy[node]
        if ns!=ne:
            lazy[node<<1]^=lazy[node]
            lazy[node<<1|1]^=lazy[node]
        lazy[node]=0
    return

def update(ns,ne,s,e,node,k):
    propagate(node,ns,ne)
    if ns>e or ne<s:return
    if s<=ns and ne<=e:
        if (ne-ns+1)%2:
            tree[node]^=k
        if ns!=ne:
            lazy[node<<1] ^= k
            lazy[node<<1|1] ^= k
        return
    mid = (ns+ne)>>1
    update(ns,mid,s,e,node<<1,k)
    update(mid+1,ne,s,e,node<<1|1,k)
    tree[node]=tree[node<<1]^tree[node<<1|1]

def query(ns,ne,s,e,node):
    propagate(node,ns,ne)
    if e<ns or s>ne:return 0
    if s<=ns and ne<=e:
        return tree[node]
    mid = (ne+ns)>>1
    return query(ns,mid,s,e,node<<1)^query(mid+1,ne,s,e,node<<1|1)

for _ in range(int(input())):
    row = list(map(int,input().split()))
    if row[0]==1:
        update(1,st,row[1]+1,row[2]+1,1,row[3])
    else:
        output("%d\n"%query(1,st,row[1]+1,row[2]+1,1))