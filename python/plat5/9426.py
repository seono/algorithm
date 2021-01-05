import sys
input = sys.stdin.readline

tree = [0]*65537
arr = []
st,ed = 1,65536

def update(idx,n):
    while idx<=ed:
        tree[idx]+=n
        idx+=(idx&-idx)

def getIdx(idx):
    ans = 0
    while idx>0:
        ans+=tree[idx]
        idx-=(idx&-idx)
    return ans
best = 0
ans = 0
N, K = map(int,input().split())
for i in range(1,N+1):
    arr.append(int(input())+1)
    update(arr[-1],1)
    if i>=K:
        lo = st
        hi = ed
        while lo<=hi:
            m = (lo+hi)//2
            if getIdx(m)>=(K+1)//2:
                best = m
                hi = m - 1
            else:
                lo = m + 1
        ans+=best-1
        update(arr[i-K],-1)
print(ans)