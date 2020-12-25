import sys
input = sys.stdin.readline

N, M = map(int, input().split())
arr = [0]*(N+1)
tree = [0]*(N+1)

def get(a,b):
    def getIdx(i):
        ans = 0
        while i>0:
            ans+=tree[i]
            i-=(i&-i)
        return ans
    return getIdx(b)-getIdx(a-1)

def update(a,b):
    while a<N+1:
        tree[a]+=b
        a+=(a&-a)

for _ in range(M):
    cmd, a, b = map(int,input().split())
    if cmd==0:
        if a>b:
            print(get(b,a))
        else:
            print(get(a,b))
    else:
        diff = b-arr[a]
        update(a,diff)
        arr[a]=b