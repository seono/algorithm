import sys
input = sys.stdin.readline

M, N = map(int, input().split())
INF = sys.maxsize
arr = [INF]*400001

def get(s,e):
    ans = INF
    while s<=e:
        if s%2==1:ans=min(ans,arr[s])
        if e%2==0:ans=min(ans,arr[e])
        s = (s+1)//2
        e = (e-1)//2
    return ans

st = 1
while st<M:
    st*=2
for i in range(M):
    arr[st+i]=int(input())

temp = st
while temp>1:
    ed = temp
    temp = temp//2
    for i in range(temp,ed):
        arr[i]=min(arr[i*2],arr[i*2+1])

for _ in range(N):
    a,b = map(int, input().split())
    print(get(st+a-1,st+b-1))