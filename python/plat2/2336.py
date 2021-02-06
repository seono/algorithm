import sys
input = sys.stdin.readline

st = 1
N = int(input())
while st<N:
    st<<=1

segtree = [1e9]*(st<<1|1)

def update(node,ns,ne,s,e,k):
    if ne<s or ns>e: return
    if s<=ns and ne<=e:
        segtree[node]=min(segtree[node],k)
        while node:
            node>>=1
            segtree[node]=min(segtree[node<<1],segtree[node<<1|1])
        return
    mid = (ns+ne)>>1
    update(node<<1,ns,mid,s,e,k)
    update(node<<1|1,mid+1,ne,s,e,k)

def getmin(node,ns,ne,s,e):
    if ne<s or ns>e: return 1e9
    if s<=ns and ne<=e:
        return segtree[node]
    mid = (ns+ne)>>1
    return min(getmin(node<<1,ns,mid,s,e),getmin(node<<1|1,mid+1,ne,s,e))

arr = [[0,0,0] for _ in range(N)]
for i,num in enumerate(list(map(int,input().split())),1):
    arr[num-1][0]=i
for i,num in enumerate(list(map(int,input().split())),1):
    arr[num-1][1]=i
for i,num in enumerate(list(map(int,input().split())),1):
    arr[num-1][2]=i
arr.sort()
ans = 0
for x,y,z in arr:
    if getmin(1,1,st,1,y-1)>z:
        ans+=1
    update(1,1,st,y,y,z)
print(ans)