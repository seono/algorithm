import sys
import bisect
input = sys.stdin.readline
print = sys.stdout.write
N = int(input())
st = 1
while st<N:
    st*=2
tree = [[] for _ in range(4*N)]

for i,num in enumerate(list(map(int,input().split())),st):
    tree[i]+=[num]

temp = st
while temp>1:
    ed = temp
    temp = temp//2
    for i in range(temp,ed):
        tree[i]=[]
        left,right=0,0
        l,r = len(tree[i<<1]),len(tree[i<<1|1])
        while left<l or right<r:
            if right==r or (left<l and tree[i<<1][left]<tree[i<<1|1][right]):
                tree[i].append(tree[i<<1][left])
                left+=1
            else:
                tree[i].append(tree[i<<1|1][right])
                right+=1
        
def greater(s, e, k, node, ns, ne):
    if ne<s or ns>e:return 0
    if s<=ns and ne<=e:
        a= len(tree[node])-bisect.bisect_right(tree[node],k)
        return a
    mid = (ns+ne)//2
    return greater(s,e,k,node<<1,ns,mid)+greater(s,e,k,node<<1|1,mid+1,ne)
q = int(input())
for i in range(q):
    i,j,k=map(int,input().split())
    print("%d\n"%greater(i,j,k,1,1,st))