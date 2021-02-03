import sys
import bisect
input = sys.stdin.readline
output = sys.stdout.write
N, C = map(int,input().split())
st = 1
while st<N:
    st<<=1
tree = [[] for _ in range(st<<1)]
tmp = st
flag = [-1]*(st<<1)
for i,num in enumerate(list(map(int,input().split())),st):
    tree[i]=[num]
    flag[i]=num
while tmp>1:
    ed = tmp
    tmp = tmp>>1
    for i in range(tmp,ed):
        l,r=0,0
        left,right = len(tree[i<<1]),len(tree[i<<1|1])
        while l<left or r<right:
            if r==right or (l<left and tree[i<<1][l]<tree[i<<1|1][r]):
                tree[i].append(tree[i<<1][l])
                l+=1
            else:
                tree[i].append(tree[i<<1|1][r])
                r+=1
        n = 0
        x = len(tree[i])/2
        for num in set(tree[i]):
            l = bisect.bisect_left(tree[i],num)
            r = bisect.bisect_right(tree[i],num)
            if r-l>x:
                flag[i]=num
                break
def query(node,ns,ne,s,e):
    if ne<s or ns>e:return []
    if s<=ns and ne<=e:
        if flag[node]>0:
            return [flag[node]]
        return []
    mid = (ns+ne)>>1
    return query(node<<1,ns,mid,s,e)+query(node<<1|1,mid+1,ne,s,e)

def query2(node,ns,ne,s,e, num):
    if ne<s or ns>e:return 0
    if s<=ns and ne<=e:
        return bisect.bisect_right(tree[node],num)-bisect.bisect_left(tree[node],num)
    mid = (ns+ne)>>1
    return query2(node<<1,ns,mid,s,e,num)+query2(node<<1|1,mid+1,ne,s,e,num)


M = int(input())

for i in range(M):
    a,b = map(int,input().split())
    p_list = query(1,1,st,a,b)
    total = b-a+1
    check = True
    for num in p_list:
        if query2(1,1,st,a,b,num)>total/2:
            output("yes %d\n"%num)
            check = False
            break
    if check:
        output("no\n")