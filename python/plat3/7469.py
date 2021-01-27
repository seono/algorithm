import sys
import bisect
input = sys.stdin.readline
output = sys.stdout.write
n, m = map(int,input().split())
st = 1
while st<n:
    st*=2
tree = [[] for _ in range(4*n)]
arr = list(map(int,input().split()))
tmp = {}
tmp2 = {}
for i,x in enumerate(sorted(arr)):
    tmp[x]=i
    tmp2[i]=x
for idx,num in enumerate(arr,st):
    tree[idx]=[tmp[num]]
tmp = st
while tmp>1:
    ed = tmp
    tmp = tmp//2
    for i in range(tmp,ed):
        left,right = 0,0
        l,r = len(tree[i<<1]),len(tree[i<<1|1])
        while left<l or right<r:
            if right==r or (left<l and tree[i<<1][left]<tree[i<<1|1][right]):
                tree[i].append(tree[i<<1][left])
                left+=1
            else:
                tree[i].append(tree[i<<1|1][right])
                right+=1
def find(s,e,node,ns,ne,x):
    if ne<s or ns>e:return 0
    if s<=ns and ne<=e:return bisect.bisect_right(tree[node],x)
    mid = (ns+ne)>>1
    return find(s,e,node<<1,ns,mid,x) + find(s,e,node<<1|1,mid+1,ne,x)
for _ in range(m):
    i,j,k = map(int,input().split())
    l,r = 0,n
    while l<=r:
        mid = (l+r)>>1
        if find(i,j,1,1,st,mid)<k:
            l=mid+1
        else:
            r=mid-1
    output("%d\n"%tmp2[l])