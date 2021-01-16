import sys
input = sys.stdin.readline
print = sys.stdout.write
nm_max=200001

def getIdx(a,b):
    ans = 0
    while a<=b:
        if a%2==1:ans+=tree[a]
        if b%2==0:ans+=tree[b]
        a = (a+1)>>1
        b = (b-1)>>1
    return ans

def update(idx,diff):
    while idx>0:
        tree[idx]+=diff
        idx>>=1
T = int(input())
while T:
    T-=1
    n, m = map(int,input().split())
    tree = [0]*(nm_max*4)
    st = 1
    while st<nm_max:
        st<<=1
    for i in range(st,st+n):
        tree[i]=1
    idx = [st+n-i for i in range(1,n+1)]
    temp = st
    while temp>0:
        ed = temp
        temp = temp>>1
        for i in range(temp,ed):
            tree[i]=tree[i<<1]+tree[i<<1|1]
    ed = st+n+m
    for i,num in enumerate(list(map(int,input().split()))):
        print("%d "%getIdx(idx[num-1]+1,ed))
        update(idx[num-1],-1)
        idx[num-1]=st+n+i
        update(idx[num-1],1)
    print("\n")