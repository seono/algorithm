import sys
input = sys.stdin.readline
output = sys.stdout.write

N = int(input())
st = 1
while st<=N:
    st<<=1
tree = [(sys.maxsize,-1)]*(st<<1)
lazy = [(sys.maxsize,-1)]*(st<<1)


for idx, num in enumerate(list(map(int,input().split()))):
    tree[st+idx]=(num,idx+1)

temp = st
while temp>1:
    ed = temp
    temp >>=1
    for i in range(temp,ed):
        tree[i] = min(tree[i<<1],tree[i<<1|1])

def propagate(s,e,node):
    if lazy[node][1]==-1:return
    tree[node] = lazy[node]
    if s!=e:
        lazy[node<<1] = min(lazy[node<<1], lazy[node])
        lazy[node<<1|1] = min(lazy[node<<1|1], lazy[node])
    lazy[node] = (sys.maxsize,-1)

def update(ns,ne,s,e,node,val):
    propagate(ns,ne,node)
    if ns>e or ne<s: return tree[node]
    if s<=ns and ne<=e:
        lazy[node] = min(lazy[node],val)
        propagate(ns,ne,node)
        return tree[node]
    mid = (ne+ns)>>1
    tree[node] = min(update(ns,mid,s,e,node<<1,val),update(mid+1,ne,s,e,node<<1|1,val))
    return tree[node]

def query(ns,ne,s,e,node):
    propagate(ns,ne,node)
    if ns>e or ne<s: return (sys.maxsize,-1)
    if s<=ns and ne<=e: return tree[node]
    mid = (ns+ne)>>1
    return min(query(ns,mid,s,e,node<<1),query(mid+1,ne,s,e,node<<1|1))

for _ in range(int(input())):
    cmd, a, b = map(int,input().split())
    if cmd==1:
        update(1,st,a,a,1,(b,a))
    else:
        print(query(1,st,a,b,1)[1])