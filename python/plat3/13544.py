import sys
import bisect
input = sys.stdin.readline
output = sys.stdout.write

N = int(input())
st = 1
while st<N:
    st<<=1
tree = [[] for _ in range(st*2)]
tmp = st
for i,num in enumerate(list(map(int,input().split())),st):
    tree[i]=[num]
while tmp>1:
    ed = tmp
    tmp = tmp>>1
    for i in range(tmp,ed):
        l,r = 0,0
        left,right = len(tree[i<<1]),len(tree[i<<1|1])
        while l<left or r<right:
            if r==right or l<left and tree[i<<1][l]<tree[i<<1|1][r]:
                tree[i].append(tree[i<<1][l])
                l+=1
            else:
                tree[i].append(tree[i<<1|1][r])
                r+=1
def query(node,ns,ne,s,e,k):
    if ns>e or ne<s: return 0
    if s<=ns and ne<=e:
        return len(tree[node]) - bisect.bisect_right(tree[node],k)
    mid = (ns+ne)>>1
    return query(node<<1,ns,mid,s,e,k)+query(node<<1|1,mid+1,ne,s,e,k)
M = int(input())
ans = 0
for i in range(M):
    a,b,c = map(int,input().split())
    i,j,k = a^ans,b^ans,c^ans
    ans = query(1,1,st,i,j,k)
    output("%d\n"%ans)