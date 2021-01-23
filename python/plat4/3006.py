import sys
input = sys.stdin.readline

N = int(input())
tree = [0]*(N+1)
def update(idx,diff):
    while idx<=N:
        tree[idx]+=diff
        idx+=(idx&-idx)
def get(idx):
    ans = 0
    while idx>0:
        ans+=tree[idx]
        idx-=(idx&-idx)
    return ans
for i in range(1,N+1):
    update(i,1)
arr = {int(input()):idx for idx in range(1,N+1)}
left,right=1,N
while True:
    print(get(arr[left]-1))
    update(arr[left],-1)
    left+=1
    if left>right:break
    print(get(N)-get(arr[right]))
    update(arr[right],-1)
    right-=1
    if left>right:break