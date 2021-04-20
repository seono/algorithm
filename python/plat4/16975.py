import sys
input = sys.stdin.readline
output = sys.stdout.write

N = int(input())
st = 1
while st<=N:
    st<<=1
tree = [0]*(st<<1)
lazy = [0]*(st<<1)

for idx,num in enumerate(list(map(int,input().split()))):
    tree[idx+st] = num

temp = st
while temp>1:
    ed = temp
    temp>>=1
    for idx in range(temp,ed):
        tree[idx] = tree[idx<<1]+tree[idx<<1|1]

def propagate(node, ns, ne):
    if lazy[node]:
        tree[node] +=lazy[node]
        if ns!=ne:
            lazy[node<<1] += lazy[node]
            lazy[node<<1|1] += lazy[node]
        lazy[node] = 0

def update(ns,ne,s,e,node,k):
    propagate(node,ns,ne)
    if ns>e or ne<s : return
    if s<=ns and ne<=e:
        tree[node]+=k
        if ns!=ne:
            lazy[node<<1]+=k
            lazy[node<<1|1]+=k
        return
    mid = (ns+ne)>>1
    update(ns,mid,s,e,node<<1,k)
    update(mid+1,ne,s,e,node<<1|1,k)
    tree[node]=tree[node<<1]+tree[node<<1|1]

def query(ns,ne,s,e,node):
    propagate(node,ns,ne)
    if e<ns or s>ne: return 0
    if s<=ns and ne<=e: return tree[node]
    mid = (ne+ns)>>1
    return query(ns,mid,s,e,node<<1) + query(mid+1,ne,s,e,node<<1|1)

M = int(input())
for i in range(M):
    row = list(map(int,input().split()))
    if row[0]==1:
        update(1,st,row[1],row[2],1,row[3])
    else:
        output("%d\n"%query(1,st,row[1],row[1],1))