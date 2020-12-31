import sys
input = sys.stdin.readline

N = int(input())

arr = list(map(int,input().split()))
arr2 = {}
for idx,n in enumerate(list(map(int,input().split()))):
    arr2[n]=idx
tree = [0]*(N+1)

def sum(a,b):
    def sumidx(idx):
        ans = 0
        while idx>0:
            ans+=tree[idx]
            idx -= (idx & -idx)
        return ans
    return sumidx(b)-sumidx(a-1)

def update(idx,diff):
    while idx<=N:
        tree[idx]+=diff
        idx +=(idx & -idx)

def sol():
    ans = 0
    for n in arr:
        idx = arr2[n]
        ans+= sum(idx+1,N)
        update(idx+1,1)
    print(ans)
    return
sol()