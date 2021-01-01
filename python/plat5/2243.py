import sys
input = sys.stdin.readline
output = sys.stdout.write

def getidx(idx):
    ans = 0
    while idx>0:
        ans+=tree[idx]
        idx-=(idx&-idx)
    return ans

def get(idx):
    st = 1
    ed = 1000000
    while st<ed:
        mid = (st+ed)//2
        p = getidx(mid)
        if p>=idx:
            ed = mid
        else:
            st = mid+1
    update(st,-1)
    return st


def update(idx,diff):
    while idx<=1000000:
        tree[idx]+=diff
        idx+=(idx&-idx)

n = int(input())
tree = [0]*1000001
for _ in range(n):
    arr = list(map(int,input().split()))
    if arr[0]==1:
        print(get(arr[1]))
    else:
        update(arr[1],arr[2])