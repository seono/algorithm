import sys
input = sys.stdin.readline
print = sys.stdout.write
N, M, K = map(int,input().split())
a_tree = [0]*(N+2)
b_tree = [0]*(N+2)
def update(tree,idx,diff):
    while idx<N+1:
        tree[idx]+=diff
        idx+=(idx&-idx)
def get(a,b):
    def getIdx(idx):
        ret = 0
        ret2 = 0
        tmp = idx
        while idx>0:
            ret+=a_tree[idx]
            ret2+=b_tree[idx]
            idx-=(idx&-idx)
        return ret*tmp+ret2
    return getIdx(b)-getIdx(a-1)
    
p=0
def rangeUpdate(L,R,diff):
    update(a_tree, L,diff)
    update(a_tree, R+1,-diff)
    update(b_tree, L,(-L+1)*diff)
    update(b_tree, R+1,R*diff)


for idx in range(1,N+1):
    n = int(input())
    rangeUpdate(idx,idx,n)
for _ in range(M+K):
    row = list(map(int,input().split()))
    L,R = row[1],row[2]
    if L>R:L,R=R,L
    if row[0]==1:
        rangeUpdate(L,R,row[3])
    else:
        print("%d\n"%get(L,R))