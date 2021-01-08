import sys
input=sys.stdin.readline
N = int(input())
tree = [0]*(N+1)

def get(n):
    def getIdx(idx):
        ans = 0
        while idx>0:
            ans+=tree[idx]
            idx-=(idx&-idx)
        return ans
    st = n
    ed = N
    while st<=ed:
        mid = (st+ed)//2
        if getIdx(mid)<=mid-n:
            ed = mid-1
        else:
            st = mid+1
    update(st,1)
    return st
    
def update(idx, diff):
    while idx<=N:
        tree[idx]+=diff
        idx+=(idx&-idx)
ans = [0]*N
for i in range(1,N+1):
    n = int(input())
    ans[get(n+1)-1] = i
print('\n'.join(map(str,ans)))